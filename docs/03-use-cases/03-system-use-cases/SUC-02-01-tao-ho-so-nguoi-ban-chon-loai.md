# SUC-02-01 — Tạo hồ sơ người bán, chọn loại

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-02-01 / BUC-02 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Người dùng |
| Tác nhân phụ | Vận hành; dịch vụ xác minh nếu được chọn |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **tạo hồ sơ người bán, chọn loại** trong BUC-02. Mục tiêu nghiệp vụ: có hồ sơ người bán; chưa được phát hành tin tới khi xác minh đạt.

## 2. Tiền điều kiện

- Có tài khoản và đã đồng ý điều khoản bán hàng.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Người dùng chọn mở quyền bán.
2. Hệ thống hiển thị loại cá nhân, shop, doanh nghiệp, nhà phân phối theo tầng.
3. Hệ thống liên kết hồ sơ với đúng tài khoản chịu trách nhiệm và lưu loại người bán đã chọn; chưa hiển thị huy hiệu xác minh.
4. Người dùng chọn loại và khai thông tin cơ bản.
5. Trước khi cho nộp, hệ thống hiển thị thông tin xác minh tương ứng từng loại và những loại đang mở ở tầng hiện tại.
6. Hệ thống tạo hồ sơ ở trạng thái chưa xác minh.

## 4. Luồng thay thế

- Tầng A chỉ cho cá nhân và shop nếu M-S1 được duyệt; loại khác vào hàng chờ hoặc bị từ chối rõ lý do.
- Tài khoản đã có hồ sơ bán: mở hồ sơ hiện có thay vì tạo bản thứ hai nếu P-01 được duyệt.
- Người dùng đổi ý trước khi nộp: giữ bản nháp hồ sơ, chưa mở quyền đăng tin.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Loại chưa mở hoặc tài khoản bị khóa | không tạo quyền bán. | TC-08, TC-13 |
| Tài khoản chưa đồng ý điều khoản bán | Yêu cầu SUC-01-04 trước khi tiếp tục. | Chưa có TC riêng |
| Chọn doanh nghiệp ở tầng A | Thông báo chưa mở theo M-S1; không tạo quyền bán. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Có hồ sơ người bán; chưa được phát hành tin tới khi xác minh đạt.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Chỉ hồ sơ xác minh đạt mới mở quyền bán; dữ liệu giấy tờ không công khai (BR-04, BR-30).
- Tầng A chỉ mở cá nhân và shop nếu M-S1 được PO duyệt.
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-01, BR-04; P-01; M-S1.

## 8. Truy vết

FR-03, FR-04; BR-01, BR-04; P-01; M-S1; TC-08, TC-13. BUC-02; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- M-S1, một tài khoản có nhiều hồ sơ hay đổi loại chưa chốt.
- Trường xác minh, thời hạn hiệu lực và thẩm quyền duyệt phụ thuộc quy trình xác minh được phê duyệt.

