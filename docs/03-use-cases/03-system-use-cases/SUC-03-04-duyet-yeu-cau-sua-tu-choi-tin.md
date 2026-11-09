# SUC-03-04 — Duyệt, yêu cầu sửa, từ chối tin

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-03-04 / BUC-03 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Vận hành |
| Tác nhân phụ | Vận hành; người mua chịu ảnh hưởng |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **duyệt, yêu cầu sửa, từ chối tin** trong BUC-03. Mục tiêu nghiệp vụ: trạng thái tin và lý do quyết định có thể truy vết.

## 2. Tiền điều kiện

- Tin chờ duyệt và vận hành có quyền.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Hệ thống đưa tin đầu tiên hoặc bị gắn cờ vào hàng duyệt.
2. Vận hành xem nội dung và bằng chứng.
3. Vận hành kiểm tra danh mục, ảnh thực tế, tuyên bố xác thực, phí và điều kiện giao dịch theo bản tin được gửi.
4. Vận hành chọn duyệt, cần sửa hoặc từ chối kèm lý do.
5. Quyết định duyệt phải tham chiếu đúng phiên bản tin; chỉnh sửa mới sau duyệt cần xét lại nếu ảnh hưởng trọng yếu.
6. Hệ thống ghi nhật ký và thông báo người bán.

## 4. Luồng thay thế

- Tin đạt chuyển đã duyệt rồi chờ mở; tin cần sửa giữ bản cũ để đối chiếu.
- Tin cần sửa: người bán thấy lý do từng mục và đường nộp lại.
- Tin bị gắn cờ dù không phải tin đầu tiên: vẫn vào hàng duyệt thủ công.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Thiếu quyền hoặc thuộc hàng cấm | không duyệt. | TC-17 đến TC-19 |
| Phiên bản tin đổi khi vận hành đang xem | Không áp quyết định cũ; tải phiên bản mới. | Chưa có TC riêng |
| Thiếu danh mục cấm đã duyệt | Không tự mở công khai tin rủi ro. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Trạng thái tin và lý do quyết định có thể truy vết.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Tin thiếu trường, hàng bị cấm hoặc chưa duyệt không thể mở phiên (BR-06).
- Thông tin trọng yếu sau lượt giá đầu tiên phải giữ lịch sử và được vận hành xử lý (BR-09).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-06, BR-07; P-04.

## 8. Truy vết

FR-08, FR-09; BR-06, BR-07; P-04; TC-17 đến TC-19. BUC-03; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Ai duyệt và tiêu chí rủi ro phải chốt trước thử nghiệm.
- Danh mục cấm, trường bắt buộc và quy trình sửa nội dung trọng yếu cần được duyệt trước khi mở tin công khai.

