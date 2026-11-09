# SUC-07-02 — Ghi nhận thanh toán tự khai

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-07-02 / BUC-07 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A]` |
| Tác nhân chính | Người thắng |
| Tác nhân phụ | Người bán; vận hành; đối tác thanh toán ở tầng B |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **ghi nhận thanh toán tự khai** trong BUC-07. Hai bên có thể đã chuyển tiền thật ngoài nền tảng; mục tiêu nghiệp vụ là không biến lời khai thành trạng thái đã thanh toán hoặc đã giải ngân.

## 2. Tiền điều kiện

- Giao dịch thử nghiệm đang chờ ghi nhận.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Hệ thống hiển thị cảnh báo rằng tiền chuyển ngoài nền tảng có thể là tiền thật nhưng hệ thống không nhận, giữ, đối soát hoặc bảo vệ khoản tiền đó.
2. Người thắng xác nhận đã đọc và tự khai chuyển khoản ngoài nền tảng.
3. Nút tự khai không được gọi là thanh toán thành công; trạng thái hiển thị đúng nguồn và chưa đối soát cho cả hai bên.
4. Hệ thống lưu lời khai, thời điểm và phiên bản cảnh báo.
5. Lưu phiên bản cảnh báo đã đồng ý để biết người thắng được thông tin gì khi chuyển ngoài nền tảng.
6. Hệ thống hiển thị trạng thái người thắng khai, chưa đối soát.

## 4. Luồng thay thế

- Người thắng có thể xem lại lời khai; người bán và vận hành thấy rõ nguồn tự khai.
- Người thắng khai nhầm: cho gửi yêu cầu sửa với lịch sử, không ghi đè lời khai cũ.
- Người bán xác nhận đã nhận tiền: chỉ ghi là lời khai thứ hai nếu không có nguồn đối soát tin cậy.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Người dùng chỉ tải trang thành công hoặc gửi lại yêu cầu | không đổi thành đã thanh toán. | TC-59, TC-60 |
| Người thắng bấm nhiều lần | Không tạo nhiều khoản tiền hoặc biến thành đã thanh toán. | Chưa có TC riêng |
| Người thắng chưa xác nhận cảnh báo | Không nhận lời khai; nội dung và cách lưu phiên bản cảnh báo cần duyệt. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Không có trạng thái đã thanh toán hoặc đã giải ngân từ lời khai.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Lời khai hoặc trang quay về không đủ xác nhận đã thanh toán (BR-22).
- Đã trả, đang giữ, đã giải ngân và đã hoàn phải được theo dõi riêng (FR-22, BR-38).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-05, BR-22; M-D2, M-D4.

## 8. Truy vết

FR-22, FR-23; BR-05, BR-22; M-D2, M-D4; TC-59, TC-60. BUC-07; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- M-D2 đã chọn giao dịch ngoài nền tảng; M-D4 và nội dung cảnh báo cần duyệt.
- Đối tác thanh toán, nguồn xác nhận và cách đối soát thiếu/thừa tiền thuộc cổng D-04.

