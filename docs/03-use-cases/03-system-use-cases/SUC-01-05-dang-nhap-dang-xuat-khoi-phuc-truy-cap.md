# SUC-01-05 — Đăng nhập, đăng xuất, khôi phục truy cập

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-01-05 / BUC-01 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Khách, người dùng |
| Tác nhân phụ | Dịch vụ email/SMS; vận hành khi tài khoản bị khóa |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **đăng nhập, đăng xuất, khôi phục truy cập** trong BUC-01. Mục tiêu nghiệp vụ: phiên đăng nhập được tạo hoặc kết thúc; khôi phục không sửa lịch sử giao dịch.

## 2. Tiền điều kiện

- Tài khoản đã tồn tại.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Khách cung cấp thông tin đăng nhập.
2. Hệ thống xác thực và kiểm tra trạng thái khóa.
3. Khi tạo phiên, hệ thống xác định quyền dựa trên trạng thái hiện tại thay vì dựa trên quyền lưu trong trình duyệt cũ.
4. Hệ thống tạo phiên truy cập.
5. Luồng khôi phục phải vô hiệu thông tin truy cập cũ theo chính sách và lưu thời điểm thay đổi mà không sửa giao dịch trước đó.
6. Người dùng có thể đăng xuất để kết thúc phiên.

## 4. Luồng thay thế

- Quên thông tin đăng nhập: yêu cầu khôi phục qua kênh đã xác thực rồi đặt lại thông tin truy cập.
- Người dùng đăng xuất khỏi một thiết bị: kết thúc phiên thiết bị đó; đăng xuất mọi thiết bị là lựa chọn chính sách riêng.
- Khôi phục truy cập: gửi mã tới kênh đã xác thực và yêu cầu xác minh trước khi thay thông tin đăng nhập.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Sai thông tin hoặc tài khoản bị khóa | không mở phiên và trả thông báo phù hợp. | Chưa có TC |
| Yêu cầu khôi phục không chứng minh quyền sở hữu | Không đổi thông tin truy cập. | Chưa có TC riêng |
| Tài khoản bị khóa trong khi đang đăng nhập | Chặn thao tác giao dịch tiếp theo và hiển thị hướng liên hệ. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Phiên đăng nhập được tạo hoặc kết thúc; khôi phục không sửa lịch sử giao dịch.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Tài khoản bị khóa không được thực hiện hành động giao dịch mới (BR-02).
- Dữ liệu cá nhân và trạng thái xác minh chỉ công khai theo quyền (NFR-04, BR-30).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-02; NFR-04.

## 8. Truy vết

FR-01; BR-02; NFR-04. BUC-01; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Phương thức đăng nhập, thời hạn phiên và giới hạn thử sai chưa chốt.
- Phương thức xác thực, ngưỡng tuổi và cách xử lý tài khoản trùng phải được chốt trước khi phát hành.

