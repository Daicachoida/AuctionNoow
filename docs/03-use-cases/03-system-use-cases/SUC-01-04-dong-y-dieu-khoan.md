# SUC-01-04 — Đồng ý điều khoản

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-01-04 / BUC-01 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Khách, người dùng |
| Tác nhân phụ | Dịch vụ email/SMS; vận hành khi tài khoản bị khóa |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **đồng ý điều khoản** trong BUC-01. Mục tiêu nghiệp vụ: có bản ghi đồng ý có thể truy vết.

## 2. Tiền điều kiện

- Có phiên bản điều khoản hiện hành.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Hệ thống hiển thị nội dung và phiên bản áp dụng.
2. Người dùng xác nhận đã đọc và đồng ý.
3. Trước khi lưu, hệ thống kiểm tra phiên bản điều khoản người dùng vừa xem còn là phiên bản hiện hành.
4. Hệ thống lưu tài khoản, phiên bản, thời điểm và phạm vi đồng ý.
5. Bản ghi đồng ý cần phân biệt điều khoản chung, quy tắc đặt giá và cảnh báo tầng A nếu áp dụng; không thay thế đồng ý cũ trong lịch sử.
6. Hệ thống cho tiếp tục thao tác đủ điều kiện.

## 4. Luồng thay thế

- Khi điều khoản đổi phiên bản, yêu cầu đồng ý lại trước đăng bán hoặc đặt giá.
- Điều khoản đổi trong lúc người dùng đang đọc: hiển thị phiên bản mới và yêu cầu xác nhận lại.
- Khách xem tin công khai: chưa cần đồng ý nếu không thực hiện hành động giao dịch.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Từ chối hoặc chưa xác nhận | chặn thao tác cần điều khoản. | TC-04 |
| Phiên bản được xác nhận đã cũ | Không nhận bản đồng ý cho hành động mới. | Chưa có TC riêng |
| Thiếu dấu xác nhận chủ động | Không coi việc tiếp tục duyệt trang là đồng ý. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Có bản ghi đồng ý có thể truy vết.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Tài khoản bị khóa không được thực hiện hành động giao dịch mới (BR-02).
- Dữ liệu cá nhân và trạng thái xác minh chỉ công khai theo quyền (NFR-04, BR-30).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-05.

## 8. Truy vết

FR-01; BR-05; TC-04. BUC-01; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Thời điểm bắt buộc đồng ý khi đăng ký hay trước giao dịch cần PO xác nhận.
- Phương thức xác thực, ngưỡng tuổi và cách xử lý tài khoản trùng phải được chốt trước khi phát hành.

