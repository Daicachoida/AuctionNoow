# SUC-13-01 — Gửi, tiếp nhận báo cáo

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-13-01 / BUC-13 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Người dùng, vận hành |
| Tác nhân phụ | Người dùng gửi báo cáo; các bên liên quan |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **gửi, tiếp nhận báo cáo** trong BUC-13. Mục tiêu nghiệp vụ: có vụ việc với người phụ trách và dấu vết.

## 2. Tiền điều kiện

- Có tin, người dùng hoặc hành vi cần báo cáo.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Người dùng chọn đối tượng, lý do và gửi chứng cứ.
2. Hệ thống cấp mã vụ và chuyển hàng xử lý.
3. Vụ việc cần loại đối tượng và mức độ rủi ro để ưu tiên gian lận, hàng giả, tiền hoặc hàng cấm.
4. Vận hành phân công, đánh giá mức độ khẩn.
5. Người báo cáo chỉ thấy trạng thái phù hợp; dữ liệu điều tra và danh tính người khác không công khai.
6. Hệ thống hiển thị trạng thái và thông báo kết quả phù hợp.

## 4. Luồng thay thế

- Báo cáo hàng giả, đặt giá ảo hoặc đánh giá vi phạm chuyển đúng nhánh chuyên môn.
- Báo cáo ẩn danh nếu được chính sách cho phép: vẫn cấp mã theo dõi hạn chế.
- Người dùng bổ sung chứng cứ: thêm vào vụ cũ.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Thiếu thông tin hoặc báo cáo trùng | yêu cầu bổ sung hoặc gộp có lịch sử. | TC-89 |
| Báo cáo không có đối tượng hợp lệ | Yêu cầu chọn lại, không tạo vụ rỗng. | Chưa có TC riêng |
| Sự cố nhận báo cáo | Ghi nhận lỗi và cho gửi lại, tránh tạo vụ trùng. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Có vụ việc với người phụ trách và dấu vết.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Biện pháp vận hành cần quyền, lý do, trước/sau và nhật ký (FR-35, FR-36).
- Tín hiệu đặt giá ảo chỉ đưa vào xem xét thủ công; không tự hủy phiên (01b mục 11).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-31, BR-32; P-20.

## 8. Truy vết

FR-34; BR-31, BR-32; P-20; TC-89. BUC-13; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Kênh báo cáo, SLA và phân quyền chưa chốt.
- Quyền vận hành, ngưỡng can thiệp và mục chống đặt giá ảo thủ công cần PO duyệt.

