# SUC-01-03 — Xác thực số điện thoại

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-01-03 / BUC-01 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Người dùng |
| Tác nhân phụ | Dịch vụ email/SMS; vận hành khi tài khoản bị khóa |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **xác thực số điện thoại** trong BUC-01. Mục tiêu nghiệp vụ: sĐT được xác thực; không tự mở quyền bán.

## 2. Tiền điều kiện

- Có tài khoản và SĐT chưa xác thực hoặc đã đổi.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Người dùng yêu cầu xác thực SĐT.
2. Hệ thống gửi mã tới SĐT đang chờ xác thực.
3. Mã SMS phải gắn với đúng tài khoản, số điện thoại và mục đích; xác minh số mới không sửa lịch sử giao dịch cũ.
4. Người dùng nhập mã.
5. Sau xác thực, hệ thống đánh giá lại quyền đặt giá và chỉ mở nếu email, điều khoản và trạng thái tài khoản cũng hợp lệ.
6. Hệ thống kiểm tra và đánh dấu SĐT đã xác thực.

## 4. Luồng thay thế

- Đổi SĐT: quyền đặt giá tạm khóa tới khi xác thực số mới.
- Gửi lại mã: mã cũ hết hiệu lực, hiển thị thời điểm có thể yêu cầu tiếp theo.
- Người dùng đã xác thực số này: trả trạng thái hiện tại, không tạo thêm bản ghi xác minh.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Mã sai, hết hạn hoặc SMS lỗi | giữ trạng thái chưa xác thực và cho thử lại theo giới hạn. | TC-02, TC-03 |
| Mã dùng cho số cũ | Từ chối và giữ số mới ở trạng thái chưa xác thực. | Chưa có TC riêng |
| Dịch vụ SMS lỗi hoặc quá giới hạn gửi | Thông báo thời điểm thử lại; chưa mở quyền đặt giá. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** SĐT được xác thực; không tự mở quyền bán.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Tài khoản bị khóa không được thực hiện hành động giao dịch mới (BR-02).
- Dữ liệu cá nhân và trạng thái xác minh chỉ công khai theo quyền (NFR-04, BR-30).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-11; P-01.

## 8. Truy vết

FR-01; BR-11; P-01; TC-02, TC-03. BUC-01; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Thời hạn mã, giới hạn gửi lại và xử lý SĐT trùng chưa chốt.
- Phương thức xác thực, ngưỡng tuổi và cách xử lý tài khoản trùng phải được chốt trước khi phát hành.

