# SUC-13-02 — Ẩn, gỡ tin

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-13-02 / BUC-13 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Vận hành |
| Tác nhân phụ | Người dùng gửi báo cáo; các bên liên quan |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **ẩn, gỡ tin** trong BUC-13. Mục tiêu nghiệp vụ: tin không còn công khai theo quyết định có thể truy vết.

## 2. Tiền điều kiện

- Có căn cứ kiểm duyệt và vận hành có quyền.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Vận hành mở tin và chứng cứ.
2. Vận hành chọn ẩn hoặc gỡ, ghi lý do.
3. Khi ẩn tin đang mở, cần đồng thời ngăn hành động mới theo trạng thái phiên và chuyển xử lý BUC-14.
4. Hệ thống đổi trạng thái, lưu bản trước sau và thông báo người bán.
5. Bản công khai cũ và quyết định kiểm duyệt phải được giữ để xét khiếu nại.
6. Nếu phiên có giá, chuyển BUC-14 xử lý ảnh hưởng.

## 4. Luồng thay thế

- Tin cần sửa có thể quay lại hàng duyệt theo quy trình.
- Tin chưa có giá: có thể yêu cầu sửa và nộp lại.
- Tin có giá: không tự gỡ khỏi lịch sử hay bán cho người dẫn đầu.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Không đủ quyền hoặc thiếu lý do | không thay đổi tin. | TC-90 |
| Người bán cố mở lại tin đã gỡ | Từ chối cho tới khi duyệt lại. | Chưa có TC riêng |
| Thao tác ẩn lặp | Không tạo nhiều sự kiện thay đổi hoặc thông báo mâu thuẫn. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Tin không còn công khai theo quyết định có thể truy vết.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Biện pháp vận hành cần quyền, lý do, trước/sau và nhật ký (FR-35, FR-36).
- Tín hiệu đặt giá ảo chỉ đưa vào xem xét thủ công; không tự hủy phiên (01b mục 11).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-06, BR-20, BR-31; P-20.

## 8. Truy vết

FR-09, FR-35, FR-36; BR-06, BR-20, BR-31; P-20; TC-90. BUC-13; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Tiêu chí gỡ vĩnh viễn và kháng nghị chưa chốt.
- Quyền vận hành, ngưỡng can thiệp và mục chống đặt giá ảo thủ công cần PO duyệt.

