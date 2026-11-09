# SUC-12-03 — Báo cáo đánh giá vi phạm

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-12-03 / BUC-12 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Người dùng |
| Tác nhân phụ | Vận hành xử lý đánh giá vi phạm |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **báo cáo đánh giá vi phạm** trong BUC-12. Mục tiêu nghiệp vụ: đánh giá có kết quả kiểm duyệt và nhật ký.

## 2. Tiền điều kiện

- Có đánh giá công khai hoặc đang xét mà người dùng liên quan thấy.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Người dùng chọn đánh giá và nêu lý do vi phạm.
2. Hệ thống tạo báo cáo gắn đánh giá, tài khoản và giao dịch.
3. Báo cáo cần chỉ rõ đánh giá nào, lý do và chứng cứ; không cho người báo cáo sửa nội dung gốc.
4. Vận hành xét theo SUC-13-01.
5. Quyết định gỡ/giữ phải có căn cứ, thông báo hai bên và cập nhật điểm uy tín nếu đánh giá không còn hiệu lực.
6. Hệ thống giữ, ẩn hoặc gỡ theo quyết định có lý do.

## 4. Luồng thay thế

- Người bị đánh giá có thể gửi chứng cứ phản hồi.
- Người bị đánh giá bổ sung bằng chứng: gắn vào vụ hiện có.
- Báo cáo rút: lưu lịch sử, vận hành vẫn có thể xét nếu vi phạm nghiêm trọng.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Báo cáo trùng hoặc không có căn cứ | không tự xóa đánh giá. | Chưa có TC |
| Báo cáo trùng | Gộp vào vụ, không gỡ đánh giá tức thì. | Chưa có TC riêng |
| Vận hành không có quyền kiểm duyệt | Không đổi trạng thái đánh giá. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Đánh giá có kết quả kiểm duyệt và nhật ký.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Mỗi bên đánh giá một lần trên giao dịch hoàn tất trong hạn đề xuất (BR-29, P-18).
- Thông tin uy tín công khai không tiết lộ dữ liệu xác minh gốc (BR-30).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-29, BR-31; P-18, P-20.

## 8. Truy vết

FR-33, FR-34; BR-29, BR-31; P-18, P-20. BUC-12; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Tiêu chí đánh giá vi phạm và quyền kháng nghị chưa chốt.
- Công thức điểm uy tín, nội dung vi phạm và cách chống đánh giá thao túng chưa chốt.

