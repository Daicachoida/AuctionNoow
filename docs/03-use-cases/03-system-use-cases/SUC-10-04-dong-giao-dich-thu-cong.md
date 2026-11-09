# SUC-10-04 — Đóng giao dịch thủ công

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-10-04 / BUC-10 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A]` |
| Tác nhân chính | Vận hành |
| Tác nhân phụ | Người mua, người bán; đối tác thanh toán ở tầng B |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **đóng giao dịch thủ công** trong BUC-10. Mục tiêu nghiệp vụ: giao dịch tầng A đóng để đánh giá; hai bên có thể đã chuyển tiền thật bên ngoài nhưng hệ thống không xác nhận hoặc chuyển tiền.

## 2. Tiền điều kiện

- Giao dịch thử nghiệm đã có bằng chứng giao và không còn vụ việc mở.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Vận hành xem lời khai giao hàng, bằng chứng và phản hồi hai bên.
2. Vận hành xác nhận đủ điều kiện đóng thử nghiệm theo tiêu chí được duyệt.
3. Vận hành phải ghi rõ nguồn bằng chứng: vận đơn, người mua xác nhận, ảnh giao hoặc đối chiếu hai bên.
4. Hệ thống ghi hoàn tất thử nghiệm, người quyết định, lý do và thời điểm.
5. Trạng thái hoàn tất thử nghiệm tách với hoàn tất tài chính; không tạo lệnh giải ngân/hoàn.
6. Hai bên được thông báo và có thể đánh giá.

## 4. Luồng thay thế

- Nếu có tranh chấp hoặc bằng chứng chưa đủ, giữ giao dịch chờ xem xét.
- Người mua xác nhận nhận hàng: là bằng chứng để vận hành xét, không tự đóng giao dịch.
- Người bán khai đã giao nhưng người mua phản đối: mở BUC-11 trước khi đóng.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Không có nguồn xác minh thanh toán | Không biến lời tự khai thành `đã thanh toán` hoặc giải ngân. | TC-59, TC-110 |
| Thiếu bằng chứng giao đáng tin | Giữ đang xét, không mở đánh giá. | TC-111 |
| Tranh chấp đang mở hoặc hai bên bất đồng | Từ chối đóng thử nghiệm. | TC-112 |
| Thao tác đóng bị gửi lặp | Không tạo thêm kết quả. | TC-113 |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Giao dịch tầng A đóng để đánh giá, không có xác nhận hoặc chuyển tiền qua hệ thống.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Tranh chấp đang mở chặn đóng giao dịch thử nghiệm; tầng A không có lệnh giải ngân hoặc hoàn từ hệ thống.
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-25, BR-27, BR-28.

## 8. Truy vết

FR-29, FR-36; BR-25, BR-27, BR-28; BUC-10; TC-59, TC-72, TC-110 đến TC-113.

## 9. Điểm còn mở

- Tiêu chí bằng chứng giao hàng đủ tin cậy để vận hành đóng thử nghiệm cần được duyệt trước khi mở tầng A.
- Quyền ra lệnh hoàn/giải ngân, ranh giới với tranh chấp và xử lý sau giải ngân thuộc D-04/D-09.

