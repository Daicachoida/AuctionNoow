# 02 — Requirements & Business Rules

## 1. Thông tin tài liệu và cách đọc

| Thuộc tính | Nội dung |
|---|---|
| Dự án | AuctionNoow — marketplace đấu giá, triển khai tại Việt Nam trước |
| Phiên bản | 0.5 — thêm D-09: PO chọn bảo vệ người mua giống Shopee (2026-11-09); P-15, P-16 đổi sang 15 ngày; thêm P-21, mục 9.6, FR-46–48, BR-42–43. Trước đó 0.4: D-08 tiền đặt trước theo Điều 39. Chờ xác minh pháp lý và thông số |
| Ngày rà soát | 2026-11-09 |
| Đầu vào | [01-product-scope.md](../01-product/01-product-scope.md) và các quyết định đã trao đổi |
| Mục đích | Xác định hành vi sản phẩm và quy tắc nghiệp vụ đủ rõ để thiết kế luồng, ước lượng, triển khai và kiểm thử MVP |
| Chủ quyết định | Chủ dự án / Product Owner (PO) |

**Trạng thái quyết định:** `Đã chốt` = PO đã chọn; `Đề xuất MVP` = BA đưa ra phương án cụ thể để PO duyệt; `Cần chốt` = còn thiếu lựa chọn; `Cổng phát hành` = phải xác minh trước khi cho giao dịch thật. Các con số đề xuất trong mục 9 là **giả định sản phẩm**, không phải quy định pháp luật hay quyết định đã chốt. Khi PO đồng ý, cập nhật trạng thái trong bảng quy tắc và tiêu chí nghiệm thu tương ứng.

**Quy tắc quản lý thay đổi:** mỗi quyết định mới cần cập nhật trạng thái, ngày, người quyết định và các yêu cầu / tiêu chí nghiệm thu liên quan. File này mô tả *sản phẩm phải làm gì*; [03-use-cases-user-flows.md](../03-use-cases/03-use-cases-user-flows.md) diễn giải luồng thao tác và [04-system-design.md](../04-system-design/04-system-design.md) dành cho cách hiện thực.

## 2. Phạm vi và nguyên tắc

### 2.1. Đã chốt từ Product Scope

- Marketplace đấu giá tổng hợp; C2C là trọng tâm nhưng cho phép cá nhân, shop, doanh nghiệp và nhà phân phối bán hàng.
- Phục vụ Việt Nam trước; mô hình nghiệp vụ phải có đường mở rộng quốc tế sau này.
- Nền tảng tham gia toàn bộ vòng đời giao dịch: đấu giá, xác định người thắng, điều phối thanh toán, theo dõi giao hàng, tranh chấp và uy tín; xác minh danh tính khi cần.
- **PO chốt cho MVP ngày 2026-09-30:** cho phép hàng mới, hàng cũ và đồ sưu tầm; đấu giá tăng dần thủ công kèm tùy chọn mua ngay; nút mua ngay tắt sau lượt đặt giá hợp lệ đầu tiên. Không có giá bảo lưu hoặc tự trả giá hộ. Lượt giá hợp lệ trong 2 phút cuối làm phiên kéo dài đến 2 phút sau lượt giá đó, lặp lại khi có lượt hợp lệ mới. Luồng thanh toán hướng tới cơ chế bảo đảm kiểu Shopee: tiền người mua trả được giữ cho tới khi đạt điều kiện giải ngân hoặc hoàn tiền.
- Chưa quyết định danh mục hàng cụ thể và danh mục cấm, đơn vị có quyền / trách nhiệm giữ tiền, nhà cung cấp thanh toán, điều kiện giải ngân, phí, SLA và mức tự động hóa MVP. Quyết định sau cùng về luồng giữ tiền **thay thế** lựa chọn sơ bộ trước đó là chuyển tiền thẳng cho người bán.

### 2.2. Ranh giới của bản MVP đề xuất

Một phiên đấu giá cho **một lô hàng**, một người thắng và một giao dịch tiếp theo; tài khoản, hồ sơ người bán, đăng hàng, duyệt / từ chối, tìm kiếm cơ bản, đặt giá, chốt phiên, xử lý thanh toán, cập nhật vận chuyển, khiếu nại và đánh giá. Đây là lát cắt để ước lượng, **chưa phải phạm vi MVP được PO phê duyệt**.

Chưa cam kết: đấu giá nhiều lô cùng lúc, đấu giá ngược, tự động đặt giá hộ, livestream, đa tiền tệ, giao dịch xuyên biên giới, ví nội bộ, **tự vận hành dịch vụ giữ tiền**, nhập catalog hàng loạt, quản lý nhiều nhân viên cho một shop. Nếu PO chọn tính năng nào trong số này, phải mở rộng yêu cầu và bộ kiểm thử trước khi triển khai. PO đã chọn chia MVP thành tầng A (thử nghiệm kín với giao dịch tiền thật có thể diễn ra trực tiếp giữa hai bên ngoài nền tảng; hệ thống không xử lý hoặc bảo vệ tiền) và tầng B (thanh toán bảo đảm bằng tiền thật qua đối tác), xem [01b-mvp-scope.md](../01-product/01b-mvp-scope.md). Cơ chế giữ tiền qua đối tác vẫn là mục tiêu của tầng B và chưa chọn nhà cung cấp.

### 2.3. Thuật ngữ

| Thuật ngữ | Định nghĩa dùng trong tài liệu |
|---|---|
| Tài khoản | Danh tính đăng nhập của một người dùng; việc một tài khoản vừa mua vừa bán còn cần xác nhận |
| Hồ sơ người bán | Danh tính bán hàng gắn với loại cá nhân / shop / doanh nghiệp / nhà phân phối |
| Lô hàng | Đơn vị được đưa ra đấu giá; có thể gồm một món hoặc một nhóm món theo mô tả |
| Tin đăng | Nội dung công khai của lô hàng, điều kiện bán và thông tin giao hàng |
| Phiên đấu giá | Khoảng thời gian áp dụng một bộ quy tắc nhận giá cho một lô hàng |
| Lượt đặt giá | Yêu cầu trả giá của một người mua; chỉ lượt được hệ thống xác nhận hợp lệ mới tham gia xếp hạng |
| Giá dẫn đầu | Giá cao nhất hợp lệ tại thời điểm được hiển thị; cách tính cần đổi nếu PO chọn đặt giá tự động |
| Người thắng | Người được xác định theo quy tắc phiên tại thời điểm đóng phiên; không đồng nghĩa giao dịch đã thanh toán |
| Giao dịch | Hồ sơ thực hiện mua bán được tạo sau khi có người thắng |
| Tranh chấp | Yêu cầu xem xét bất đồng sau hoặc trong quá trình giao dịch, có bằng chứng và kết quả xử lý |

## 3. Người tham gia và quyền cấp cao

| Vai trò | Quyền cần có trong lát cắt MVP đề xuất | Giới hạn |
|---|---|---|
| Khách chưa đăng nhập | Xem tin công khai, tìm kiếm, xem quy tắc chung | Không đăng hàng hoặc đặt giá |
| Người mua | Đặt giá, xem lịch sử của mình, thanh toán, theo dõi, mở tranh chấp, đánh giá khi đủ điều kiện | Không tự sửa kết quả phiên |
| Người bán | Tạo / sửa tin theo trạng thái cho phép, xem giá, thực hiện giao hàng, phản hồi tranh chấp | Không đặt giá trên phiên của chính mình |
| Vận hành / kiểm duyệt | Duyệt tin, xử lý báo cáo và tranh chấp, áp dụng biện pháp theo chính sách | Hành động phải có quyền, lý do và nhật ký |
| Dịch vụ ngoài | Gửi trạng thái thanh toán / vận chuyển / xác minh nếu được tích hợp | Không tự quyết định quy tắc đấu giá |

P-01 đề xuất bốn loại người bán dùng cùng quyền bán cơ bản trong MVP; chưa có nhân viên shop. Người đại diện tổ chức và bằng chứng quyền bán thay tổ chức phải được xác minh theo mô hình thực tế trước khi mở quyền bán.

## 4. Yêu cầu chức năng — ứng viên MVP

Mã `FR` dùng để truy vết sang user flow và kiểm thử. Các `FR` thể hiện năng lực dự kiến; tham số nghiệp vụ cụ thể trong mục 9 là **đề xuất BA** cho những chỗ còn mở, chưa được tự động xem là quyết định PO. Những cổng phát hành vẫn cần được kiểm tra riêng.

### 4.1. Tài khoản và hồ sơ người bán

| ID | Yêu cầu có thể quan sát / kiểm thử |
|---|---|
| FR-01 | Người dùng đăng ký, đăng nhập, đăng xuất và khôi phục quyền truy cập theo phương thức xác thực sẽ chọn; hệ thống không cho tài khoản bị khóa tham gia giao dịch. |
| FR-02 | Người dùng xem và sửa thông tin hồ sơ được phép; thay đổi thông tin quan trọng không được âm thầm thay đổi danh tính giao dịch cũ. |
| FR-03 | Người muốn bán khai loại người bán và thông tin cần thiết tương ứng; hệ thống thể hiện trạng thái `chưa xác minh / đang xét / đạt / bị từ chối / cần xác minh lại`. |
| FR-04 | Chỉ người bán đáp ứng điều kiện đã chốt và được xác minh theo yêu cầu áp dụng mới được phát hành tin bán. Thông tin xác minh không công khai nguyên bản cho người mua. |
| FR-05 | Người mua thấy thông tin công khai cần thiết về người bán và trạng thái uy tín / xác minh, không thấy dữ liệu nhạy cảm. |

**Đề xuất P-01:** một tài khoản vừa mua vừa bán; xác thực email và điện thoại trước khi đặt giá; người bán hoàn thành xác minh trước khi bán. Tuổi tham gia, dữ liệu và cách xác minh từng loại người bán, chuyển loại / nhiều hồ sơ và yêu cầu KYC sâu hơn phải rà theo mô hình thực tế. Xác minh người bán của nền tảng cần được rà theo Luật TMĐT 2025 và Nghị định 248/2026/NĐ-CP trước phát hành thật.

### 4.2. Hàng hóa, tin đăng và kiểm duyệt

| ID | Yêu cầu có thể quan sát / kiểm thử |
|---|---|
| FR-06 | Người bán tạo bản nháp cho một lô hàng với tiêu đề, mô tả, ảnh, danh mục, tình trạng, các khiếm khuyết đã biết, địa điểm gửi, thông tin vận chuyển và điều kiện đấu giá. Trường bắt buộc theo danh mục cần chốt. |
| FR-07 | Trước khi gửi duyệt, người bán xem lại tổng thông tin người mua sẽ thấy, bao gồm giá, phí dự kiến, chính sách giao hàng / đổi trả và điều kiện giao dịch áp dụng. |
| FR-08 | Tin không đạt kiểm tra bắt buộc được giữ ở trạng thái cần sửa kèm lý do; không mở phiên công khai. |
| FR-09 | Vận hành có thể duyệt, yêu cầu sửa, ẩn hoặc gỡ tin với lý do lưu lại; người bán được thông báo kết quả và hướng xử lý. |
| FR-10 | Khách xem và tìm tin theo từ khóa / danh mục / trạng thái; trang chi tiết nêu rõ mô tả hàng, người bán, giá, mốc thời gian, chi phí bổ sung và quy tắc phiên. |
| FR-11 | Sau khi đã có giá hợp lệ, thay đổi nội dung ảnh hưởng quyết định đặt giá phải đi qua cơ chế thông báo và xử lý phiên được PO chốt; không ghi đè lịch sử cũ. |

**Đã chốt:** MVP cho phép hàng mới, hàng cũ và đồ sưu tầm. **Đề xuất P-02–04:** giới hạn nhóm hàng vật lý phổ thông, mô tả tình trạng / bằng chứng rõ, duyệt thủ công tin đầu tiên và tin rủi ro, khóa sửa nội dung trọng yếu sau giá đầu tiên. Chính sách hàng cấm / hạn chế và chuẩn xác thực đồ sưu tầm cần rà trước phát hành.

### 4.3. Phiên đấu giá và đặt giá

| ID | Yêu cầu có thể quan sát / kiểm thử |
|---|---|
| FR-12 | Khi mở phiên, hệ thống chụp lại quy tắc áp dụng và thông tin cốt lõi của tin; thay đổi quy tắc sau đó phải có cơ chế rõ, không áp dụng hồi tố một cách âm thầm. |
| FR-13 | Trang phiên hiển thị giá khởi điểm, giá dẫn đầu, bước giá hoặc giá tối thiểu tiếp theo, thời điểm đóng hiện hành (được cập nhật khi gia hạn), chi phí có thể phát sinh và tình trạng của phiên. |
| FR-14 | Trước khi xác nhận đặt giá, người mua được xem số tiền định đặt cùng thông tin giao dịch quan trọng; hệ thống phản hồi `được chấp nhận` hoặc `bị từ chối` với lý do. |
| FR-15 | Mỗi yêu cầu đặt giá được kiểm tra tư cách người đặt, trạng thái phiên, giá và giới hạn liên quan. Chỉ giá đã được xác nhận hợp lệ mới làm thay đổi người dẫn đầu. |
| FR-16 | Người đặt thấy lượt của mình và trạng thái hiện tại; người tham gia được thông báo khi bị vượt giá hoặc khi phiên kết thúc theo chính sách thông báo. |
| FR-17 | Khi đến điều kiện đóng phiên, hệ thống khóa nhận giá, xác định kết quả một lần theo quy tắc đã công bố và lưu bằng chứng đủ để kiểm tra lại. |
| FR-18 | Hệ thống xử lý rõ hai kết quả khi đóng phiên: không có giá hợp lệ, hoặc người dẫn đầu hợp lệ thắng. Mua ngay là nhánh kết thúc riêng trước khi có giá hợp lệ. |
| FR-19 | Nếu phiên bị dừng / hủy, hệ thống công bố lý do và ảnh hưởng tới các lượt đặt đã có; không chuyển thành giao dịch thành công một cách ngầm định. |

**Đã chốt:** đấu giá tăng dần thủ công, có mua ngay trước lượt giá hợp lệ đầu tiên, không có giá bảo lưu hoặc tự trả giá hộ, có gia hạn mềm 2 phút cuối. **Đề xuất P-05–10:** thời lượng, bước giá, tiền đặt trước theo hướng Điều 39 (chỉ ở tầng B qua đối tác; P-07, D-08), rút / hủy giá qua vận hành và giữ chỗ mua ngay 10 phút ở tầng B.

**Luật gia hạn đã chốt:** nếu lượt giá hợp lệ được xác nhận khi thời gian còn lại `≤ 2 phút` và phiên chưa đóng, thời điểm đóng mới bằng thời điểm xác nhận lượt giá đó `+ 2 phút`. Mỗi lượt hợp lệ tiếp theo trong 2 phút cuối tiếp tục áp dụng; phiên đóng sau 2 phút không có lượt hợp lệ mới. Giờ đóng mới phải hiển thị cho người tham gia. Thời điểm máy chủ là chuẩn; thông báo có thể đến chậm nhưng không đổi kết quả chính thức. Cần thử cạnh tranh đồng thời và sát ranh giới trước phát hành.

#### Mua ngay — bổ sung từ quyết định PO

| ID | Yêu cầu có thể quan sát / kiểm thử |
|---|---|
| FR-38 | Nếu người bán bật mua ngay, phiên đang mở và chưa có lượt đặt giá hợp lệ, trang phiên hiển thị giá mua ngay, tổng chi phí dự kiến và điều kiện thanh toán bên cạnh lựa chọn đặt giá. Sau lượt giá hợp lệ đầu tiên, lựa chọn mua ngay biến mất. |
| FR-39 | Người mua đủ điều kiện có thể xác nhận mua ngay; hệ thống kiểm tra lại tính khả dụng của lô hàng tại thời điểm xác nhận và chỉ cho một người sở hữu quyền mua. Hành động mua ngay và lượt đặt giá đến đồng thời không được tạo hai người thắng / hai giao dịch bán cùng lô. |
| FR-40 | Nếu mua ngay được chốt hợp lệ trước bất kỳ lượt giá hợp lệ nào, phiên dừng nhận giá và tạo giao dịch ở giá mua ngay. Tầng A tạo giao dịch thử nghiệm ngay, không chờ xác nhận tiền ngoài nền tảng. Tầng B chỉ chốt sau xác nhận thanh toán của đối tác; khi giữ chỗ thất bại / quá hạn thì khôi phục theo P-10 nếu được duyệt. |

**Đề xuất P-10 cần PO duyệt và thử với đối tác thanh toán:** giá mua ngay tối thiểu, giữ chỗ, tạm dừng phiên và khôi phục khi không thanh toán. Chưa thể phát hành luồng mua ngay có tiền thật nếu đối tác không hỗ trợ xác nhận / hủy đáng tin cậy.

### 4.4. Giao dịch và thanh toán

| ID | Yêu cầu có thể quan sát / kiểm thử |
|---|---|
| FR-20 | Chỉ phiên có người thắng hợp lệ mới tạo một giao dịch gắn với phiên, người thắng, người bán, giá chốt và phiên bản điều kiện giao dịch. |
| FR-21 | Người thắng và người bán nhận thông báo kết quả; người thắng thấy số tiền cần trả, khoản phí / vận chuyển nếu có và hạn thanh toán sau khi PO chốt. |
| FR-22 | Hệ thống ghi nhận riêng trạng thái người mua trả tiền và trạng thái khoản tiền được giữ / được giải ngân / được hoàn. Không gộp `đã trả` với `đã chi cho người bán`; nguồn xác nhận mỗi trạng thái phải rõ. |
| FR-23 | Phản hồi thanh toán trùng lặp, đến muộn hoặc mâu thuẫn không được tạo nhiều giao dịch hoặc chuyển trạng thái sai; sự kiện được lưu để đối soát thủ công. |
| FR-24 | Khi thanh toán quá hạn / thất bại, hệ thống chuyển sang nhánh xử lý được công bố, thông báo các bên và không tự ý trao quyền mua cho người trả giá kế tiếp nếu chưa có quy tắc. |
| FR-25 | Vận hành có thể tra cứu và đối soát lịch sử giao dịch / thanh toán theo quyền được cấp, nhưng không tự sửa trực tiếp số tiền đã chốt. |

**Yêu cầu cho luồng bảo đảm tiền đã được PO chọn:**

| ID | Yêu cầu có thể quan sát / kiểm thử |
|---|---|
| FR-41 | Sau khi người mua thanh toán, hệ thống chỉ ghi `tiền đang được giữ` khi có bằng chứng từ nhà cung cấp / tài khoản bảo đảm được chọn; người bán thấy khoản dự kiến nhận và lý do chưa được giải ngân. |
| FR-42 | Khi đủ điều kiện giải ngân và không có tranh chấp chặn giải ngân, hệ thống gửi / ghi nhận yêu cầu giải ngân theo cơ chế của đối tác, đối soát kết quả và thông báo người bán. Yêu cầu lặp không tạo hai lần chi trả. |
| FR-43 | Khi giao dịch đủ điều kiện hoàn tiền, hệ thống gửi / ghi nhận yêu cầu hoàn qua đối tác, đối soát trạng thái hoàn và thông báo người mua; hoàn một phần nếu có phải theo chính sách đã chốt. |
| FR-44 | Tầng B: người đặt giá phải có khoản tiền đặt trước hợp lệ đang được giữ qua đối tác cho phiên đó trước lượt giá đầu tiên của mình trên phiên; trước khi nộp, hệ thống hiển thị số tiền, thời điểm hoàn và các trường hợp bị mất. Đề xuất theo D-08. |
| FR-45 | Khi phiên kết thúc: người không thắng được giải phóng hoặc hoàn đặt trước trong hạn đã công bố (tham chiếu 3 ngày làm việc); người thắng được chuyển khoản đó thành phần đã trả của giá chốt, không trừ hai lần; người vi phạm bị xử lý mất đặt trước theo quy tắc công bố, có nhật ký và thông báo các bên. Đề xuất theo D-08. |

**Đã chốt về kết quả mong muốn:** tiền người mua được giữ tới khi có điều kiện giải ngân / hoàn tiền, tương tự cơ chế bảo đảm của Shopee. **Cần chốt trước thiết kế và giao dịch thật:** đơn vị được phép giữ tiền, tài khoản pháp lý, hợp đồng với nhà cung cấp hỗ trợ nhiều người bán, quyền ra lệnh giải ngân / hoàn, thời hạn, phí, đối soát, thuế, hoàn tiền sau giải ngân và chargeback. Không mặc định AuctionNoow tự mở ví hay tự giữ tiền trong tài khoản ngân hàng của dự án. Không coi `thanh toán thành công` chỉ dựa vào việc người mua quay về trang thành công. Nếu chưa tìm được đối tác và cơ chế hợp lệ, luồng thanh toán bảo đảm chưa sẵn sàng phát hành; không âm thầm đổi sang chuyển thẳng tiền cho người bán.

### 4.5. Giao hàng, hoàn tất và tranh chấp

| ID | Yêu cầu có thể quan sát / kiểm thử |
|---|---|
| FR-26 | Sau trạng thái thanh toán đủ điều kiện, người bán thấy thông tin giao hàng cần thiết và hạn bàn giao; dữ liệu địa chỉ chỉ được hiện cho người có vai trò cần dùng. |
| FR-27 | Giao dịch có lịch sử trạng thái giao hàng: chờ gửi, đã bàn giao, đang vận chuyển, giao thành công, giao thất bại, trả lại hoặc ngoại lệ tương ứng. |
| FR-28 | Trạng thái giao hàng phải có nguồn và thời điểm cập nhật; người dùng phân biệt được trạng thái do bên vận chuyển xác nhận với trạng thái do người dùng tự khai. |
| FR-29 | Hệ thống chỉ đánh dấu `hoàn tất` khi đạt điều kiện sẽ chốt; giao thành công về mặt vận chuyển chưa tự động đồng nghĩa hết quyền khiếu nại. |
| FR-30 | Bên đủ điều kiện có thể mở tranh chấp với lý do, mô tả và bằng chứng; hệ thống cấp mã theo dõi, khóa bằng chứng liên quan và thông báo bên còn lại. |
| FR-31 | Vận hành xem hồ sơ, yêu cầu thêm chứng cứ, ghi quyết định có lý do, thông báo các bên và ghi hành động hoàn tiền / tiếp tục chi trả nếu cơ chế thanh toán cho phép. |
| FR-32 | Các nhánh không gửi hàng, giao thất bại, hàng sai mô tả, hủy / trả hàng và không phản hồi tranh chấp phải có chính sách, thời hạn và người chịu trách nhiệm được PO chốt trước khi thử nghiệm thật. |
| FR-46 | Tầng B: trong cửa sổ P-15, người mua tạo yêu cầu trả hàng / hoàn tiền bằng cách chọn một lý do hợp lệ ở P-21 và đính kèm bằng chứng; hệ thống cấp mã theo dõi và chặn giải ngân theo FR-30. Không có lý do "đổi ý". Đề xuất theo D-09. |
| FR-47 | Vận hành xem bằng chứng hai bên cùng bản mô tả đã khóa của tin (BR-09), ghi kết quả (hoàn sau khi trả hàng, hoàn không cần trả hàng, hoàn một phần, từ chối) kèm lý do, và thông báo các bên. Người bán có 48 giờ khiếu nại quyết định (P-16). Đề xuất theo D-09. |
| FR-48 | Hệ thống hiển thị cho vận hành lịch sử yêu cầu trả hàng / hoàn tiền và dấu hiệu gian lận của người mua khi ra quyết định, để không hoàn không cần trả hàng chỉ dựa vào lý do được chọn. Đề xuất theo D-09. |

**Đề xuất P-13–17:** dùng đơn vị có mã theo dõi, người mua trả phí hiển thị trước, người bán gửi trong 3 ngày làm việc, vận hành kiểm tra chứng cứ giao, giữ tiền 15 ngày lịch sau giao (PO chọn hướng Shopee, D-09) và chặn giải ngân khi có tranh chấp đúng hạn. Bảo hiểm, nhà vận chuyển và cơ chế hoàn / giải ngân thực tế phụ thuộc đối tác và quy chế đã rà.

### 4.6. Uy tín, báo cáo và vận hành

| ID | Yêu cầu có thể quan sát / kiểm thử |
|---|---|
| FR-33 | Sau giao dịch đủ điều kiện, các bên có thể đánh giá theo mẫu và giới hạn sẽ chốt; đánh giá gắn với giao dịch thật. |
| FR-34 | Người dùng báo cáo tin, người bán, người mua hoặc hành vi đặt giá đáng ngờ; vận hành nhận được hồ sơ và trạng thái xử lý. |
| FR-35 | Vận hành có thể tạm khóa tài khoản / tin / phiên theo quyền và lý do; tác động lên phiên đang mở hoặc giao dịch đang chạy phải theo quy trình riêng. |
| FR-36 | Mọi thay đổi trọng yếu — giá, kết quả, trạng thái thanh toán, vận chuyển, tranh chấp, kiểm duyệt — có nhật ký gồm tác nhân, thời điểm, trước / sau và lý do khi cần. |
| FR-37 | Báo cáo vận hành tối thiểu cho thấy số phiên mở / kết thúc, phiên có giá, phiên có người thắng, giao dịch thanh toán / hoàn tất, hủy và tranh chấp. Định nghĩa chỉ số cần khớp file 01. |

**Đề xuất P-18–20:** mỗi bên được đánh giá một lần sau giao dịch hoàn tất; vận hành xử lý đánh giá vi phạm, báo cáo, hạn chế tài khoản và kháng nghị với lý do / nhật ký. Phân quyền, nhân sự vận hành và mức xử lý tự động sẽ quyết định theo quy mô thử nghiệm.

## 5. Quy tắc nghiệp vụ

### 5.1. Quy tắc nền tảng và tư cách

| ID | Quy tắc | Trạng thái |
|---|---|---|
| BR-01 | Một phiên thuộc đúng một hồ sơ người bán và một lô hàng; hồ sơ người bán phải được liên kết với tài khoản chịu trách nhiệm. | Đề xuất MVP |
| BR-02 | Tài khoản bị khóa không được tạo tin, mở phiên hoặc gửi giá mới; ảnh hưởng tới phiên / giao dịch đang tồn tại phải do quy trình xử lý quyết định. | Đề xuất MVP |
| BR-03 | Người bán không được đặt giá trên phiên của chính mình. Tài khoản liên quan và thông đồng phải có chính sách phát hiện, xem xét và xử lý. | Đề xuất MVP |
| BR-04 | Quyền bán chỉ được mở sau khi hoàn thành xác minh người bán theo yêu cầu áp dụng cho mô hình thực tế. Trường dữ liệu, phương thức và thời hạn xác minh cần được rà soát. | Cổng phát hành |
| BR-05 | Người dùng thấy và đồng ý điều khoản liên quan trước khi đăng bán / đặt giá; hệ thống lưu phiên bản điều khoản đã áp dụng. | Đề xuất MVP |

### 5.2. Tin đăng và phiên

| ID | Quy tắc | Trạng thái |
|---|---|---|
| BR-06 | Tin thiếu trường bắt buộc, thuộc danh mục không được phép hoặc chưa đạt kiểm duyệt không thể mở phiên. Phạm vi hàng và dữ liệu bắt buộc đề xuất tại P-02–03; chính sách cấm / hạn chế cần rà trước phát hành. | Đề xuất P-02–03; cổng phát hành |
| BR-07 | Tin / phiên có trạng thái rõ: `nháp → chờ duyệt → đã duyệt / cần sửa / từ chối → chờ mở → đang mở → kết thúc / bị dừng`. Không cho chuyển trạng thái trái quy trình. | Đề xuất MVP |
| BR-08 | Giá khởi điểm, tiền tệ, thời điểm mở / đóng và quy tắc đấu giá phải hiển thị trước lượt đặt đầu tiên; P-05–06 đề xuất thời lượng và định dạng giá. | Đề xuất P-05–06 |
| BR-09 | P-04 đề xuất khóa trường mô tả / giá / hàng / giao hàng sau lượt giá đầu tiên; sai sót trọng yếu phải qua vận hành, lưu phiên bản và thông báo. | Đề xuất P-04 |
| BR-10 | P-09 đề xuất người bán tự dừng trước lượt giá đầu tiên; sau đó chỉ vận hành được dừng vì lý do có căn cứ, lưu lý do và thông báo. | Đề xuất P-09 |

### 5.3. Đặt giá và xác định người thắng

| ID | Quy tắc | Trạng thái |
|---|---|---|
| BR-11 | Chỉ tài khoản đủ điều kiện mới gửi giá; P-01 đề xuất xác thực email / điện thoại, ở tầng B, P-07 (PO chọn hướng 2026-11-09) yêu cầu có tiền đặt trước hợp lệ trước lượt giá đầu tiên trên phiên. Điều kiện tuổi và xác minh cần rà trước phát hành. | Đề xuất P-01; hướng đã chọn P-07; cổng phát hành |
| BR-12 | Lượt giá chỉ được xét khi phiên đang mở. Đề xuất dùng thời điểm hệ thống **ghi nhận lượt hợp lệ thành công** làm căn cứ và công bố mốc đó trong lịch sử; không dùng đồng hồ thiết bị người mua. Yêu cầu chưa được ghi nhận trước mốc đóng bị từ chối. | Đề xuất MVP |
| BR-13 | MVP dùng đấu giá tăng dần thủ công: người mua tự gửi từng giá, không có giá tối đa bí mật / tự trả giá hộ. P-06 đề xuất lượt đầu `≥ giá khởi điểm`, các lượt sau `≥ giá dẫn đầu + bước giá theo bậc`; lượt bằng giá đến sau bị từ chối. | Đã chốt kiểu; bước giá đề xuất P-06 |
| BR-14 | Một lượt giá được chấp nhận phải được ghi bền vững trước khi trả xác nhận. Lượt bị từ chối không làm đổi giá dẫn đầu và có lý do đủ để người dùng hiểu. | Đề xuất MVP |
| BR-15 | Hai lượt giá đến sát nhau được xét theo thứ tự ghi nhận thành công của hệ thống; chỉ lượt thỏa mức tối thiểu trên trạng thái mới nhất được nhận. Nếu bằng giá, lượt được ghi nhận trước có hiệu lực và lượt còn lại bị từ chối với giá tối thiểu mới. | Đề xuất MVP |
| BR-16 | Không cho người đặt giá hoặc người bán tự xóa lượt giá. P-08 đề xuất người mua chỉ yêu cầu vận hành hủy vì nhập nhầm rõ ràng hoặc mô tả đổi trọng yếu; có nhật ký, tính lại giá dẫn đầu và thông báo. | Đề xuất P-08 |
| BR-17 | Lượt giá hợp lệ được xác nhận trong 2 phút cuối (bao gồm đúng mốc 2 phút, trước thời điểm đóng) đặt giờ đóng mới bằng thời điểm xác nhận lượt đó cộng 2 phút. Lặp lại với mỗi lượt hợp lệ tiếp theo; lượt bị từ chối không gia hạn. | Đã chốt |
| BR-18 | Không có giá bảo lưu: giá khởi điểm là mức người bán chấp nhận bán; khi đóng phiên, người dẫn đầu hợp lệ thắng. Phiên không có giá hợp lệ không tạo người thắng. | Đã chốt |
| BR-19 | Kết quả chốt phiên phải có một bản ghi chính thức; xử lý lặp của tiến trình đóng phiên không tạo thêm người thắng hay giao dịch. | Đề xuất MVP |
| BR-20 | Hủy một phiên vì gian lận hoặc lỗi hệ thống cần căn cứ, người có thẩm quyền, cách báo cho các bên và cơ chế kháng nghị; P-09 và P-20 đề xuất xử lý thủ công có nhật ký. | Đề xuất P-09, P-20 |

**Quy tắc mua ngay bổ sung:**

| ID | Quy tắc | Trạng thái |
|---|---|---|
| BR-35 | Người bán có thể bật giá mua ngay khi tạo phiên; P-10 đề xuất giá mua ngay `≥ giá khởi điểm + một bước giá` và công bố trước khi người mua giao dịch. | Đã chốt tính năng; giá đề xuất P-10 |
| BR-36 | Một lô hàng chỉ có một kết quả bán chính thức. Nếu giữ chỗ mua ngay được ghi nhận trước thì lượt giá đến sau bị từ chối; nếu lượt giá hợp lệ được ghi nhận trước thì mua ngay bị từ chối. Không dùng giờ trên thiết bị người mua để phân xử. | Đề xuất MVP |
| BR-37 | Lượt đặt giá hợp lệ đầu tiên làm mất hiệu lực mua ngay; các yêu cầu mua ngay gửi sau đó bị từ chối. Tầng A chốt giao dịch thử nghiệm ngay khi xác nhận mua ngay hợp lệ, không xác nhận thanh toán ngoài nền tảng. P-10 đề xuất tầng B giữ chỗ 10 phút, tạm dừng phiên và khôi phục có giới hạn nếu đối tác không xác nhận thanh toán. | Đã chốt hiệu lực; giữ chỗ đề xuất P-10 |

### 5.4. Sau đấu giá

| ID | Quy tắc | Trạng thái |
|---|---|---|
| BR-21 | Giá chốt, người mua, người bán và điều kiện giao dịch của phiên thắng được giữ nguyên trong giao dịch; sửa đổi về sau phải theo một sự kiện nghiệp vụ có dấu vết. | Đề xuất MVP |
| BR-22 | Chỉ bằng chứng thanh toán từ nguồn được tin cậy theo mô hình đã chọn mới xác nhận `đã thanh toán`; ảnh chụp chuyển khoản hoặc URL quay về không đủ nếu chưa được đối soát. | Đề xuất MVP |
| BR-23 | P-11 đề xuất người thắng trả trong 48 giờ, nhắc sau 24 giờ; quá hạn hủy và cho người bán đăng lại. Không mặc định người thứ hai tự động thắng; tiền đặt trước của người bỏ thanh toán xử lý theo P-07 và BR-41; người tái phạm có thể bị hạn chế đặt giá. | Đề xuất P-11; hướng đã chọn P-07 |
| BR-24 | Tiền người mua thanh toán phải đi vào cơ chế giữ tiền đã được xác minh và chỉ được giải ngân / hoàn theo điều kiện công bố. Chủ thể giữ tiền, cơ chế pháp lý, phí và đối soát là `TBD`; luồng này chưa sẵn sàng phát hành tới khi có đối tác và rà soát áp dụng. | Đã chốt mục tiêu bảo đảm; chi tiết là cổng phát hành |
| BR-25 | Trạng thái giao hàng được cập nhật bởi nguồn xác định; cập nhật thủ công phải hiện rõ là tự khai / đã đối soát. | Đề xuất MVP |
| BR-26 | P-15–18 đề xuất xác minh giao hàng, giữ tiền 15 ngày lịch sau giao, chặn giải ngân khi có tranh chấp đúng hạn, rồi mới đủ điều kiện hoàn tất / đánh giá. | Đề xuất P-15–18; cổng thanh toán |
| BR-27 | Tranh chấp phải gắn một giao dịch và lý do; quyết định giải quyết có người xử lý, căn cứ, thời điểm, kết quả và thông báo. | Đề xuất MVP |
| BR-28 | Một giao dịch không thể đồng thời ở hai kết quả cuối mâu thuẫn (ví dụ đã hoàn tất và đã hoàn toàn bộ) nếu không có sự kiện điều chỉnh được kiểm soát. | Đề xuất MVP |
| BR-38 | Một khoản tiền được giữ chỉ được xử lý theo kết quả tài chính nhất quán: giải ngân, hoàn toàn bộ, hoặc chia phần nếu chính sách cho phép; thao tác lặp / phản hồi muộn phải đối soát. | Đề xuất MVP |
| BR-39 | P-16–17 đề xuất tranh chấp đúng hạn chặn giải ngân; vận hành giải quyết dựa trên chứng cứ và cho kháng nghị qua kênh hỗ trợ. Cách thực thi chặn / giải ngân phụ thuộc đối tác được chọn. | Đề xuất P-16–17; cổng thanh toán |
| BR-40 | Tiền đặt trước chỉ dùng cho mục đích bảo đảm phiên đó, giữ tách khỏi tiền của nền tảng và chỉ ghi nhận sau xác nhận từ đối tác (tham chiếu Điều 39 khoản 2). Không dùng cho mục đích khác. | Đề xuất D-08; cổng pháp lý và đối tác |
| BR-41 | Các trường hợp mất tiền đặt trước phải được công bố trước trong quy chế / điều khoản phiên, không thêm sau khi người dùng đã nộp. Tham chiếu các trường hợp ở Điều 39 khoản 6 (nguồn thứ cấp, cần đối chiếu văn bản chính thức): từ chối ký biên bản, rút lại giá, từ chối kết quả, bị truất quyền tham gia. | Đề xuất D-08; cổng pháp lý |
| BR-42 | Khi hoàn tiền mà người mua không phải trả hàng (hàng nghi giả hoặc chứng cứ rõ), người mua không được bán lại hoặc tặng lại hàng đó, và điều này phải nêu trong điều khoản. Cách xử lý hàng (tiêu hủy, thu hồi) cần chốt khi rà pháp lý. | Đề xuất D-09; cổng pháp lý |
| BR-43 | Yêu cầu sai sự thật, tráo đổi hoặc trả hàng đã dùng hỏng, và lạm dụng hoàn tiền bị hạn chế quyền yêu cầu hoặc tạm khóa tài khoản theo quy trình công bố trước, có nhật ký và quyền kháng nghị. | Đề xuất D-09 |

### 5.5. Uy tín, dữ liệu và tuân thủ

| ID | Quy tắc | Trạng thái |
|---|---|---|
| BR-29 | P-18 đề xuất mỗi bên đánh giá đối tác một lần sau giao dịch hoàn tất, trong 30 ngày; điểm đã gửi không sửa, đánh giá vi phạm có thể báo cáo. | Đề xuất P-18 |
| BR-30 | Trạng thái xác minh công khai không tiết lộ giấy tờ, số định danh, tài khoản ngân hàng hoặc dữ liệu nhạy cảm không cần thiết. | Đề xuất MVP |
| BR-31 | Báo cáo gian lận / hàng giả phải có đường tiếp nhận, người phụ trách và cách tạm xử lý tin / phiên / giao dịch. | Đề xuất MVP |
| BR-32 | Quy chế hoạt động, thông tin người bán / hàng hóa, cơ chế phản ánh, xử lý vi phạm và lưu trữ dữ liệu phải được rà theo quy định hiện hành với mô hình cụ thể trước khi mở giao dịch thật. | Cổng phát hành |
| BR-33 | Thời hạn lưu giữ, quyền truy cập, chia sẻ, xóa / ẩn dữ liệu cá nhân phải được xác định theo nhu cầu nghiệp vụ và quy định áp dụng; chưa đặt con số tùy ý. | Cổng phát hành |
| BR-34 | Chính sách hàng cấm / hạn chế, hàng giả, sở hữu trí tuệ và bằng chứng kiểm duyệt phải được phê duyệt trước khi cho đăng tin công khai. | Cổng phát hành |

## 6. Trạng thái và nhánh ngoại lệ cần đặc tả tiếp

Các trạng thái dưới đây là **mô hình nghiệp vụ đề xuất**, không quyết định triển khai dữ liệu hoặc API. Mỗi chuyển trạng thái phải được gắn sự kiện, người / nguồn gây ra và điều kiện cho phép.

| Đối tượng | Trạng thái chính | Nhánh ngoại lệ phải xử lý |
|---|---|---|
| Người bán | chưa xác minh → đang xét → đạt | từ chối, hết hiệu lực, cần xác minh lại, tạm khóa |
| Tin đăng | nháp → chờ duyệt → đã duyệt → công khai | cần sửa, từ chối, ẩn / gỡ |
| Phiên | chờ mở → đang mở → kết thúc | hoãn, tạm dừng, hủy, kết thúc không bán được |
| Giao dịch | chờ thanh toán → đã thanh toán → chờ gửi → đang giao → đã giao → hoàn tất | quá hạn, thanh toán thất bại, giao thất bại, tranh chấp, hủy, hoàn tiền |
| Khoản tiền | chờ người mua trả → đã trả / đang giữ → đủ điều kiện giải ngân → đã giải ngân | thanh toán lỗi, đang hoàn, hoàn toàn bộ / một phần, đối soát lệch |
| Tranh chấp | mở → chờ phản hồi / chứng cứ → đang xét → đã quyết định → đóng | rút yêu cầu, kháng nghị nếu có |

**Ma trận ngoại lệ tối thiểu:**

| Tình huống | Phản ứng yêu cầu | Quyết định còn thiếu |
|---|---|---|
| Không ai đặt giá | Đóng phiên không tạo giao dịch; thông báo người bán | Có tự đăng lại hay không |
| Mua ngay và giá hợp lệ đầu tiên gần như cùng lúc | Một kết quả bán chính thức: nếu giá được xác nhận trước thì mua ngay hết hiệu lực; nếu mua ngay được chốt trước thì không nhận giá tiếp | Thứ tự xử lý và lúc khóa lô hàng |
| Người mua ngay không thanh toán | Không âm thầm chuyển quyền mua hoặc mở lại phiên | Hạn trả, xử lý giá cũ, mở lại hay đăng lại |
| Hai giá hợp lệ gửi đồng thời | Chỉ một thứ tự chính thức; trả kết quả rõ cho cả hai | Quy tắc phá hòa và ranh giới thời gian |
| Giá đến sát / sau mốc đóng | Giá hợp lệ trong 2 phút cuối gia hạn như BR-17; giá đến từ thời điểm đóng trở đi bị từ chối | Cách thông báo khi người dùng nhìn thấy đồng hồ cũ |
| Người thắng không trả tiền | Không chuyển `đã thanh toán`; thông báo, mở quy trình xử lý | Hạn trả, chế tài, mời người thứ hai |
| Thanh toán báo thành công hai lần | Một giao dịch chỉ được xác nhận / ghi nhận số tiền đúng một lần; phần dư được đối soát | Nhà cung cấp, nguồn xác nhận, cách hoàn tiền |
| Giải ngân và tranh chấp đến gần như cùng lúc | Không chi trả trái chính sách đã công bố; có lịch sử xử lý để đối soát | Ranh giới thời gian, điều kiện chặn và quyền ra lệnh |
| Người bán không gửi hàng | Giữ trạng thái ngoại lệ và cho người mua mở yêu cầu | Hạn gửi, hoàn tiền, xử lý người bán |
| Giao hàng thất bại / hàng sai mô tả | Cho khai báo vấn đề, lưu chứng cứ, không tự hoàn tất khi còn tranh chấp | Thời hạn, chi phí trả hàng, người ra quyết định |
| Báo cáo giá ảo / hàng giả | Có mã vụ việc, lưu vết và thẩm quyền tạm xử lý | Tiêu chí can thiệp, hủy kết quả, kháng nghị |

## 7. Tiêu chí nghiệm thu mẫu cho luồng lõi

Các ví dụ dưới đây giúp QA và PO thấy mức độ chi tiết cần đạt. Các con số từ P-05–20 chỉ trở thành tiêu chí nghiệm thu cuối khi PO duyệt và cổng phát hành liên quan được xác minh.

1. **Đăng hàng:** Cho trước người bán đủ điều kiện và dữ liệu hợp lệ, khi gửi tin thì tin vào `chờ duyệt`; không tự mở phiên trước điều kiện duyệt được chốt. Tin thiếu trường bắt buộc trả lỗi theo trường.
2. **Đặt giá hợp lệ:** Nếu duyệt P-06, với giá dẫn đầu 100.000 VND, lượt 109.000 bị từ chối, lượt 110.000 được nhận và cập nhật lịch sử đúng một lần. Người đang dẫn đầu không tự nâng giá của mình.
3. **Đặt giá bị từ chối:** Với phiên đã đóng, tài khoản bị khóa, người bán tự đặt hoặc giá không đạt mức tối thiểu, hệ thống từ chối và không đổi giá dẫn đầu.
4. **Cạnh tranh đồng thời:** Cho trước hai yêu cầu tới cùng một phiên gần nhau, chỉ các lượt đáp ứng quy tắc trên trạng thái mới nhất được chấp nhận; kết quả chốt phiên có thể kiểm tra lại từ lịch sử.
5. **Đóng phiên:** Không có giá hợp lệ thì không tạo giao dịch; có người thắng theo quy tắc đã chốt thì tạo đúng một giao dịch, kể cả khi lệnh đóng phiên chạy lặp.
6. **Thanh toán:** Không đổi sang `đã thanh toán` chỉ vì người mua bấm nút hoặc tải trang thành công; chỉ đổi sau xác nhận từ nguồn đã chọn và lưu mã tham chiếu đối soát.
7. **Tranh chấp:** Nếu duyệt P-15–17, vụ được mở trong 15 ngày lịch sau giao được xác minh phải lưu chứng cứ và chặn yêu cầu giải ngân; vận hành thấy hạn phản hồi và lịch sử xử lý. Quyền khiếu nại theo quy định áp dụng cần được rà riêng.
8. **Mua ngay:** Sau lượt giá hợp lệ đầu tiên, không thể mua ngay. Nếu mua ngay được chốt trước, chỉ một giao dịch được tạo cho lô hàng; lượt đặt giá gửi đồng thời không tạo thêm người thắng. Khi mua ngay thất bại do hết hiệu lực hoặc lô đã bán, người mua thấy lý do và không bị tạo giao dịch.
9. **Giữ và giải ngân tiền:** Xác nhận người mua đã trả không tự động đổi trạng thái sang `đã giải ngân`. Nếu duyệt P-15–17, chỉ khi có bằng chứng giao và đã qua cửa sổ 15 ngày không tranh chấp thì mới đủ điều kiện gửi lệnh giải ngân; lệnh giải ngân / hoàn lặp không làm tiền chuyển hai lần.
10. **Giữ chỗ mua ngay:** Nếu duyệt P-10, khi A giữ chỗ thì B không thể đặt giá; thanh toán A được xác nhận trong 10 phút tạo đúng một giao dịch. Hết hạn, phiên mở lại với ít nhất 2 phút còn lại và không có người thắng / thanh toán giả.
11. **Gia hạn sát giờ:** Phiên đóng lúc 20:00, giá hợp lệ xác nhận lúc 19:59:30 thì giờ đóng mới là 20:01:30; giá tiếp lúc 20:00:45 thì giờ đóng mới là 20:02:45. Giá bị từ chối không gia hạn.
12. **Bỏ thanh toán (tầng B):** Nếu duyệt P-11, người thắng quá hạn thì giao dịch chuyển sang hủy với lý do, người bán được thông báo và có thể đăng lại; tiền đặt trước xử lý theo P-07 và BR-41, có nhật ký. Khi FR-24 chưa có quy tắc, hệ thống không tự trao quyền mua cho người đặt giá thứ hai. Hạn chế tài khoản được ghi nhật ký.

## 8. Yêu cầu chất lượng và dữ liệu

| ID | Yêu cầu | Tiêu chí cần chốt |
|---|---|---|
| NFR-01 | Tính đúng đắn của giá và kết quả được ưu tiên hơn tốc độ hiển thị; một phiên có một thứ tự sự kiện chính thức. | Cách xử lý đồng thời và sai lệch thời gian |
| NFR-02 | Các thao tác quan trọng có bảo vệ khỏi gửi lặp, tải lại trang hoặc thông báo trùng từ bên ngoài. | Tập thao tác và thời hạn lưu khóa chống lặp |
| NFR-03 | Có dấu vết cho giá, thay đổi tin, kiểm duyệt, xác minh, tiền, vận chuyển và tranh chấp; người dùng chỉ thấy phần được phép. | Thời hạn lưu và chính sách truy cập |
| NFR-04 | Thông tin cá nhân, giấy tờ xác minh, địa chỉ giao hàng và dữ liệu thanh toán được thu thập tối thiểu, kiểm soát quyền và bảo vệ trong truyền / lưu trữ. | Danh mục dữ liệu, nhà cung cấp, thời hạn giữ |
| NFR-05 | Thông báo chậm / thất bại không làm thay đổi kết quả chính thức; người dùng luôn có thể tra cứu trạng thái hiện tại. | Kênh thông báo và kỳ vọng thời gian |
| NFR-06 | Tình trạng sự cố phải có cách vận hành: dừng nhận giá / tạm dừng phiên, công bố và khôi phục theo chính sách. | Ngưỡng sự cố, có gia hạn / bù thời gian không |
| NFR-07 | Giao diện ban đầu dự kiến dùng tiếng Việt và VND; dữ liệu miền không được giả định mọi thị trường sau này cùng tiền tệ, múi giờ hoặc địa chỉ. | PO xác nhận thị trường và loại tiền MVP |
| NFR-08 | Có khả năng xuất / truy xuất hồ sơ giao dịch phục vụ hỗ trợ và rà soát theo quyền. | Định dạng, phạm vi dữ liệu, thời hạn |

Chưa có chỉ tiêu hiệu năng, tính sẵn sàng, quy mô đồng thời hoặc thời gian khắc phục sự cố được chốt. Không nên gán số tùy ý vào bản yêu cầu.

## 9. Gói quy tắc còn mở — BA đề xuất để PO duyệt

Phần này trả lời các câu hỏi còn mở bằng **một phương án MVP có thể triển khai và kiểm thử**. Các mức giá và thời hạn là đề xuất riêng cho AuctionNoow, được chọn để giảm nhánh xử lý trong dự án cá nhân; nguồn ở mục 11 chỉ chứng minh đây là các kiểu cơ chế đang được dùng, không chứng minh các con số này phù hợp với thị trường Việt Nam. Nếu PO chọn khác, sửa các dòng `BR` liên quan trước khi xây tính năng.

### 9.1. Tài khoản, hàng hóa và kiểm duyệt

| Mã | Phương án đề xuất | Tác động |
|---|---|---|
| P-01 | Một tài khoản có thể vừa mua vừa bán và có một hồ sơ bán trong MVP. Bốn loại người bán dùng cùng chức năng đăng bán cơ bản, khác thông tin xác minh; chưa có tài khoản nhân viên shop. Người mua xác thực email và số điện thoại trước khi đặt giá; người bán chỉ được đăng bán sau khi hoàn thành xác minh theo quy định áp dụng. Người tham gia tự xác nhận đủ tuổi theo điều khoản; ngưỡng tuổi và phương thức kiểm tra cần rà pháp lý. | FR-01–05; BR-01–05, BR-11 |
| P-02 | MVP nhận hàng hóa vật lý mới, cũ và sưu tầm trong các nhóm tiêu dùng phổ thông có thể vận chuyển, ví dụ đồ gia dụng, điện tử, thời trang, sách và đồ sưu tầm thông thường. Chưa nhận tài sản phải sang tên, hàng số / dịch vụ, hàng dễ hỏng và nhóm cần giấy phép hoặc kiểm định chuyên ngành cho tới khi có quy trình riêng. Đây là giới hạn vận hành MVP, không phải tuyên bố nhóm nào bị pháp luật cấm. | FR-06–11; BR-06, BR-34 |
| P-03 | Tin bắt buộc có ảnh thực tế, tình trạng `mới / đã dùng`, khiếm khuyết đã biết, số lượng, xuất xứ nếu người bán biết, phí / cách tính vận chuyển, chính sách hoàn trả và bằng chứng xác thực nếu quảng cáo là hàng thật / đồ sưu tầm có giá trị. Không cho tuyên bố “đã xác thực” nếu chưa có quy trình xác thực. | FR-06–11; BR-06, BR-09 |
| P-04 | Vận hành duyệt thủ công tin đầu tiên của mỗi người bán và mọi tin bị hệ thống / người dùng gắn cờ; có thể duyệt thêm theo mẫu rủi ro. Tin đang mở mà chưa có giá có thể xin chỉnh sửa nội dung không ảnh hưởng giá; sau lượt giá hợp lệ đầu tiên khóa các trường ảnh hưởng quyết định mua. Sai sót trọng yếu phải dừng phiên, thông báo và xử lý qua vận hành. | FR-09, FR-11; BR-09–10 |

Danh mục hàng cấm / hạn chế cuối cùng, tài liệu xác minh theo từng loại người bán và tuổi tham gia là **cổng phát hành**, cần đối chiếu luật và mô hình thực tế. P-01–04 chưa thay thế việc rà này.

### 9.2. Đấu giá, bước giá và mua ngay

| Mã | Phương án đề xuất | Tác động |
|---|---|---|
| P-05 | Người bán chọn thời lượng phiên **3, 5 hoặc 7 ngày**; mặc định 7 ngày. Thời điểm mở / đóng công bố trước khi có giá; gia hạn 2 phút cuối theo BR-17 đã chốt vẫn áp dụng. | FR-12–19; BR-08, BR-17 |
| P-06 | Giá khởi điểm và giá đặt là số nguyên VND, bội số 1.000 VND; giá khởi điểm tối thiểu 10.000 VND. Lượt đầu phải `≥ giá khởi điểm`. Sau đó, người mua khác phải đặt `≥ giá dẫn đầu + bước giá theo bậc` trong bảng dưới. Không cho người đang dẫn đầu tự nâng giá của mình. Hai lượt bằng giá không cùng được nhận; lượt đến sau phải trả theo giá tối thiểu mới. | FR-14–17; BR-13–15 |
| P-07 | **PO chọn hướng (2026-11-09): kiểm soát bỏ thanh toán bằng tiền đặt trước, làm giống cơ chế Điều 39 Luật Đấu giá tài sản.** Áp dụng ở **tầng B** (tiền thật qua đối tác); tầng A không thu hoặc giữ tiền qua nền tảng nên không có tiền đặt trước do hệ thống quản lý (xem 01b). Hướng tham chiếu: tiền đặt trước nằm trong khoảng 5%–20% giá khởi điểm; giữ tách riêng, không dùng cho mục đích khác; người không thắng được hoàn trong 3 ngày làm việc sau khi phiên kết thúc; người thắng được chuyển thành khoản đảm bảo / trả trước cho giao dịch; người bỏ thanh toán, rút giá hoặc từ chối kết quả mất khoản này theo quy tắc công bố trước. **Chưa chốt:** tỷ lệ cụ thể, thời điểm thu (Điều 39 gắn với "ngày mở cuộc đấu giá", khó áp nguyên văn cho phiên 3–7 ngày), người nhận khoản bị mất (luật: người có tài sản), tính hợp pháp theo phân loại pháp lý. Không tự động coi lượt đặt giá là thanh toán. Người tái phạm tạm hạn chế đặt giá theo quy trình công bố. | BR-11, BR-23, BR-40–41; FR-24, FR-35, FR-44–45 |
| P-08 | Người mua không tự rút giá. Có thể yêu cầu vận hành hủy lượt giá vì nhập nhầm số rõ ràng hoặc người bán thay đổi thông tin trọng yếu; vận hành ghi bằng chứng, lý do, thời điểm và thông báo những người bị ảnh hưởng. Nếu việc hủy thay đổi giá dẫn đầu, tính lại từ lịch sử còn hợp lệ. | BR-16; FR-15–19 |
| P-09 | Người bán tự dừng tin trước lượt giá đầu tiên nếu hàng không còn. Sau lượt giá đầu tiên, chỉ vận hành được dừng vì hàng mất / hỏng, tin sai trọng yếu, nghi gian lận hoặc yêu cầu có căn cứ khác; không được biến việc dừng thành bán cho người dẫn đầu. Mọi người đặt giá được thông báo. | BR-09–10, BR-20; FR-19 |
| P-10 | Giá mua ngay tối thiểu bằng `giá khởi điểm + một bước giá tại giá khởi điểm`; chỉ hiện khi chưa có giá hợp lệ. Tầng A: xác nhận mua ngay hợp lệ tạo ngay một giao dịch thử nghiệm, hai bên tự thanh toán bên ngoài; hệ thống không chờ hoặc xác nhận tiền. Tầng B: khi người mua xác nhận, giữ chỗ độc quyền **10 phút** và tạm dừng nhận giá / đồng hồ phiên. Thanh toán được đối tác xác nhận trong hạn thì bán ở giá mua ngay; nếu hết hạn / thất bại, trả lại trạng thái chưa có giá, tiếp tục thời gian còn lại trước khi giữ chỗ, nhưng tối thiểu còn 2 phút. Mỗi tài khoản chỉ được một lần giữ chỗ thất bại cho một phiên; mọi thay đổi được thông báo trên trang phiên. | FR-38–40; BR-35–37 |

**Bậc bước giá P-06 (đề xuất, tính theo giá dẫn đầu trước lượt mới):**

| Giá dẫn đầu | Bước giá tối thiểu |
|---|---:|
| Dưới 100.000 VND | 5.000 VND |
| Từ 100.000 đến dưới 1.000.000 VND | 10.000 VND |
| Từ 1.000.000 đến dưới 5.000.000 VND | 50.000 VND |
| Từ 5.000.000 đến dưới 20.000.000 VND | 100.000 VND |
| Từ 20.000.000 VND trở lên | 500.000 VND |

Ví dụ: giá khởi điểm 90.000 VND, lượt đầu có thể là 90.000 VND; lượt sau tối thiểu 95.000 VND. Nếu giá dẫn đầu là 100.000 VND, lượt tiếp tối thiểu 110.000 VND. Bậc giá là lựa chọn sản phẩm, cần thử với người mua / bán và điều chỉnh theo dữ liệu sử dụng. Luồng giữ chỗ P-10 cũng cần được thử kỹ cùng cổng thanh toán; nếu đối tác không hỗ trợ xác nhận / hủy đáng tin cậy, chưa phát hành mua ngay có thanh toán thật.

### 9.3. Thanh toán bảo đảm và giao hàng

| Mã | Phương án đề xuất | Tác động |
|---|---|---|
| P-11 | Người thắng đấu giá có **48 giờ** để thanh toán; nhắc ở mốc 24 giờ. Quá hạn thì hủy giao dịch với lý do, thông báo người bán, cho phép đăng lại tin sau rà soát. Không tự chuyển quyền mua cho người đặt giá thứ hai. | FR-20–24; BR-23 |
| P-12 | Người mua trả qua đối tác thanh toán; tiền vào cơ chế bảo đảm của đối tác / chủ thể được phép đã xác minh. AuctionNoow ghi riêng `đã trả`, `đang giữ`, `đủ điều kiện giải ngân`, `đã giải ngân`, `đang hoàn`, `đã hoàn`. Chỉ dùng trạng thái có thể đối soát từ đối tác. **Không chọn sẵn nhà cung cấp, tài khoản hay cách pháp lý giữ tiền.** | FR-22–25, FR-41–43; BR-22, BR-24, BR-38 |
| P-13 | Người bán chọn một đơn vị trong danh sách vận chuyển được nền tảng chấp nhận, bàn giao hàng có mã theo dõi trong **3 ngày làm việc** sau khi khoản tiền được xác nhận đang giữ. Người bán nhập mã vận đơn; trạng thái `đã giao` chỉ lấy từ nhà vận chuyển hoặc bằng chứng được vận hành kiểm tra, không chỉ từ lời người bán. Giai đoạn đầu chưa hỗ trợ tự giao / gặp mặt vì thiếu bằng chứng độc lập. | FR-26–29; BR-25 |
| P-14 | Phí vận chuyển do người mua trả theo số hiển thị trước khi đặt giá / mua ngay, trừ khi tin ghi miễn phí và người bán chịu. Không tự thay phí sau khi có giá hợp lệ; nếu phí thực tế thay đổi trọng yếu, cần bên mua đồng ý hoặc xử lý hủy theo chính sách. | FR-06–07, FR-21, FR-26 |
| P-15 | Sau khi nhà vận chuyển xác nhận giao, bắt đầu **15 ngày lịch** để người mua kiểm tra hàng và yêu cầu trả hàng / hoàn tiền (PO chọn hướng giống Shopee ngày 2026-11-09; mức 15 ngày lấy theo các bài báo về chính sách Shopee từ 2024, chưa đối chiếu trang chính thức). Nếu không có tranh chấp hợp lệ, hết ngày thứ 15 giao dịch đủ điều kiện giải ngân và hoàn tất theo kết quả đối tác. Bấm “đã nhận” trước hạn không tự rút ngắn 15 ngày (còn mở: có cho giải ngân sớm khi người mua xác nhận hài lòng không, xem D-09). Nếu chưa có bằng chứng giao đáng tin cậy thì chưa tự giải ngân. | FR-29, FR-41–43; BR-26, BR-38–39 |

Thời hạn P-15 chỉ là cửa sổ **giữ tiền của sản phẩm đề xuất**, không tự giới hạn quyền khiếu nại / yêu cầu theo quy định áp dụng. Trước khi dùng P-11–15 với tiền thật phải có đối tác hỗ trợ giữ, đối soát, giải ngân, hoàn tiền và phục vụ nhiều người bán theo hợp đồng; phải rà mô hình pháp lý, phí, thuế, xử lý hoàn / chargeback và khả năng giữ tiền khi tranh chấp. Nếu không đáp ứng, **không tự đổi sang thu tiền vào tài khoản cá nhân hoặc trả thẳng người bán**.

### 9.4. Tranh chấp, uy tín và vận hành thử nghiệm

| Mã | Phương án đề xuất | Tác động |
|---|---|---|
| P-16 | Người mua được mở tranh chấp trong 15 ngày lịch sau mốc giao được xác minh, hoặc khi quá hạn gửi / vận chuyển và hàng chưa tới. Vụ mở đúng hạn tạm chặn giải ngân; người bán có 3 ngày làm việc để phản hồi. Vận hành quyết định trong mục tiêu 5 ngày làm việc sau khi đủ chứng cứ, hoặc báo lý do kéo dài. Mỗi bên có thể kháng nghị một lần trong 48 giờ từ quyết định, kèm chứng cứ mới; tiền vẫn bị chặn cho tới khi kháng nghị đúng hạn được giải quyết. | FR-30–32; BR-26–27, BR-39 |
| P-17 | Kết quả có thể là tiếp tục giải ngân, hoàn toàn bộ sau trả hàng (nếu cần), hoàn một phần khi hai bên đồng ý, hoặc hủy / hoàn vì không giao hàng. Quyết định và chứng cứ phải lưu; khoản tiền chỉ chuyển sau xác nhận của đối tác. Tranh chấp phát sinh sau giải ngân phải đi theo quy trình riêng, không hứa có thể thu hồi tiền ngay. | FR-31–32, FR-41–43; BR-27–28, BR-38–39 |
| P-18 | Mỗi bên được đánh giá đối tác **một lần trên một giao dịch đã hoàn tất**, trong 30 ngày, thang 1–5 sao kèm nhận xét; không sửa điểm sau khi gửi, nhưng có thể báo cáo đánh giá vi phạm. Đánh giá bị tranh chấp được giữ ẩn tới khi vụ việc đóng. | FR-33; BR-29 |
| P-19 | Đợt thử nghiệm kín chưa thu phí nền tảng; phí do đối tác thanh toán / vận chuyển thu phải được hiển thị đúng bên chịu trước khi giao dịch. Sau thử nghiệm mới quyết định phí giao dịch. Chính sách giá cuối cùng cần rà hợp đồng và thuế. | FR-07, FR-21; mô hình kinh doanh |
| P-20 | Vận hành duyệt tin theo P-04, nhận báo cáo gian lận, có thể tạm ẩn tin hoặc khóa quyền đặt giá / bán hàng với lý do và nhật ký. Người dùng có đường liên hệ và gửi kháng nghị; hành động ảnh hưởng tiền / kết quả phiên phải được xem xét riêng, không tự sửa dữ liệu lịch sử. | FR-09, FR-34–37; BR-20, BR-31–32 |
| P-21 | **PO chọn hướng (2026-11-09): chính sách bảo vệ người mua giống Shopee.** Áp dụng ở **tầng B**. (1) Người mua có **15 ngày lịch** kể từ khi giao được xác minh để yêu cầu trả hàng / hoàn tiền (P-15). (2) Lý do hợp lệ: không nhận được hàng; hàng hỏng, thiếu hoặc sai sản phẩm; không đúng mô tả trong tin (tình trạng, khiếm khuyết, xuất xứ); nghi hàng giả hoặc nhái. **Không có lý do "đổi ý"**: đây là chỗ khác Shopee, vì lượt thắng đấu giá đã ràng buộc và hàng thường là hàng cũ hoặc sưu tầm (điều chỉnh, cần PO duyệt). (3) Nền tảng đứng giữa: vận hành xem bằng chứng (ảnh, video mở hộp, bản mô tả đã khóa theo BR-09, lịch sử hai bên) rồi quyết định. (4) Kết quả: hoàn sau khi trả hàng; hoàn không cần trả hàng khi chứng cứ rõ hoặc hàng nghi giả cần xử lý; hoàn một phần nếu hai bên đồng ý; từ chối nếu thiếu chứng cứ. Không mặc định hoàn không cần trả hàng chỉ vì người mua chọn lý do hàng giả; vận hành xét thêm lịch sử và dấu hiệu gian lận (FR-48). (5) Người mua không chịu phí trả hàng khi yêu cầu được chấp nhận; chi phí này và khoản hoàn do người bán chịu (cơ chế thu hồi từ người bán chưa chốt, xem D-09). (6) Người bán khiếu nại quyết định trong 48 giờ (P-16). (7) Hàng giả phát hiện sau 15 ngày: không hoàn tự động; người mua báo cáo qua FR-34 và giữ quyền theo luật; vận hành xử lý người bán. PO cần quyết định có hỗ trợ hoàn trong trường hợp này không (D-09). | FR-30–34, FR-46–48; BR-42–43 |

P-16–20 là quy tắc vận hành MVP đề xuất. Quy chế, điều khoản giao dịch, hàng cấm, bảo vệ dữ liệu và xử lý người bán phải được soạn / rà theo quy định hiện hành trước khi thử nghiệm có giao dịch thật. Cửa sổ 15 ngày ở P-15 và P-16 theo hướng PO chọn giống Shopee (D-09); các số khác ở đây là đề xuất riêng của AuctionNoow, không lấy nguyên từ Shopee, eBay hoặc Catawiki.

### 9.5. Kiểm soát việc người thắng bỏ thanh toán — PO chọn hướng tiền đặt trước (D-08)

Mục này ghi dữ liệu tham khảo cách các nền tảng và luật đấu giá xử lý. **Ngày 2026-11-09 PO chọn phương án 3 (tiền đặt trước, làm giống luật Việt Nam)**; kết luận và việc còn mở ở cuối mục. Thông tin lấy từ trang trợ giúp và bài tổng hợp công khai (nguồn ở mục 11, kiểm tra ngày 2026-11-07); chính sách có thể thay đổi nên phải đối chiếu lại khi triển khai.

| Nguồn | Hạn trả sau khi thắng | Kiểm soát trước khi thắng | Khi không trả |
|---|---|---|---|
| Catawiki | 3 ngày sau khi phiên đóng | Giữ một khoản trên thẻ (bid reservation) khi kích hoạt theo điều kiện tài khoản và ngưỡng giá, ví dụ người chưa từng mua trên nền tảng; trang trợ giúp ghi tổng khoản giữ không vượt 1.000 euro | Hủy bán, chặn đặt giá và mua; vẫn phải trả phí bảo vệ người mua; lô có thể được mời lại cho người đặt giá thứ hai và thứ ba; lô giá trị lớn có thể chuyển thu hồi nợ |
| eBay | Khoảng 4 ngày | Không đặt cọc theo chính sách chung; eBay có thử tự động thu tiền ngay khi phiên kết thúc tại một số thị trường (thông báo cho người bán ở Anh năm 2023) | Hủy đơn chưa trả; người bán có thể chuyển cho người đặt giá kế tiếp; ghi nhận lên tài khoản người mua và có thể hạn chế quyền mua; người bán được xem xét hoàn phí |
| Luật Đấu giá tài sản 2016 (kiểm tra văn bản hiện hành, vì có đề xuất sửa đổi) | Theo quy chế từng cuộc đấu giá | Tiền đặt trước bắt buộc: 5%–20% giá khởi điểm; vào tài khoản thanh toán riêng của tổ chức đấu giá; thu trong 3 ngày làm việc trước ngày mở cuộc đấu giá, trừ khi thỏa thuận khác; không được dùng cho mục đích khác; có thể thay bằng bảo lãnh ngân hàng | Người không trúng được hoàn trong 3 ngày làm việc; người trúng thì khoản này chuyển thành tiền đặt cọc; người từ chối ký biên bản, rút giá hoặc từ chối kết quả không được nhận lại, khoản đó thuộc người có tài sản đấu giá (nguồn thứ cấp, kiểm tra 2026-11-09). Áp dụng cho AuctionNoow hay không phụ thuộc phân loại pháp lý, chưa kết luận |

**Phương án (PO chọn phương án 3 ngày 2026-11-09; phương án 1 và 2 giữ lại để so sánh):**

| Phương án | Mô tả | Cần có | Rủi ro |
|---|---|---|---|
| 1 — Không đặt trước (nội dung P-07 trước 2026-11-09) | Chỉ cảnh báo và hạn chế tài khoản sau vi phạm | Không cần tích hợp thêm | Tỷ lệ bỏ thanh toán có thể cao; thiệt hại đã xảy ra trước khi chế tài |
| 2 — Giữ chỗ trên phương thức thanh toán theo điều kiện | Chỉ áp dụng cho tài khoản mới hoặc khi giá vượt ngưỡng; giải phóng khi không thắng | Đối tác thanh toán hỗ trợ giữ chỗ; PO chốt ngưỡng và điều kiện | Tăng độ phức tạp; có thể giảm số người đặt giá |
| 3 — Tiền đặt trước | Người đặt giá nộp trước, mất khi bỏ | Cơ chế giữ tiền đã xác minh; rà pháp lý về tính chất đặt trước / đặt cọc | Phụ thuộc cổng pháp lý và cổng giữ tiền ở D-04 |

**Các điểm cần quyết định kèm theo:** hạn trả của người thắng (P-11 hiện đề xuất 48 giờ; hai nền tảng trên dùng 3 đến 4 ngày); có cho phép mời người đặt giá kế tiếp trong thời hạn ngắn không (FR-24 hiện chỉ nói không tự trao quyền khi chưa có quy tắc, chưa cấm); người bỏ thanh toán có phải chịu khoản phí không hoàn không; mức hạn chế tài khoản khi tái phạm.

**Kết luận PO chọn (2026-11-09) và hệ quả thiết kế:**
- Tiền đặt trước chỉ chạy được khi có đối tác giữ tiền riêng (cổng D-04) và đã rà pháp lý. Vì vậy tầng A không thể chặn bỏ thanh toán, chỉ đo tỷ lệ bỏ (xem 01b).
- Điều 39 viết cho cuộc đấu giá có một ngày mở và một ngày kết thúc do tổ chức đấu giá tổ chức. AuctionNoow là sàn nhiều phiên kéo dài 3–7 ngày, mỗi phiên cần một khoản đặt trước riêng. Hai điểm cần thiết kế lại cho hợp: thời điểm thu (đề xuất: trước lượt giá đầu tiên của người đó trên phiên, cần luật sư xác nhận) và cách xử lý nhiều phiên đồng thời của một người.
- Nếu AuctionNoow không thuộc diện đấu giá tài sản, khoản này nhiều khả năng được xem là đặt cọc theo luật dân sự, với quy tắc xử lý riêng. Cần luật sư xác nhận trước khi dùng thuật ngữ trong điều khoản.
- Đặt trước làm tăng ma sát: người mua phải nộp tiền trước khi đặt giá. Chỉ số cần theo dõi: tỷ lệ người xem chuyển thành người đặt giá.
- Còn mở, cần PO chốt: tỷ lệ cụ thể trong khoảng 5%–20% (hoặc dùng ngưỡng cố định cho hàng giá thấp, vì 5% của 10.000 VND rất nhỏ), hạn trả P-11, việc mời người đặt giá kế tiếp (FR-24), người nhận khoản bị mất (luật: người bán; sàn có thu phí xử lý không).

### 9.6. Bảo vệ người mua — PO chọn hướng giống Shopee (D-09)

Ngày 2026-11-09 PO chọn làm chính sách bảo vệ người mua giống Shopee. Cột Shopee lấy từ các bài báo và hướng dẫn công khai (nguồn ở mục 11), chưa đối chiếu được trang trợ giúp chính thức của Shopee, và chính sách này đã đổi nhiều lần.

| Nội dung | Shopee (theo các nguồn trên) | AuctionNoow (D-09) |
|---|---|---|
| Cửa sổ yêu cầu trả hàng / hoàn tiền | 15 ngày kể từ khi giao thành công, áp dụng từ 26/02/2024 | 15 ngày lịch từ khi giao được xác minh (P-15, P-16) |
| Lý do | Hàng lỗi, sai mô tả, hết hạn và cả "thay đổi quyết định" ở một số sản phẩm; có nguồn ghi Shopee gần đây thu hẹp lý do này (chưa xác minh) | Không có "đổi ý" (P-21) |
| Ai quyết định | Shopee đứng giữa kiểm tra và xử lý | Vận hành AuctionNoow (FR-47) |
| Hàng giả, nhái | Không hoàn chỉ dựa vào lý do được chọn; xét lịch sử mua hàng và dấu hiệu gian lận | Giống (FR-48) |
| Phí trả hàng | Người mua không chịu | Giống, người bán chịu (cơ chế thu hồi chưa chốt) |
| Người bán khiếu nại | Trong 2 ngày | 48 giờ (P-16) |
| Tiền | Có phản ánh người bán thiếu vốn khi thời hạn kéo dài | Giữ qua đối tác tới hết 15 ngày (P-15), chưa giải ngân sớm |

**Chỗ AuctionNoow khác Shopee, cần PO duyệt:**
- Không có lý do đổi ý, vì lượt thắng đấu giá đã ràng buộc người thắng và hàng phần lớn là hàng cũ hoặc sưu tầm.
- Bản mô tả đã khóa của tin (BR-09) là căn cứ chính khi xét "không đúng mô tả", vì người bán không được đổi nội dung trọng yếu sau lượt giá đầu tiên.
- Quyết định thủ công ở giai đoạn thử nghiệm; chưa có công cụ tự động phát hiện gian lận.

**Còn mở (D-09):**
- Hàng giả phát hiện sau 15 ngày. Hàng giả thường lộ muộn; các sàn khác dùng 30 ngày (Whatnot) hoặc 90 ngày (Amazon). Cửa sổ 15 ngày có thể để người mua thiệt, nên cần quyết định có hỗ trợ ngoài cửa sổ hay không.
- Cơ chế thu hồi tiền hoàn từ người bán: giữ tiền người bán, ký quỹ hoặc đòi sau, vì hoàn cho người mua trước khi người bán đồng ý cần có nguồn tiền.
- Có cho giải ngân sớm khi người mua xác nhận hài lòng không.
- Nghĩa vụ của nền tảng theo Luật Bảo vệ quyền lợi người tiêu dùng 2023: nền tảng trung gian có thể phải chịu chung trách nhiệm nếu biết người bán vi phạm mà không xử lý kịp. Cần kênh báo cáo, quy trình xử lý nhanh và nhật ký việc đã làm (BR-31, BR-32). Đã đọc qua bài của Bộ Công Thương và báo chí, chưa đọc văn bản luật.

## 10. Quyết định PO cần đưa ra, theo thứ tự ưu tiên

| Mã | Câu hỏi cần quyết định | Tác động nếu để mở |
|---|---|---|
| D-01 | **Đã chốt** hàng mới, cũ và sưu tầm. PO duyệt / chỉnh danh mục, mô tả và duyệt tin ở P-02–04; chính sách cấm / hạn chế cần rà riêng. | FR-06–11, BR-06, BR-34 |
| D-02 | **Đã chốt** đấu giá tăng dần thủ công, mua ngay tắt sau giá đầu tiên, không giá bảo lưu / tự trả giá hộ, gia hạn 2 phút. PO duyệt / chỉnh thời lượng, bước giá, rút giá, hủy và giữ chỗ mua ngay ở P-05–10. | FR-12–19, FR-38–40, BR-13–20, BR-35–37 |
| D-03 | PO duyệt / chỉnh điều kiện tài khoản P-01 và nhánh bỏ thanh toán P-07; yêu cầu xác minh người bán / tuổi tham gia cần rà riêng. | FR-01–05, FR-24, BR-01–05, BR-11 |
| D-04 | **Đã chốt mục tiêu** giữ tiền đến khi đủ điều kiện giải ngân. PO duyệt / chỉnh P-11–12, P-15–17; tìm đối tác, hợp đồng, trách nhiệm giữ tiền, thuế / hoàn / chargeback là cổng phát hành. | FR-20–25, FR-41–43, BR-22–24, BR-38–39 |
| D-05 | PO duyệt / chỉnh vận chuyển, phí và chứng cứ giao ở P-13–14. | FR-26–29, BR-25–26 |
| D-06 | PO duyệt / chỉnh xử lý tranh chấp, đánh giá, phí thử nghiệm và vận hành ở P-16–20. | FR-30–37, BR-27–31 |
| D-07 | PO chọn quy mô thử nghiệm, ngân sách, lịch phát hành và kênh hỗ trợ. Các chỉ tiêu hiệu năng / bảo mật cụ thể chuyển sang file 05 sau khi biết quy mô. | NFR và kế hoạch thử nghiệm |
| D-08 | **PO đã chọn hướng (2026-11-09): phương án 3, tiền đặt trước theo cơ chế Điều 39.** Còn mở: tỷ lệ cụ thể, thời điểm thu, người nhận khoản bị mất, hạn trả (P-11), mời người đặt giá kế tiếp (FR-24), xác minh pháp lý. | FR-24, FR-44–45, BR-11, BR-23, BR-40–41; P-07, P-11 |
| D-09 | **PO đã chọn hướng (2026-11-09): bảo vệ người mua giống Shopee, cửa sổ 15 ngày.** Còn mở: hàng giả phát hiện sau 15 ngày, cơ chế thu hồi tiền hoàn từ người bán, giải ngân sớm khi người mua xác nhận, bỏ lý do "đổi ý" (PO duyệt), xác minh số liệu Shopee từ trang chính thức. | FR-30–32, FR-46–48, BR-26, BR-42–43; P-15, P-16, P-21 |

**Cổng phát hành riêng:** rà phân loại pháp lý của mô hình, xác minh người bán, quy chế nền tảng, chính sách hàng hóa, dữ liệu cá nhân, điều kiện nhà cung cấp thanh toán và nghĩa vụ thuế / hóa đơn theo cách vận hành thực tế. Các mục này chưa thể tuyên bố đạt chỉ bằng tài liệu 02.

## 11. Ghi chú nghiên cứu và nguồn

Nguồn được kiểm tra ngày 2026-09-30. Chúng cung cấp **khung rà soát** và ví dụ thiết kế; tài liệu này không đưa ra kết luận pháp lý cuối cùng cho AuctionNoow.

- [Luật Thương mại điện tử 122/2025/QH15](https://vanban.chinhphu.vn/?classid=1&docid=216503&pageid=27160&typegroupid=3) và [Nghị định 248/2026/NĐ-CP](https://vanban.chinhphu.vn/?docid=218747&orggroupid=2&pageid=27160), cùng có hiệu lực từ 01-07-2026. [Bộ Công Thương tóm lược](https://moit.gov.vn/tin-tuc/bo-cong-thuong-pho-bien-luat-thuong-mai-dien-tu-va-nghi-dinh-so-248-2026-nd-cp.html) các nội dung về xác thực người bán, thông tin, quy chế, phản ánh và xử lý nội dung trên nền tảng trung gian. Cần xác định chính xác AuctionNoow thuộc loại hình nào và áp dụng điều khoản nào.
- [Nghị định 52/2013/NĐ-CP](https://vanban.chinhphu.vn/?docid=167457&pageid=27160) từng định nghĩa website đấu giá trực tuyến trong khung thương mại điện tử. Đây là dấu hiệu phải rà **phân loại dịch vụ đấu giá trực tuyến** và quy định chuyển tiếp / hiện hành cùng Luật TMĐT 2025, không phải kết luận rằng toàn bộ quy định cũ còn áp dụng nguyên trạng. Cần phân biệt thêm với [Luật Đấu giá tài sản và văn bản hướng dẫn](https://vanban.chinhphu.vn/?docid=212171&pageid=27160) theo loại tài sản và mô hình vận hành.
- [Luật Bảo vệ quyền lợi người tiêu dùng 19/2023/QH15](https://vanban.chinhphu.vn/?classid=1&docid=208363&orggroupid=1&pageid=27160&previousPage=other+articles): nguồn để rà việc công bố thông tin, quyền của người mua và cơ chế giải quyết phản ánh / tranh chấp.
- [Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15](https://vanban.chinhphu.vn/?classid=1&docid=214590&pageid=27160&typegroup=): nguồn để rà thu thập, dùng, chia sẻ và lưu dữ liệu người dùng, đặc biệt hồ sơ xác minh.
- [Nghị định 52/2024/NĐ-CP về thanh toán không dùng tiền mặt](https://vanban.chinhphu.vn/?classid=1&docid=210262&pageid=27160): nguồn cần đối chiếu khi lựa chọn cách điều phối / nhận / giữ tiền và nhà cung cấp thanh toán.
- [Điều khoản dịch vụ Shopee](https://help.shopee.vn/portal/4/article/77243): mô tả khoản tiền người mua được lưu trong Tài khoản Đảm Bảo Shopee rồi chuyển cho người bán khi đạt điều kiện. Đây là tham khảo về hành vi sản phẩm, không chứng minh AuctionNoow được phép sao chép cùng cơ chế pháp lý.
- Tài liệu eBay về [cách đặt giá](https://www.ebay.com/help/buying/bidding/bidding?id=4003), [giá bảo lưu](https://www.ebay.com/help/selling/listings/selling-tips/best-offer?id=4143), [rút giá](https://www.ebay.com/help/invalid-bid-retraction-policy/rules-policies-buyers/invalid-bid-retraction-policy?id=4227) và [ngăn đặt giá ảo](https://www.ebay.com/help/selling-practices-policy/shill-bidding-policy/policies/selling-policies?id=4353) cho thấy các lựa chọn mà sàn phải công bố rõ. AuctionNoow đã quyết định không dùng giá bảo lưu trong MVP.
- [eBay: Buy It Now trong đấu giá](https://www.ebay.com/help/selling-buy-now/listings/selling-buy-now?id=4109) là ví dụ về việc nút mua ngay thường biến mất sau khi có người đặt giá; AuctionNoow áp dụng quy tắc đó vì PO đã chốt, không áp dụng các mức giá hoặc ngoại lệ của eBay.
- [Catawiki: giá bảo lưu](https://www.catawiki.com/en/help/unsold-lots/the-reserve-price-for-my-object-was-not-met-what-are-my-options), [tự trả giá hộ](https://www.catawiki.com/en/help/max-bids/what-is-a-max-bid-and-how-does-it-work) và [gia hạn cuối phiên](https://www.catawiki.com/en/help/buyer-terms/general-terms-of-use?1519129965=) là các ví dụ để so sánh. [eBay](https://www.ebay.com/help/buying/bidding/bidding?id=4003) cũng cho biết đang thử gia hạn ở một số danh mục; quy tắc 2 phút của AuctionNoow là quyết định riêng của PO.
- [eBay: thời lượng phiên](https://www.ebay.com/help/Selling/-/Listing_durations_and_timings?id=4652) và [Catawiki: bước giá theo bậc](https://www.catawiki.com/en/help/bidding-basics/how-is-the-next-minimum-bid-calculated) là cơ sở tham khảo cho P-05–06. [eBay: thanh toán ngay khi mua ngay](https://www.ebay.com/help/selling/creating-managing-listings/listings/immediate-payment-works?id=4151) là đối chiếu cho P-10; AuctionNoow đề xuất giữ chỗ có hạn vì phải xử lý việc quay lại từ cổng thanh toán. Các mốc và bậc VND là lựa chọn đề xuất riêng.
- [Shopee Đảm Bảo](https://help.shopee.vn/portal/4/article/79314) và [chính sách trả hàng / hoàn tiền](https://help.shopee.vn/portal/4/article/77251?seo=1) cho thấy cần phân biệt trạng thái giao hàng, cửa sổ khiếu nại và luồng tiền. Từ 2026-11-09 PO chọn làm theo hướng Shopee cho cửa sổ 15 ngày (D-09). AuctionNoow chưa sao chép bảo đảm hoặc mức bồi thường của Shopee, và các số vẫn cần đối chiếu trang chính thức.

- **Bổ sung kiểm tra ngày 2026-11-07 (kiểm soát bỏ thanh toán, mục 9.5):** các trang trợ giúp của [Catawiki về người mua không trả](https://auction.catawiki.com/en/help/seller-payment-issues/what-happens-if-a-buyer-doesn-t-pay), [mời lại người đặt giá thứ hai](https://auction.catawiki.com/en/help/seller-payment-issues/what-happens-if-the-buyer-does-not-pay-for-my-object), [giữ chỗ tiền khi đặt giá](https://auction.catawiki.com/en/help/bidding-basics/what-is-a-bid-reservation) và [khoản giữ tạm trên thẻ](https://www.catawiki.com/en/help/fees/why-is-there-a-temporary-hold-on-my-credit-card-from-catawiki); [chính sách mặt hàng chưa thanh toán của eBay](https://www.ebay.com.au/help/policies/payment-policies/unpaid-item-policy?id=4271) và [thông báo thu tiền khi phiên kết thúc của eBay Anh](https://www.ebay.co.uk/sellercentre/news/2023-september/unpaid-item). Đây là ví dụ cơ chế, không chứng minh con số nào phù hợp thị trường Việt Nam.
- **Kiểm tra ngày 2026-11-09 (tiền đặt trước, mục 9.5):** [bài của Luật Minh Khuê về mức tiền đặt trước](https://luatminhkhue.vn/quy-dinh-khoan-tien-dat-truoc-de-tham-gia-dau-gia-tai-san-la-bao-nhieu.aspx) tóm tắt Điều 39: mức 5%–20% giá khởi điểm, tài khoản thanh toán riêng, thời hạn thu và hoàn 3 ngày làm việc, khoản đặt trước chuyển thành đặt cọc khi trúng, các trường hợp không được nhận lại. Đây là nguồn thứ cấp; phải đối chiếu văn bản luật chính thức trước khi dùng trong điều khoản.
- **Điều 39 Luật Đấu giá tài sản:** [bài tổng hợp pháp lý về tiền đặt trước](https://luatminhkhue.vn/quy-dinh-tien-dat-truoc-tham-gia-dau-gia-bien-so-xe-o-to-the-nao.aspx) là nguồn thứ cấp, cần đối chiếu với văn bản chính thức. [Bộ Tư pháp đề xuất sửa đổi luật này trong năm 2026](https://baodauthau.vn/sua-doi-luat-dau-gia-tai-san-che-tai-manh-ngan-ngua-xu-ly-cac-hanh-vi-vi-pham-post197233.html), nên cần kiểm tra lại văn bản hiện hành trước khi dựa vào.
- **Shopee, thời điểm ghi nhận tiền cho người bán:** [bài tổng hợp bên thứ ba](https://www.misaeshop.vn/?p=40941) mô tả tiền được giữ rồi ghi nhận khi người mua xác nhận hoặc sau 4 ngày kể từ giao thành công. Đây không phải trang chính thức của Shopee; cần đối chiếu help.shopee.vn trước khi dùng làm căn cứ.

- **Bổ sung kiểm tra ngày 2026-11-09 (bảo vệ người mua, mục 9.6):** [chính sách Money Back Guarantee của eBay](https://www.ebay.com/help/policies/ebay-money-back-guarantee-policy/ebay-money-back-guarantee-policy?id=4210) (trang chính thức), [Buyer Protection của Catawiki](https://www.catawiki.com/pages/p/buyer-protection), [Buyer Protection của Whatnot](https://help.whatnot.com/hc/en-us/articles/360061194552). Về Shopee, chỉ có nguồn thứ cấp: [hướng dẫn trả hàng hoàn tiền](https://atpsoftware.vn/huong-dan-khieu-nai-tra-hang-hoan-tien-shopee.html), [bài VTC News về mức 15 ngày](https://vtcnews.vn/bi-phan-doi-vi-chinh-sach-tra-hang-shopee-noi-kiem-soat-chat-nguoi-mua-truc-loi-ar861469.html) và [bài về người bán bị giữ tiền](https://plo.vn/nguoi-ban-hang-buc-xuc-vi-bi-giam-tien-shopee-noi-se-phan-hoi-cu-the-post782305.html). Về luật: [bài của Bộ Công Thương về Luật Bảo vệ quyền lợi người tiêu dùng 2023 và Nghị định 55/2024](https://moit.gov.vn/tin-tuc/bao-chi-voi-nguoi-dan/luat-bao-ve-quyen-loi-nguoi-tieu-dung-nam-2023-va-van-ban-huong-dan-luat-huong-toi-muc-tieu-nang-cao-trach-nhiem-bao-ve-.html). Mọi số ngày và phí chỉ để tham khảo vì từng sàn đổi chính sách thường xuyên.
**Việc còn thiếu bằng chứng thực địa:** chưa phỏng vấn người mua / bán ở Việt Nam, chưa thử luồng với nhà cung cấp thanh toán / vận chuyển cụ thể và chưa có rà soát pháp lý cho mô hình vận hành đã chọn. Khi có kết quả, cập nhật file này trước khi đánh dấu `Đã chốt` hoặc `sẵn sàng phát hành`.
