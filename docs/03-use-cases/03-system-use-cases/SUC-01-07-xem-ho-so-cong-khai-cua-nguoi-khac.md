# SUC-01-07 — Xem hồ sơ công khai của người khác

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-01-07 / BUC-01 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Khách, người dùng |
| Tác nhân phụ | Dịch vụ email/SMS; vận hành khi tài khoản bị khóa |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **xem hồ sơ công khai của người khác** trong BUC-01. Mục tiêu nghiệp vụ: người xem có thông tin đánh giá độ tin cậy mà không lộ dữ liệu nhạy cảm.

## 2. Tiền điều kiện

- Hồ sơ cần xem đang được phép công khai.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Người xem mở hồ sơ từ tin hoặc giao dịch.
2. Hệ thống lấy tên hiển thị, trạng thái xác minh và tín hiệu uy tín được phép công khai.
3. Thông tin công khai phải lấy từ bản hồ sơ được phép hiển thị, không trả dữ liệu xác minh gốc cho trình duyệt.
4. Trạng thái uy tín cần nêu số lượng giao dịch/đánh giá đủ điều kiện để người xem không hiểu nhầm điểm khi dữ liệu ít.
5. Hệ thống hiển thị thông tin cùng nguồn trạng thái.

## 4. Luồng thay thế

- Hồ sơ bị hạn chế: chỉ hiển thị phần được phép và trạng thái phù hợp.
- Người xem chưa đăng nhập: vẫn xem được hồ sơ công khai từ tin.
- Tài khoản bị hạn chế: chỉ hiển thị thông báo công khai được chính sách cho phép.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Yêu cầu dữ liệu nhạy cảm | không trả giấy tờ, SĐT, địa chỉ hoặc tài khoản ngân hàng. | TC-23 |
| Yêu cầu giấy tờ xác minh hoặc địa chỉ | Từ chối, không gửi dữ liệu nhạy cảm trong phản hồi. | Chưa có TC riêng |
| Hồ sơ không tồn tại hoặc đã ẩn | Hiển thị trạng thái không tìm thấy/phần bị hạn chế, không lộ lý do nội bộ. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Người xem có thông tin đánh giá độ tin cậy mà không lộ dữ liệu nhạy cảm.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Tài khoản bị khóa không được thực hiện hành động giao dịch mới (BR-02).
- Dữ liệu cá nhân và trạng thái xác minh chỉ công khai theo quyền (NFR-04, BR-30).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-30.

## 8. Truy vết

FR-05; BR-30; TC-23. BUC-01; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Công thức điểm uy tín và chính sách ẩn hồ sơ chưa chốt.
- Phương thức xác thực, ngưỡng tuổi và cách xử lý tài khoản trùng phải được chốt trước khi phát hành.

