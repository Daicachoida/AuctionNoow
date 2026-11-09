# SUC-05-06 — Thông báo bị vượt giá và kết quả phiên

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-05-06 / BUC-05 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Hệ thống |
| Tác nhân phụ | Người bán; vận hành; đối tác thanh toán ở tầng B |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **thông báo bị vượt giá và kết quả phiên** trong BUC-05. Mục tiêu nghiệp vụ: người tham gia có đường tra cứu kết quả bất kể thông báo.

## 2. Tiền điều kiện

- Có thay đổi giá dẫn đầu hoặc kết quả phiên.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Hệ thống xác định người bị vượt giá hoặc các bên nhận kết quả.
2. Hệ thống tạo thông báo từ sự kiện chính thức.
3. Thông báo bị vượt giá phát sinh sau khi lượt mới được ghi bền vững, không từ yêu cầu chưa được chấp nhận.
4. Hệ thống gửi qua kênh đã cấu hình.
5. Thông báo kết quả phải trỏ đến bản ghi kết quả chính thức và trạng thái giao dịch, tránh gây hiểu rằng đã thanh toán.
6. Người nhận mở trang phiên để xem trạng thái hiện hành.

## 4. Luồng thay thế

- Gửi thất bại: thử lại theo chính sách, trạng thái phiên vẫn theo bản ghi chính thức.
- Người dùng tắt một kênh thông báo: vẫn xem được trạng thái trong ứng dụng.
- Thông báo gửi trùng: hiển thị cùng sự kiện, không tạo thay đổi nghiệp vụ.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Thông báo đến muộn | không thay đổi giá, giờ đóng hay người thắng. | TC-37, TC-42, TC-43 |
| Thông báo vượt giá đến sau phiên đóng | Trang đích hiển thị kết quả mới nhất. | Chưa có TC riêng |
| Dịch vụ gửi lỗi | Ghi lỗi và thử lại; không đảo lượt giá hoặc kết quả. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Người tham gia có đường tra cứu kết quả bất kể thông báo.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Chỉ lượt giá đã được ghi bền vững mới làm đổi người dẫn đầu (BR-14).
- Giờ máy chủ và thứ tự ghi nhận chính thức phân xử cạnh tranh giá/mua ngay (BR-12, BR-15, BR-36).
- Mã quy tắc/đề xuất liên quan trực tiếp: NFR-05.

## 8. Truy vết

FR-16, FR-21; NFR-05; TC-37, TC-42, TC-43. BUC-05; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Kênh, thời hạn và tần suất thông báo chưa chốt.
- Bước giá, giữ chỗ mua ngay và tiền đặt trước chỉ là tham số đề xuất; phải cập nhật TC khi PO chốt.

