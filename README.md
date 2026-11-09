# AuctionNoow

Nền tảng đấu giá trực tuyến cho thị trường Việt Nam (tên tạm AuctionNoow). Mục tiêu dài hạn là một marketplace đấu giá nhiều loại hàng hóa cho người dùng trên cả nước.

> **Trạng thái: đang ở giai đoạn tài liệu và thiết kế MVP. Repo chưa có mã nguồn.**
> Nhiều quy tắc trong tài liệu còn ở dạng đề xuất, chờ chủ sản phẩm duyệt. Phần pháp lý (đấu giá tài sản, giữ tiền hộ) chưa có kết luận.

## Tài liệu

| File | Nội dung |
|---|---|
| [01-product-scope.md](docs/01-product/01-product-scope.md) | Tầm nhìn, đối tượng, phạm vi, ranh giới sản phẩm, rủi ro, câu hỏi mở |
| [01b-mvp-scope.md](docs/01-product/01b-mvp-scope.md) | Định nghĩa MVP chi tiết: tầng A giao dịch ngoài nền tảng, tầng B thanh toán bảo đảm, luồng và kịch bản kiểm thử |
| [02-requirements-business-rules.md](docs/02-requirements/02-requirements-business-rules.md) | Yêu cầu chức năng (FR), quy tắc nghiệp vụ (BR), quyết định cần chốt (D), tham số đề xuất (P), nguồn tham khảo |
| [03-use-cases-user-flows.md](docs/03-use-cases/03-use-cases-user-flows.md) | Mục lục Business Use Case và System Use Case |
| [Sơ đồ System Use Case](docs/03-use-cases/03-system-use-cases/system-use-case-overview.svg) | Ảnh tổng quan; [bốn sơ đồ chi tiết](docs/03-use-cases/03-system-use-cases/system-use-case-overview.md) theo nhóm nghiệp vụ |

Đọc theo thứ tự 01, 01b, 02. Các mã `FR`, `BR`, `P`, `D`, `TC` dùng để truy vết giữa các file.

## Các quy tắc lõi (đã chốt)

- Đấu giá tăng dần, đặt giá thủ công. Không có giá bảo lưu hay tự trả giá hộ.
- Có mua ngay, chỉ hiển thị trước lượt giá hợp lệ đầu tiên.
- Gia hạn mềm: lượt giá hợp lệ trong 2 phút cuối kéo giờ đóng thành thời điểm lượt đó cộng 2 phút. Thời điểm máy chủ là chuẩn duy nhất.
- Đóng phiên chỉ xác định một người thắng, chạy lặp không tạo thêm kết quả.
- Mục tiêu giữ tiền đến khi đủ điều kiện giải ngân qua đối tác. Dự án không tự giữ tiền người dùng.

## Hướng đang chọn (chưa chốt thông số)

- MVP chia hai tầng: **tầng A** thử nghiệm kín với người và hàng thật; hai bên có thể tự thanh toán, giao hàng ngoài nền tảng, nhưng hệ thống không nhận, giữ, đối soát hoặc bảo vệ tiền. **Tầng B** xử lý tiền thật qua đối tác thanh toán bảo đảm, chỉ mở khi có đối tác và đã rà pháp lý.
- Chống người thắng bỏ thanh toán bằng **tiền đặt trước theo hướng Điều 39 Luật Đấu giá tài sản**, áp dụng ở tầng B. Tỷ lệ, thời điểm thu và người nhận khoản bị mất còn mở.
- Bảo vệ người mua theo hướng **Shopee**: 15 ngày để yêu cầu trả hàng / hoàn tiền, nền tảng đứng giữa xử lý, không có lý do "đổi ý". Hàng giả phát hiện muộn và cách thu hồi tiền hoàn từ người bán còn mở.

## Việc tiếp theo

1. Chốt các điểm còn mở của D-08 và duyệt các quyết định ở mục 2 của `01b`.
2. Rà soát pháp lý: sàn có bị coi là đấu giá tài sản không, giữ tiền cần giấy phép gì.
3. Hoàn thiện thiết kế hệ thống, yêu cầu phi chức năng và kế hoạch kiểm thử; use case đã có ở tài liệu 03.
4. Làm lõi đấu giá trước (đặt giá đồng thời, gia hạn, đóng phiên) khi bắt đầu code.

## Bản quyền

Chưa chọn license. Mọi quyền được bảo lưu; người khác có thể xem trên GitHub nhưng không được sao chép hay dùng lại khi chưa có phép.
