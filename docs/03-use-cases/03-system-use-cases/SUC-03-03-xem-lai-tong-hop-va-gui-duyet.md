# SUC-03-03 — Xem lại tổng hợp và gửi duyệt

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-03-03 / BUC-03 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Người bán |
| Tác nhân phụ | Vận hành; người mua chịu ảnh hưởng |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **xem lại tổng hợp và gửi duyệt** trong BUC-03. Mục tiêu nghiệp vụ: tin chờ duyệt; phiên chưa công khai.

## 2. Tiền điều kiện

- Tin và cấu hình phiên đang ở bản nháp.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Người bán mở màn hình tổng hợp như người mua sẽ thấy.
2. Hệ thống hiển thị mô tả, giá, phí, giao hàng, đổi trả, quy tắc phiên.
3. Trang tổng hợp phải dùng chính dữ liệu sẽ công khai, tránh người bán duyệt một bản khác bản người mua xem.
4. Người bán xác nhận gửi duyệt.
5. Khi gửi, hệ thống khóa phiên bản bản nháp đưa vào hàng duyệt và lưu thời điểm, người gửi.
6. Hệ thống kiểm tra toàn bộ dữ liệu và chuyển tin sang chờ duyệt.

## 4. Luồng thay thế

- Nếu người bán quay lại sửa: giữ bản nháp và kiểm tra lại khi gửi.
- Người bán phát hiện sai ở trang tổng hợp: quay lại sửa nháp rồi xem lại.
- Tin từng bị yêu cầu sửa: gửi lại tạo vòng duyệt mới, giữ lý do cũ.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Thiếu tiêu đề, ảnh hoặc trường bắt buộc | báo đúng trường và không chuyển trạng thái. | TC-14, TC-15, TC-22 |
| Tin chưa có chính sách trả hàng | Chặn gửi nếu P-03 được duyệt. | Chưa có TC riêng |
| Tài khoản mất quyền bán trước lúc gửi | Không chuyển chờ duyệt, hướng xác minh lại. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Tin chờ duyệt; phiên chưa công khai.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Tin thiếu trường, hàng bị cấm hoặc chưa duyệt không thể mở phiên (BR-06).
- Thông tin trọng yếu sau lượt giá đầu tiên phải giữ lịch sử và được vận hành xử lý (BR-09).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-06, BR-07; P-03.

## 8. Truy vết

FR-06 đến FR-08; BR-06, BR-07; P-03; TC-14, TC-15, TC-22. BUC-03; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Danh sách trường bắt buộc cuối cùng cần PO duyệt.
- Danh mục cấm, trường bắt buộc và quy trình sửa nội dung trọng yếu cần được duyệt trước khi mở tin công khai.

