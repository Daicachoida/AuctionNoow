# Architecture Research — AuctionNoow

| Thuộc tính | Nội dung |
|---|---|
| Ngày nghiên cứu | 2026-11-09 |
| Trạng thái | Nghiên cứu và khuyến nghị; chưa phải Architecture Design hay quyết định phát hành |
| Đầu vào nội bộ | [Phạm vi MVP](../01-product/01b-mvp-scope.md), [yêu cầu và quy tắc](../02-requirements/02-requirements-business-rules.md), [use case](../03-use-cases/03-use-cases-user-flows.md) |
| Mục tiêu | So sánh công nghệ theo yêu cầu thực tế, giải thích lợi ích và chi phí đánh đổi, xác định quyết định cần chốt trước khi thiết kế chi tiết |

## 1. Kết luận nghiên cứu

AuctionNoow cần bảo đảm **một thứ tự đặt giá chính thức, một người thắng, khả năng truy vết và quy trình thanh toán thật ở tầng B**. Tài liệu yêu cầu ưu tiên tính đúng hơn tốc độ hiển thị (NFR-01), xử lý gửi lặp (NFR-02) và ghi nhật ký thay đổi trọng yếu (NFR-03). Mức thử **50 yêu cầu đặt giá vào cùng phiên trong một giây** là đề xuất BA, chưa phải quy mô tải đã chốt hoặc kết quả đo.

| Nhóm | Khuyến nghị | Tình trạng |
|---|---|---|
| Giao diện | Next.js + TypeScript + Tailwind; Zustand cho trạng thái giao diện cần chia sẻ | Stack người dùng đã chọn |
| Backend | Java Spring Boot; microservices chia theo nghiệp vụ, giữ số service ban đầu ít | Stack và hướng microservices đã chọn; ranh giới service là đề xuất |
| Dữ liệu nghiệp vụ | PostgreSQL là nguồn chính; mỗi service sở hữu database/schema và tài khoản truy cập riêng | Đề xuất |
| Cache và phân phối cập nhật | Redis cho cache đọc, giới hạn tần suất và tín hiệu cập nhật SSE giữa các bản sao | Redis đã được người dùng chọn; cách dùng là đề xuất |
| Sự kiện nghiệp vụ | RabbitMQ + transactional outbox + consumer xử lý lặp | Đề xuất |
| Cập nhật trang phiên | SSE xuống trình duyệt; HTTP cho đặt giá và mua ngay | Đề xuất |
| Thông báo đẩy | Firebase Cloud Messaging (FCM); lưu lịch sử thông báo trong PostgreSQL | FCM là lựa chọn người dùng; cách lưu lịch sử là đề xuất |
| File | Tích hợp bằng API S3; MinIO cho thử nghiệm/tầng A; đánh giá lại hạ tầng lưu trữ production | MinIO là lựa chọn người dùng; phạm vi triển khai là khuyến nghị nghiên cứu |
| Xác thực | Dùng nhà cung cấp OIDC; Keycloak là ứng viên khi tự vận hành, chưa chốt | Đề xuất cần quyết định |
| Triển khai | Docker Compose ban đầu; quyết định hạ tầng production theo tải, khả năng sẵn sàng và đội vận hành | Compose ban đầu đã chọn; production chưa chốt |

Các kết luận dưới đây là **suy luận kiến trúc cho AuctionNoow** từ yêu cầu nội bộ và tài liệu chính thức. Nguồn tham khảo xác nhận cơ chế và giới hạn của công nghệ, không chứng minh một stack duy nhất là tốt nhất cho mọi quy mô.

## 2. Cách đánh giá

Mỗi phương án được so theo sáu tiêu chí: (1) tính đúng của đấu giá và tiền, (2) chịu tải, (3) công xây dựng, (4) công vận hành, (5) khả năng thay đổi nhà cung cấp, (6) phù hợp với tầng A rồi mở sang B. Khi chưa có số liệu tải, ngân sách và môi trường production, tài liệu không gán điểm số giả tạo hoặc cam kết SLO.

### 2.1. Microservices và ranh giới nghiệp vụ

**So sánh.** Modular monolith đơn giản hơn khi phát triển, kiểm thử và triển khai với đội nhỏ. Microservices cho phép triển khai độc lập nhưng phát sinh giao tiếp mạng, dữ liệu phân tán và giám sát xuyên service. Microsoft khuyến nghị xác định ranh giới theo nghiệp vụ, cho từng service sở hữu dữ liệu và tránh chia quá vụn. [Microsoft — Microservices](https://learn.microsoft.com/en-us/azure/architecture/microservices/), [Data considerations](https://learn.microsoft.com/en-us/azure/architecture/microservices/design/data-considerations).

**Khuyến nghị cho quyết định microservices đã chọn:** khởi đầu với bốn năng lực backend: tài khoản/danh tính nghiệp vụ, tin đăng/tìm kiếm, đấu giá, giao dịch sau đấu giá/vận hành. Payment là năng lực riêng khi xây tầng B. Đây là **ranh giới đề xuất để kiểm tra trong Architecture Design**, chưa phải danh sách deployment bất biến. Giữ kiểm tra giá, mua ngay, gia hạn và chốt phiên trong cùng năng lực Auction vì chúng cùng sửa trạng thái một phiên. Không tạo service riêng cho từng chức năng như đánh giá hoặc gửi email ở giai đoạn đầu.

**Điều kiện xem lại:** nếu luồng nghiệp vụ thường xuyên phải gọi đồng bộ qua nhiều service để hoàn thành một thao tác đơn giản, ranh giới đang bị chia sai; nếu một năng lực có tải hoặc chu kỳ phát hành độc lập rõ rệt, mới cân nhắc tách tiếp.

### 2.2. Database và tính đúng của lượt giá

**So sánh.** PostgreSQL cung cấp transaction, ràng buộc dữ liệu và khóa dòng; Redis/Firestore có thể xử lý tranh chấp ghi theo cách riêng nhưng sẽ thêm nguồn dữ liệu phải đồng bộ với các bảng giao dịch. PostgreSQL mô tả `SELECT ... FOR UPDATE` để chờ các thao tác tranh chấp trên cùng dòng. [PostgreSQL — Explicit locking](https://www.postgresql.org/docs/current/explicit-locking.html).

**Khuyến nghị:** PostgreSQL là nguồn sự thật cho phiên, lịch sử giá, kết quả, giao dịch và nhật ký. Auction tuần tự hóa các thay đổi cạnh tranh của cùng phiên trong transaction, dùng giờ máy chủ và ràng buộc duy nhất để chống hai kết quả. Redis không được quyết định giá hợp lệ, người thắng hoặc quyền mua ngay. Mỗi service quản lý dữ liệu riêng; có thể dùng chung máy chủ PostgreSQL lúc đầu nhưng không cho service khác đọc/ghi bảng thuộc quyền sở hữu của service kia. Dùng migration có phiên bản, ví dụ Flyway, thay vì sửa schema thủ công. [Flyway — Migrations](https://documentation.red-gate.com/fd/migrations-271585107.html).

**Cần kiểm chứng:** đo tranh chấp khóa khi nhiều yêu cầu cùng vào một phiên; thử đặt giá, mua ngay và đóng phiên cạnh tranh; kiểm tra khôi phục database từ bản sao lưu. PostgreSQL hỗ trợ khôi phục đến một thời điểm bằng base backup và WAL archive, nhưng phải thiết kế và thử quy trình phục hồi thực tế. [PostgreSQL — PITR](https://www.postgresql.org/docs/current/continuous-archiving.html).

### 2.3. Redis: cache, giới hạn tần suất và cập nhật tức thời

**So sánh.** Cache trong từng tiến trình dễ làm nhưng mỗi bản sao ứng dụng có dữ liệu và thời điểm hết hạn khác nhau. Redis cho nhiều bản sao dùng chung cache, đổi lại thêm hạ tầng và rủi ro dữ liệu cache cũ. Mẫu cache-aside dùng TTL và xóa cache khi ghi dữ liệu chính. [Redis — Cache-aside](https://redis.io/docs/latest/develop/use-cases/cache-aside/).

**Khuyến nghị:** triển khai Redis từ đầu theo lựa chọn người dùng, trước hết cho dữ liệu đọc nhiều như tin đăng công khai và trang phiên; thêm giới hạn tần suất theo tài khoản/IP cho endpoint nhạy cảm. Không cache kết quả kiểm tra cuối cùng của `POST /bids` hoặc `POST /buy-now`: Auction phải đọc trạng thái chính thức dưới khóa. Redis Pub/Sub có thể chuyển tín hiệu cập nhật tới nhiều bản sao SSE, nhưng nó có ngữ nghĩa *at-most-once*: subscriber mất kết nối có thể mất tin. Vì vậy trình duyệt phải tải lại snapshot chính thức khi kết nối lại. [Redis — Pub/Sub delivery](https://redis.io/docs/latest/develop/pubsub/).

**Điều kiện xem lại:** TTL và phạm vi cache phải đo theo độ trễ chấp nhận được; không tự đặt thời gian hết hạn dài cho dữ liệu có thể ảnh hưởng quyết định đặt giá. Redis bị lỗi có thể làm chậm trang và ảnh hưởng giới hạn tần suất, nhưng không được làm sai kết quả đã lưu.

### 2.4. RabbitMQ, Kafka và tính tin cậy của sự kiện

**So sánh.** RabbitMQ phù hợp để phân phối tác vụ và sự kiện nghiệp vụ tới consumer. Kafka mạnh ở lưu luồng sự kiện bền vững, phát lại và xử lý luồng lớn; năng lực đó chưa được yêu cầu hoặc đo tải trong tầng A. [RabbitMQ — Reliability](https://www.rabbitmq.com/docs/reliability), [Apache Kafka — Introduction](https://kafka.apache.org/documentation/).

**Khuyến nghị:** dùng RabbitMQ cho `AuctionClosed`, tạo giao dịch, thông báo và các cập nhật bất đồng bộ; dùng transactional outbox để thay đổi database và bản ghi sự kiện được commit cùng nhau. Consumer xử lý trùng bằng mã sự kiện hoặc ràng buộc nghiệp vụ, vì RabbitMQ có thể phát lại sau lỗi mạng. Không đưa việc **chấp nhận lượt giá** lên queue: người đặt giá cần câu trả lời từ transaction chính thức của Auction. [AWS — Transactional outbox](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html).

**Điều kiện chuyển Kafka:** có yêu cầu phát lại lịch sử dài, nhiều hệ thống phân tích độc lập hoặc lưu lượng sự kiện đã đo vượt thiết kế RabbitMQ. Kích thước dự án tự nó chưa phải lý do chuyển.

### 2.5. SSE, polling, WebSocket và FCM

**So sánh.** Polling dễ triển khai nhưng nhiều trình duyệt hỏi lặp lại dù giá không đổi. SSE là kết nối một chiều từ server tới trình duyệt, phù hợp với giá và giờ đóng mới; WebSocket có ích khi phải giao tiếp hai chiều liên tục. FCM là thông báo đẩy tới thiết bị và **không bảo đảm thứ tự giao**, nên không thể là kênh xác định thứ tự giá. [MDN — SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events), [Firebase — Delivery order](https://firebase.google.com/docs/cloud-messaging/customize-messages/collapsible-message-types).

**Khuyến nghị:** dùng HTTP cho lệnh đặt giá/mua ngay, SSE cho trang đang xem, FCM cho người dùng rời trang. Sau khi SSE ngắt hoặc trình duyệt mở lại, gọi API lấy trạng thái chính thức. Lưu thông báo trong PostgreSQL để người dùng xem lại. Với web push, FCM yêu cầu HTTPS, quyền thông báo của người dùng và service worker; không giả định mọi người dùng sẽ bật quyền. [Firebase — FCM for web](https://firebase.google.com/docs/cloud-messaging/web/get-started).

### 2.6. Ảnh, MinIO và object storage production

**So sánh.** Lưu ảnh trong PostgreSQL làm database giao dịch phình to; object storage phù hợp hơn cho file. API S3 hỗ trợ URL tải lên có thời hạn để client gửi file trực tiếp. MinIO có SDK tương thích S3, nhưng repository MinIO Community đã được chủ dự án chuyển sang trạng thái lưu trữ chỉ đọc từ 25/4/2026; README cũng ghi bản Community chỉ phát hành mã nguồn. Điều này làm tăng rủi ro duy trì khi tự vận hành production. [AWS — Presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html), [MinIO repository](https://github.com/minio/minio), [MinIO Java SDK](https://docs.min.io/aistor/developers/sdk/java/).

**Khuyến nghị:** giữ lựa chọn MinIO của người dùng cho phát triển và thử nghiệm tầng A; backend chỉ phụ thuộc giao diện S3. Trước production quy mô lớn, so chi phí vận hành, bản quyền/hỗ trợ và phương án sao lưu với object storage được quản lý. Catalogue lưu metadata và quyền sở hữu file trong PostgreSQL; ảnh bằng chứng và giấy tờ xác minh cần quyền truy cập khác ảnh tin công khai. Không đưa khóa truy cập object storage vào trình duyệt.

### 2.7. Xác thực, phân quyền và bảo mật API

**So sánh.** Tự viết luồng mật khẩu, khôi phục và phiên đăng nhập tạo nhiều công việc bảo mật; một nhà cung cấp OIDC chuẩn hóa phần này. Keycloak hỗ trợ các luồng đăng ký/xác minh email nhưng khi tự vận hành cũng cần database, TLS và phương án sẵn sàng cao. Spring Security có thể xác minh JWT theo issuer của nhà cung cấp OIDC. Chưa có quyết định của người dùng chọn Keycloak; Firebase chỉ được chọn cho FCM. [Keycloak — Administration](https://www.keycloak.org/docs/latest/server_admin/), [Production configuration](https://www.keycloak.org/server/configuration-production), [Spring Security — JWT](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/jwt.html).

**Khuyến nghị:** chốt **chuẩn OIDC** trước; so Keycloak tự vận hành với nhà cung cấp được quản lý sau khi biết môi trường production và ngân sách. Dù chọn nhà cung cấp nào, Identity vẫn sở hữu hồ sơ người bán, xác minh nghiệp vụ, khóa/hạn chế tài khoản; service Auction tự kiểm tra quyền thực hiện thao tác. Xác minh số điện thoại cần nhà cung cấp SMS/quy trình riêng, chưa thể coi là Keycloak đã giải quyết. Kiểm tra quyền trên từng đối tượng tin, phiên và tranh chấp vì lỗi phân quyền theo ID là rủi ro API phổ biến. [OWASP API Security Top 10](https://api-security.owasp.org/editions/2023/en/0x11-t10/).

### 2.8. Tìm kiếm tin đăng

**So sánh.** PostgreSQL có full-text search, index và xếp hạng cơ bản. OpenSearch cho cấu hình analyzer và tìm kiếm chuyên sâu hơn nhưng thêm một hệ thống chỉ mục phải đồng bộ và vận hành. [PostgreSQL — Full Text Search](https://www.postgresql.org/docs/current/textsearch.html), [OpenSearch — Search analyzers](https://docs.opensearch.org/latest/analyzers/search-analyzers/).

**Khuyến nghị:** bắt đầu với PostgreSQL cho lọc danh mục, giá, trạng thái và tìm kiếm cơ bản. Không mặc định khả năng tìm tiếng Việt có dấu/không dấu và lỗi chính tả đã đủ tốt: thử bộ truy vấn thực tế trước khi quyết định OpenSearch. Thêm OpenSearch khi chất lượng hoặc độ trễ tìm kiếm đo được không đạt mục tiêu.

### 2.9. Triển khai, quan sát và kiểm thử

**So sánh.** Docker Compose đã chọn giúp dựng đầy đủ các thành phần trên máy phát triển và có thể chạy trên một máy chủ; production nhiều máy, khả năng sẵn sàng cao và cập nhật không gián đoạn cần thiết kế triển khai riêng. Chưa có dữ liệu để chọn Kubernetes hoặc một nền tảng container cụ thể. [Docker — Compose in production](https://docs.docker.com/compose/how-tos/production/).

**Khuyến nghị:** chuẩn hóa log có correlation ID, metrics và trace xuyên service từ đầu; Spring Boot hỗ trợ Micrometer/OpenTelemetry, Prometheus hỗ trợ metrics và cảnh báo. Tự động kiểm thử với PostgreSQL/RabbitMQ thật bằng Testcontainers, chạy CI cho migration, API và trường hợp đấu giá đồng thời. Sao lưu PostgreSQL và object storage phải có **bài thử khôi phục**, không chỉ có lịch chạy backup. [Spring Boot — Observability](https://docs.spring.io/spring-boot/reference/actuator/observability.html), [Prometheus](https://prometheus.io/docs/introduction/overview/), [Testcontainers](https://java.testcontainers.org/modules/databases/postgres/), [GitHub Actions](https://docs.github.com/en/actions/get-started/continuous-integration).

### 2.10. Tầng B và tiền thật

Tầng A chỉ ghi lời khai giao dịch ngoài nền tảng, chưa đối soát. Tầng B cần đối tác giữ tiền đã ký, rà pháp lý và thử đối soát theo tài liệu MVP. Nghiên cứu kiến trúc khuyến nghị Payment là năng lực riêng: lưu mã giao dịch đối tác, trạng thái thanh toán/hoàn/giải ngân, yêu cầu idempotent và đối soát; xác nhận từ trình duyệt không đủ để đánh dấu tiền đã nhận. Quy trình qua nhiều service cần trạng thái chờ, thử lại và bù trừ khi lỗi. [AWS — Saga patterns](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/saga-patterns.html).

**Chưa chọn:** đối tác, giao thức webhook, cách giữ tiền, mô hình sổ tiền nội bộ, SLA và quy tắc giải ngân cuối cùng. Không thể chốt công nghệ tích hợp hoặc khẳng định phù hợp pháp lý trước các quyết định này.

## 3. Quyết định cần chốt và việc cần đo

| Ưu tiên | Việc cần chốt/đo | Ảnh hưởng đến thiết kế |
|---|---|---|
| 1 | Mức người dùng/phiên đồng thời, chỉ tiêu độ trễ đặt giá và thời gian khôi phục; xác nhận hoặc thay đề xuất 50 yêu cầu/giây cùng phiên | Kích thước database, số bản sao Auction, phương án triển khai và bài thử tải |
| 1 | Nhà cung cấp hạ tầng production và khả năng tự vận hành | OIDC provider, PostgreSQL/object storage được quản lý hay tự vận hành, triển khai nhiều máy |
| 1 | Chọn OIDC provider và nhà cung cấp xác minh số điện thoại/email | Luồng tài khoản, quyền và chi phí vận hành |
| 1 | Đánh giá lại MinIO cho production sau khi đã chọn hạ tầng, gồm hỗ trợ và khôi phục file | Độ bền ảnh tin, bằng chứng và giấy tờ riêng tư |
| 2 | Thử đồng thời đặt giá, mua ngay, gia hạn và đóng phiên; thử mất Redis/RabbitMQ/SSE | Chứng minh tính đúng và hành vi khi thành phần phụ gặp lỗi |
| 2 | Thử truy vấn tìm kiếm tiếng Việt có dấu, không dấu, sai chính tả | Quyết định có cần OpenSearch |
| Trước B | Chọn đối tác giữ tiền và thử webhook trùng/muộn, hoàn, giải ngân, đối soát | Thiết kế Payment và điều kiện mở tầng B |

**Đầu vào cho Architecture Design:** chỉ chuyển các lựa chọn đã chốt hoặc đã ghi rõ là giả định sang sơ đồ thành phần, sở hữu dữ liệu, trình tự nghiệp vụ và triển khai. Tài liệu nghiên cứu này không thay thế quyết định sản phẩm, rà pháp lý hoặc kết quả thử tải.
