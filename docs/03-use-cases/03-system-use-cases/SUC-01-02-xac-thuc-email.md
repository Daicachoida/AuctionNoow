# SUC-01-02 — Xác thực email

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-01-02 / BUC-01 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Người dùng |
| Tác nhân phụ | Dịch vụ email/SMS; vận hành khi tài khoản bị khóa |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **xác thực email** trong BUC-01. Mục tiêu nghiệp vụ: email được xác thực; quyền đặt giá chỉ mở khi SĐT và điều khoản cũng hợp lệ.

## 2. Tiền điều kiện

- Có tài khoản và email chưa xác thực hoặc đã đổi.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Người dùng yêu cầu xác thực email.
2. Hệ thống gửi mã hoặc liên kết tới địa chỉ đang chờ xác thực.
3. Mã xác thực phải gắn với đúng tài khoản, email và mục đích xác thực; mã cũ mất hiệu lực khi địa chỉ đổi hoặc mã mới được phát hành.
4. Người dùng nhập mã hoặc mở liên kết.
5. Sau khi xác thực, hệ thống kiểm tra lại toàn bộ điều kiện đặt giá: tài khoản không bị khóa, SĐT đã xác thực và điều khoản hiện hành đã được đồng ý.
6. Hệ thống kiểm tra hiệu lực và đánh dấu email đã xác thực.

## 4. Luồng thay thế

- Đổi email: địa chỉ mới trở về trạng thái chưa xác thực.
- Người dùng yêu cầu gửi lại mã: giữ trạng thái chưa xác thực, vô hiệu mã cũ và áp dụng giới hạn gửi lại.
- Email đã xác thực: mở trang trạng thái mà không tạo lần xác thực hoặc quyền đặt giá mới.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Mã sai hoặc hết hạn | từ chối và cho yêu cầu gửi lại. | TC-01, TC-03 |
| Mã thuộc tài khoản hoặc email khác | Từ chối, ghi nhận lần thử và không thay đổi trạng thái. | Chưa có TC riêng |
| Dịch vụ gửi thư không phản hồi | Cho thử lại sau, hiển thị trạng thái chưa xác thực; không suy đoán đã gửi thành công. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Email được xác thực; quyền đặt giá chỉ mở khi SĐT và điều khoản cũng hợp lệ.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Tài khoản bị khóa không được thực hiện hành động giao dịch mới (BR-02).
- Dữ liệu cá nhân và trạng thái xác minh chỉ công khai theo quyền (NFR-04, BR-30).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-11; P-01.

## 8. Truy vết

FR-01; BR-11; P-01; TC-01, TC-03. BUC-01; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Thời hạn mã, số lần thử và nhà cung cấp email chưa chốt.
- Phương thức xác thực, ngưỡng tuổi và cách xử lý tài khoản trùng phải được chốt trước khi phát hành.

