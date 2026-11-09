# SUC-01-06 — Xem và sửa hồ sơ cá nhân

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-01-06 / BUC-01 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Người dùng |
| Tác nhân phụ | Dịch vụ email/SMS; vận hành khi tài khoản bị khóa |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **xem và sửa hồ sơ cá nhân** trong BUC-01. Mục tiêu nghiệp vụ: hồ sơ mới có hiệu lực; danh tính trong giao dịch cũ không bị ghi đè.

## 2. Tiền điều kiện

- Người dùng đã đăng nhập.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Người dùng mở hồ sơ.
2. Hệ thống hiển thị trường được phép xem và sửa.
3. Các thay đổi về tên hiển thị, email, SĐT và địa chỉ cần được phân biệt; trường định danh ảnh hưởng xác minh phải qua quy trình tương ứng.
4. Người dùng gửi thay đổi.
5. Giao dịch đã tạo vẫn tham chiếu thông tin và phiên bản điều kiện tại thời điểm tạo; trang hồ sơ hiện bản mới.
6. Hệ thống kiểm tra, lưu phiên bản mới và ghi nhật ký khi thay đổi trọng yếu.

## 4. Luồng thay thế

- Đổi email hoặc SĐT: chuyển trường đó sang chưa xác thực theo SUC-01-02 hoặc SUC-01-03.
- Người dùng hủy thao tác trước khi lưu: hồ sơ giữ nguyên.
- Sửa email hoặc SĐT: chỉ trường mới chuyển chưa xác thực, không xóa bằng chứng xác thực cũ.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Dữ liệu không hợp lệ hoặc không thuộc quyền sửa | từ chối và giữ bản cũ. | Chưa có TC |
| Tên hiển thị vi phạm chính sách | Từ chối và nêu trường cần sửa. | Chưa có TC riêng |
| Hai yêu cầu sửa đồng thời | Chỉ lưu phiên bản hợp lệ theo thứ tự chính thức, không ghi đè im lặng. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Hồ sơ mới có hiệu lực; danh tính trong giao dịch cũ không bị ghi đè.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Tài khoản bị khóa không được thực hiện hành động giao dịch mới (BR-02).
- Dữ liệu cá nhân và trạng thái xác minh chỉ công khai theo quyền (NFR-04, BR-30).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-30; NFR-03, NFR-04.

## 8. Truy vết

FR-02; BR-30; NFR-03, NFR-04. BUC-01; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Danh sách trường sửa được và trường phải xác minh lại chưa chốt.
- Phương thức xác thực, ngưỡng tuổi và cách xử lý tài khoản trùng phải được chốt trước khi phát hành.

