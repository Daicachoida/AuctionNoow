# SUC-03-01 — Tạo bản nháp tin

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-03-01 / BUC-03 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Người bán |
| Tác nhân phụ | Vận hành; người mua chịu ảnh hưởng |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **tạo bản nháp tin** trong BUC-03. Mục tiêu nghiệp vụ: có bản nháp gắn đúng người bán và một lô hàng.

## 2. Tiền điều kiện

- Hồ sơ người bán đã xác minh đạt.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Người bán chọn tạo tin cho một lô hàng.
2. Hệ thống hiện các trường theo danh mục.
3. Bản nháp gắn một lô hàng và một hồ sơ người bán; số lượng, tình trạng, khiếm khuyết và bằng chứng phải tách trường để kiểm duyệt.
4. Người bán nhập mô tả, ảnh thực tế, tình trạng, khiếm khuyết, phí và chính sách giao hàng.
5. Ảnh và mô tả được lưu theo phiên bản; chưa có quy trình xác thực thì không hiển thị nhãn đã xác thực cho đồ sưu tầm.
6. Hệ thống lưu bản nháp chưa công khai.

## 4. Luồng thay thế

- Lưu thiếu trường được phép ở bản nháp, nhưng không được gửi duyệt.
- Người bán lưu rồi quay lại: bản nháp giữ nội dung, chưa xuất hiện trong tìm kiếm.
- Người bán đổi danh mục: hệ thống tính lại trường bắt buộc của danh mục mới.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Hàng thuộc danh mục cấm | chặn và nêu chính sách. | TC-14, TC-16 |
| Ảnh thiếu hoặc định dạng không hợp lệ | Cho lưu nháp nếu chính sách cho phép, chặn gửi duyệt. | Chưa có TC riêng |
| Hồ sơ bán hết hiệu lực | Không cho phát hành tin; bản nháp chỉ được xem/sửa theo quyền. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Có bản nháp gắn đúng người bán và một lô hàng.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Tin thiếu trường, hàng bị cấm hoặc chưa duyệt không thể mở phiên (BR-06).
- Thông tin trọng yếu sau lượt giá đầu tiên phải giữ lịch sử và được vận hành xử lý (BR-09).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-01, BR-06; P-02, P-03.

## 8. Truy vết

FR-06; BR-01, BR-06; P-02, P-03; TC-14, TC-16. BUC-03; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Danh mục cấm, trường theo danh mục và xác thực đồ sưu tầm chưa chốt.
- Danh mục cấm, trường bắt buộc và quy trình sửa nội dung trọng yếu cần được duyệt trước khi mở tin công khai.

