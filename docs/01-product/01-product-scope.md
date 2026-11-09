# 01 — Product Scope

## 1. Thông tin tài liệu

| Thuộc tính | Nội dung |
|---|---|
| Dự án | Nền tảng đấu giá trực tuyến tại Việt Nam — tên chính thức chưa chốt; tài liệu dùng tên tạm AuctionNoow |
| Phiên bản | 0.3 |
| Ngày cập nhật | 2026-11-07 |
| Trạng thái | Bản nháp phạm vi sản phẩm; các quyết định đã chốt được phân biệt với đề xuất và câu hỏi mở |
| Bối cảnh | Dự án cá nhân; ưu tiên tài liệu gọn và có thể triển khai theo giai đoạn |
| Mục đích | Thống nhất định hướng, ranh giới sản phẩm và đầu vào cho tài liệu Requirements |
| Thay đổi 0.3 | Thêm tham chiếu 01b (MVP hai tầng, đề xuất), ghi chú quy mô mục tiêu, câu hỏi mở 12 và dòng quyết định về kiểm soát bỏ thanh toán. Không đổi quyết định đã chốt |

**Quy ước:** “Đã chốt” là quyết định của chủ dự án; “Đề xuất” và “Giả định” chưa được phê duyệt; “Chưa chốt” cần quyết định tiếp. Phạm vi sản phẩm dài hạn không đồng nghĩa với cam kết triển khai toàn bộ trong MVP.

## 2. Tổng quan sản phẩm

Nền tảng marketplace đấu giá trực tuyến tổng hợp, lấy giao dịch giữa người dùng cá nhân (C2C) làm trọng tâm. Sản phẩm phục vụ thị trường Việt Nam trước, đồng thời cho phép cá nhân, shop, doanh nghiệp và nhà phân phối tham gia bán hàng.

**Các quyết định đã chốt:**

- Marketplace tổng hợp, không giới hạn định vị vào một thị trường ngách duy nhất.
- Việt Nam là thị trường triển khai đầu tiên; kiến trúc và mô hình miền nghiệp vụ cần cho phép mở rộng quốc tế về sau.
- Nền tảng đóng vai trò trung gian giao dịch, bao gồm chuỗi đấu giá → xác định người thắng → điều phối thanh toán → theo dõi vận chuyển → xử lý tranh chấp → uy tín; KYC khi cần.
- Hỗ trợ người bán là cá nhân, shop, doanh nghiệp và nhà phân phối. Việc hỗ trợ nhiều loại người bán không mặc định mỗi loại phải có bộ tính năng riêng trong MVP.
- **Chốt bổ sung ngày 2026-09-30:** MVP cho hàng mới, hàng cũ và đồ sưu tầm; đấu giá tăng dần thủ công có tùy chọn mua ngay, tắt mua ngay sau lượt giá hợp lệ đầu tiên. Không có giá bảo lưu hoặc tự trả giá hộ. Lượt giá hợp lệ đến trong 2 phút cuối kéo dài phiên đến 2 phút sau lượt đó; quy tắc lặp lại với các lượt hợp lệ tiếp theo.
- **Chốt bổ sung ngày 2026-09-30:** hướng thanh toán là giữ tiền người mua cho tới khi đủ điều kiện giải ngân / hoàn tiền, tương tự cơ chế bảo đảm của Shopee.

Chưa xác định chủ thể và cơ chế pháp lý giữ tiền, nhà cung cấp phù hợp, điều kiện giải ngân / hoàn tiền, hoặc nền tảng có tự vận chuyển hay không. Mục tiêu bảo đảm giao dịch chưa đồng nghĩa AuctionNoow được phép tự giữ tiền trong tài khoản của dự án.

## 3. Vấn đề cần giải quyết

Các nhận định dưới đây là **giả thuyết sản phẩm cần kiểm chứng**, chưa phải kết quả nghiên cứu thị trường:

- Người bán khó tìm được mức giá phù hợp khi giá trị món hàng phụ thuộc vào nhu cầu của nhiều người mua.
- Người mua cần thông tin hàng hóa rõ ràng, quy trình đặt giá dễ hiểu và kết quả đấu giá có thể kiểm tra.
- Giao dịch qua các kênh rời rạc có thể thiếu cơ chế theo dõi thanh toán, giao hàng và giải quyết bất đồng.
- Thiếu lịch sử giao dịch và tín hiệu uy tín khiến hai bên khó đánh giá mức độ đáng tin cậy của nhau.

Sản phẩm hướng tới kết nối quá trình khám phá giá qua đấu giá với quá trình hoàn tất giao dịch có thể theo dõi.

## 4. Tầm nhìn sản phẩm

Xây dựng một marketplace nơi người dùng tại Việt Nam có thể mua bán qua đấu giá một cách dễ hiểu, minh bạch và có hỗ trợ xuyên suốt giao dịch; tạo nền tảng để mở rộng sang thị trường khác khi đã xác thực nhu cầu và khả năng vận hành.

## 5. Người dùng mục tiêu

| Nhóm | Nhu cầu sản phẩm dự kiến |
|---|---|
| Người mua / người tham gia đấu giá | Tìm hàng, đánh giá thông tin và uy tín, đặt giá, thanh toán và theo dõi đơn |
| Người bán cá nhân | Đăng bán và quản lý giao dịch với quy trình đơn giản |
| Shop | Quản lý hoạt động bán hàng thường xuyên |
| Doanh nghiệp | Tham gia giao dịch với danh tính và thông tin tổ chức phù hợp |
| Nhà phân phối | Bán hàng với quy mô lớn hơn; nhu cầu lô hàng và nhập dữ liệu cần khảo sát |
| Người vận hành nền tảng | Quản lý nội dung, giám sát giao dịch và hỗ trợ xử lý sự cố, tranh chấp |

Các nhu cầu trong bảng là định hướng khảo sát, không phải cam kết tính năng. Tiêu chí phân biệt shop, doanh nghiệp và nhà phân phối, quyền hạn và yêu cầu xác minh của từng nhóm chưa chốt. Một người dùng có thể vừa mua vừa bán là **giả định cần xác nhận**.

## 6. Giá trị mang lại

- **Cho người mua:** tiếp cận nhiều loại hàng hóa, tham gia cơ chế định giá rõ ràng và theo dõi giao dịch sau khi thắng.
- **Cho người bán:** tiếp cận người mua có nhu cầu và khám phá mức giá thông qua cạnh tranh đặt giá.
- **Cho cả hai bên:** có lịch sử giao dịch, tín hiệu uy tín và một đầu mối hỗ trợ khi phát sinh vấn đề.

Các giá trị này là mục tiêu thiết kế; mức độ đạt được cần đo bằng sử dụng thực tế.

## 7. Mục tiêu

1. Kiểm chứng nhu cầu mua bán qua đấu giá tại Việt Nam.
2. Xây dựng quy trình đấu giá có kết quả nhất quán, truy vết được.
3. Kiểm chứng khả năng chuyển một phiên đấu giá thành giao dịch hoàn tất.
4. Tạo cơ chế tin cậy cơ bản phù hợp với khả năng vận hành của dự án cá nhân.
5. Giữ mô hình sản phẩm đủ linh hoạt cho nhiều loại người bán và thị trường tương lai, đồng thời kiểm soát độ phức tạp ban đầu.

## 8. Tiêu chí thành công

**Bộ chỉ số đề xuất; chưa chốt ngưỡng mục tiêu, quy mô thử nghiệm hay thời gian đánh giá.**

| Khía cạnh | Chỉ số / bằng chứng đề xuất |
|---|---|
| Nhu cầu | Số người mua và người bán hoạt động; tỷ lệ quay lại trong kỳ đo đã thống nhất |
| Thanh khoản | Tỷ lệ phiên đã kết thúc có ít nhất một lượt đặt giá hợp lệ |
| Chuyển đổi | Tỷ lệ phiên có người thắng dẫn đến thanh toán thành công |
| Hoàn tất | Tỷ lệ giao dịch đã thanh toán được xác nhận hoàn tất |
| Tin cậy | Tỷ lệ tranh chấp, tỷ lệ bỏ thanh toán và thời gian xử lý tranh chấp |
| Tính đúng đắn | Kết quả xác định người thắng khớp quy tắc đã công bố, kể cả khi nhiều lượt đặt giá đến gần nhau |
| Khả năng vận hành | Thời gian hỗ trợ thủ công và chi phí trung bình trên một giao dịch |

Định nghĩa “hoạt động”, “hợp lệ”, “hoàn tất”, mẫu số, kỳ đo và tiêu chí đạt để phát hành cần được chốt trong Requirements và kế hoạch thử nghiệm.

## 9. Phạm vi sản phẩm

### 9.1. Phạm vi dài hạn đã chốt ở cấp năng lực

- Đăng và khám phá hàng hóa trong marketplace tổng hợp.
- Tổ chức đấu giá, nhận lượt đặt giá và xác định người thắng.
- Điều phối thanh toán sau đấu giá.
- Theo dõi vận chuyển và trạng thái giao dịch.
- Tiếp nhận, xử lý tranh chấp và xây dựng uy tín giao dịch.
- Xác minh danh tính (KYC) khi cần; điều kiện kích hoạt chưa chốt.
- Phục vụ bốn nhóm người bán đã xác định.
- Cho phép mở rộng quốc tế ở cấp kiến trúc và mô hình miền nghiệp vụ.

### 9.2. Phạm vi MVP đề xuất — chưa phê duyệt

Một lát cắt giao dịch từ đầu đến cuối có thể gồm:

- Tài khoản, hồ sơ người dùng và thông tin loại người bán ở mức cơ bản.
- Đăng hàng, xem chi tiết, tìm kiếm / lọc cơ bản và kiểm duyệt nội dung tối thiểu.
- Đấu giá tăng dần thủ công có tùy chọn mua ngay; nhận đặt giá, gia hạn 2 phút cuối, đóng phiên và xác định người thắng. Mua ngay tắt sau lượt đặt giá hợp lệ đầu tiên; không dùng giá bảo lưu hay tự trả giá hộ.
- Tạo giao dịch sau khi thắng hoặc mua ngay; ghi nhận riêng thanh toán, tiền đang giữ, giải ngân / hoàn tiền và giao hàng.
- Tiếp nhận tranh chấp, xử lý với hỗ trợ thủ công và ghi nhận đánh giá sau giao dịch.
- Công cụ vận hành tối thiểu và nhật ký các sự kiện quan trọng.

Nhà cung cấp và cách triển khai hợp lệ cơ chế giữ tiền, vận chuyển, xác minh và mức tự động hóa còn mở. Nếu chỉ thử nghiệm một phần chuỗi giao dịch, cần ghi rõ giới hạn thử nghiệm trước khi phát hành. Danh mục khởi động có thể được thu hẹp để thử nghiệm mà vẫn giữ định vị marketplace tổng hợp.

**Cập nhật 2026-11-09 (PO chọn chia tầng):** tầng A thử nghiệm kín với người và hàng thật; hai bên có thể tự thanh toán, giao hàng ngoài nền tảng. Hệ thống chỉ ghi lời khai, không nhận, giữ, đối soát hoặc bảo vệ tiền và không coi lời khai là `đã thanh toán`. Tầng B xử lý tiền thật qua đối tác thanh toán bảo đảm, chỉ mở khi đạt cổng đối tác và pháp lý. Chi tiết, tiêu chí vào / ra và kịch bản kiểm thử ở [01b-mvp-scope.md](01b-mvp-scope.md). Việc chia tầng không đổi mục tiêu giữ tiền đã chốt ở mục 2; nó thay đổi thứ tự triển khai.

### 9.3. Chưa cam kết cho MVP

- Giao dịch xuyên biên giới, đa tiền tệ và vận chuyển quốc tế.
- Ứng dụng di động riêng, API đối tác và nhập danh mục hàng loạt.
- Bộ công cụ chuyên biệt cho doanh nghiệp / nhà phân phối, nhiều nhân viên quản lý shop.
- Nhiều hình thức đấu giá nâng cao, gợi ý cá nhân hóa và chống gian lận nâng cao.
- Ví nội bộ hoặc tự xây mạng lưới giao nhận. Cơ chế giữ / giải ngân tiền là mục tiêu MVP nhưng cách thực hiện phải được chốt riêng.

Danh sách này là đề xuất trì hoãn, không phải quyết định loại bỏ vĩnh viễn.

## 10. Mô hình kinh doanh cấp cao

**Chưa chốt cách thu phí.** Các phương án cần đánh giá gồm phí trên giao dịch thành công, phí đăng tin / hiển thị nổi bật và gói công cụ dành cho người bán thường xuyên.

Cần xác định bên chịu phí, thời điểm thu, cơ sở tính phí, hoàn phí khi giao dịch thất bại và tác động tới khả năng thu hút người dùng. Mục tiêu bảo đảm tiền đã được chốt, nhưng cơ chế và chủ thể được phép giữ tiền vẫn phải xác minh; điều đó không tự động chốt cách thu phí.

Các nhóm chi phí dự kiến gồm hạ tầng, thanh toán, xác minh, thông báo, hỗ trợ và xử lý tranh chấp. Chưa có ngân sách hoặc giả định doanh thu được phê duyệt.

## 11. Luồng giao dịch cấp cao

1. Người bán tạo hồ sơ; xác minh nếu thuộc trường hợp cần xác minh.
2. Người bán đăng hàng và thiết lập phiên đấu giá theo quy tắc của nền tảng.
3. Nội dung được xử lý theo cơ chế kiểm duyệt sẽ chốt sau; phiên đủ điều kiện được mở.
4. Người mua xem thông tin và gửi lượt đặt giá; nền tảng kiểm tra điều kiện hợp lệ.
5. Phiên kết thúc; nền tảng xác định có người thắng hay không theo quy tắc công bố.
6. Nếu có người thắng, nền tảng khởi tạo giao dịch và điều phối thanh toán.
7. Người bán bàn giao hàng; nền tảng theo dõi trạng thái vận chuyển.
8. Giao dịch được xác nhận hoàn tất hoặc chuyển sang xử lý vấn đề / tranh chấp.
9. Tiền được giải ngân hoặc hoàn theo điều kiện sẽ chốt; các bên đánh giá giao dịch theo chính sách uy tín.

Các nhánh không có người thắng, người thắng không thanh toán, người bán không giao, hàng không đúng mô tả, hủy giao dịch và hoàn tiền cần được đặc tả riêng. Thứ tự chi trả và điều kiện hoàn tất chưa được quyết định.

## 12. Ràng buộc

- **Đã chốt:** ưu tiên thị trường Việt Nam; duy trì khả năng mở rộng quốc tế về sau.
- **Bối cảnh dự án:** dự án cá nhân, cần cân đối phạm vi với thời gian, ngân sách và năng lực hỗ trợ thực tế; chưa có hạn mức hoặc lịch phát hành.
- **Quy mô mục tiêu dài hạn (PO nêu 2026-11-07):** phục vụ người dùng trên phạm vi cả nước. Đây là định hướng, chưa phải chỉ tiêu tải; MVP kiểm chứng ở quy mô nhỏ và các chỉ tiêu tải cụ thể được chốt ở D-07 / file 05.
- **Yêu cầu thiết kế đề xuất:** tránh gắn cứng quốc gia, ngôn ngữ, tiền tệ, múi giờ và cấu trúc địa chỉ vào mô hình nghiệp vụ; chưa yêu cầu triển khai đa quốc gia ngay.
- **Ràng buộc cần xác minh trước vận hành thực tế:** yêu cầu áp dụng đối với mô hình marketplace / đấu giá, dữ liệu cá nhân, hàng hóa, thanh toán, thuế và bảo vệ người tiêu dùng. Tài liệu này chưa xác lập nghĩa vụ pháp lý cụ thể.
- Chưa chốt công nghệ, nhà cung cấp, quy mô tải hoặc cam kết chất lượng dịch vụ.

## 13. Giả định cần xác nhận

- Giao diện ban đầu ưu tiên tiếng Việt và giao dịch bằng VND.
- Giai đoạn đầu tập trung hàng hóa vật lý; chưa xác định có hỗ trợ hàng số hoặc dịch vụ.
- Một tài khoản có thể đảm nhiệm cả vai trò mua và bán.
- Có thể dùng nhà cung cấp bên ngoài cho thanh toán, vận chuyển và KYC.
- Một phần kiểm duyệt và hỗ trợ tranh chấp có thể được xử lý thủ công trong thử nghiệm.

**Đã chốt phạm vi tình trạng hàng:** hàng mới, hàng cũ và đồ sưu tầm đều có thể tham gia MVP. Danh mục cụ thể, hàng cấm / hạn chế và điều kiện xác thực đồ sưu tầm vẫn chưa chốt.

## 14. Rủi ro chính

| Rủi ro | Hướng xử lý đề xuất |
|---|---|
| Ít người mua hoặc ít hàng, khó tạo cạnh tranh đặt giá | Thử nghiệm với quy mô có kiểm soát và đo thanh khoản trước khi mở rộng |
| Đặt giá ảo, thông đồng, tài khoản giả hoặc bỏ thanh toán | Chốt điều kiện tham gia, lưu vết và cơ chế xử lý vi phạm |
| Hàng cấm, giả mạo hoặc mô tả sai | Xây chính sách hàng hóa, kiểm duyệt và tiếp nhận báo cáo |
| Kết quả sai khi đặt giá đồng thời hoặc sát giờ kết thúc | Chốt quy tắc thời gian và bảo đảm xử lý lượt đặt giá nhất quán |
| Mất tiền, thất lạc hàng hoặc tranh chấp kéo dài | Xác định trách nhiệm, bằng chứng, thời hạn và cơ chế hoàn tiền / chi trả |
| Phạm vi quá rộng đối với dự án cá nhân | Chốt một lát cắt MVP và trì hoãn tính năng chưa cần thiết |
| Lộ dữ liệu cá nhân hoặc dữ liệu xác minh | Giảm dữ liệu thu thập, kiểm soát truy cập và chốt thời hạn lưu giữ |
| Mô hình vận hành không phù hợp yêu cầu áp dụng | Rà soát pháp lý và điều kiện nhà cung cấp trước thử nghiệm có giao dịch thật |

## 15. Phụ thuộc bên ngoài

- Nhà cung cấp thanh toán / ngân hàng: khả năng tích hợp, đối soát, chi trả, hoàn tiền và điều kiện sử dụng.
- Đơn vị vận chuyển: tạo / ghi nhận vận đơn, truy xuất trạng thái và xử lý thất lạc.
- Dịch vụ xác minh danh tính nếu lựa chọn thuê ngoài.
- Dịch vụ email / SMS / thông báo nếu cần cho xác thực và cập nhật giao dịch.
- Hạ tầng lưu trữ, giám sát và sao lưu.
- Nguồn tư vấn hoặc rà soát yêu cầu pháp lý phù hợp mô hình thực tế.

Chưa chọn nhà cung cấp; không mặc định mọi tích hợp đều bắt buộc trong MVP.

## 16. Câu hỏi mở

1. Danh mục hàng ban đầu và danh mục bị cấm / hạn chế là gì? Đồ sưu tầm cần bằng chứng xác thực nào?
2. MVP bao phủ đến bước nào của chuỗi giao dịch? Phần nào tích hợp, phần nào vận hành thủ công?
3. Với đấu giá tăng dần, mua ngay và gia hạn 2 phút đã chốt, bước giá, thời lượng phiên ban đầu, rút lượt đặt giá, giữ chỗ mua ngay và hủy phiên hoạt động ra sao?
4. Ai đủ điều kiện đặt giá / bán hàng? Có đặt cọc hoặc giới hạn tham gia không?
5. Phân loại người bán dựa trên tiêu chí nào? Khi nào cần xác minh, xác minh thông tin gì?
6. Chủ thể nào được phép nhận và giữ tiền trong cơ chế bảo đảm? Khi nào giải ngân, hoàn tiền và xử lý người thắng không thanh toán?
7. Ai chọn đơn vị vận chuyển, trả phí và chịu trách nhiệm khi giao thất bại hoặc hàng bị hỏng?
8. Điều kiện hoàn tất, mở tranh chấp, bằng chứng và thẩm quyền xử lý là gì?
9. Ai được đánh giá ai, vào thời điểm nào và cách hạn chế thao túng uy tín?
10. Thu phí theo mô hình nào? Mục tiêu sử dụng, ngân sách và lịch thử nghiệm là gì?
11. Mô hình vận hành cụ thể phải đáp ứng yêu cầu pháp lý nào trước khi mở giao dịch thật?
12. Chống người thắng bỏ thanh toán: PO đã chọn hướng tiền đặt trước theo cơ chế Điều 39 (2026-11-09). Còn mở: tỷ lệ, thời điểm thu, người nhận khoản bị mất, hạn trả, mời người đặt giá kế tiếp, tính hợp pháp. (xem D-08 và mục 9.5 của file 02)
13. Bảo vệ người mua: PO chọn hướng giống Shopee, cửa sổ 15 ngày (2026-11-09). Còn mở: hàng giả phát hiện muộn, thu hồi tiền hoàn từ người bán, bỏ lý do "đổi ý". (xem D-09 và mục 9.6 của file 02)

## 17. Các quyết định tiếp theo

| Thời điểm | Quyết định cần chốt | Đầu ra dự kiến |
|---|---|---|
| Trước khi chốt MVP | Hàng hóa, nhóm người dùng ưu tiên, luồng giao dịch tối thiểu và giới hạn thử nghiệm | Danh sách trong / ngoài MVP được phê duyệt |
| Trước khi chốt quy tắc thanh toán | Thông số tiền đặt trước (hướng đã chọn), hạn trả, mời người đặt giá kế tiếp, chế tài | Chốt các điểm còn mở của D-08 trong file 02 |
| Khi viết Requirements | Quy tắc đấu giá, điều kiện tham gia, thanh toán, giao hàng, tranh chấp, uy tín và xác minh | Yêu cầu chức năng, quy tắc nghiệp vụ và tiêu chí nghiệm thu |
| Trước thiết kế hệ thống | Quy mô dự kiến, yêu cầu tính đúng đắn, bảo mật, lưu vết, tích hợp và khả năng mở rộng quốc tế | Ràng buộc thiết kế và mô hình miền nghiệp vụ |
| Trước thử nghiệm giao dịch thật | Rà soát yêu cầu áp dụng, nhà cung cấp, chính sách vận hành, hỗ trợ và chỉ số mục tiêu | Điều kiện sẵn sàng thử nghiệm |
| Sau khi có dữ liệu sử dụng | Mở rộng danh mục, công cụ người bán, tự động hóa và thị trường quốc tế | Lộ trình cập nhật dựa trên bằng chứng |

Các quyết định mới cần được cập nhật vào tài liệu này để tránh biến giả định thành yêu cầu mặc định.
