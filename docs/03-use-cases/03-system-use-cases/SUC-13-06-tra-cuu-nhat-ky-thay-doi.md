# SUC-13-06 — Tra cứu nhật ký thay đổi

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-13-06 / BUC-13 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Vận hành |
| Tác nhân phụ | Người dùng gửi báo cáo; các bên liên quan |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **tra cứu nhật ký thay đổi** trong BUC-13. Mục tiêu nghiệp vụ: có dấu vết phục vụ kiểm tra lại giá, tiền và quyết định.

## 2. Tiền điều kiện

- Vận hành có quyền tra cứu đối tượng nghiệp vụ.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Vận hành chọn phiên, tin, giao dịch hoặc tài khoản.
2. Hệ thống lấy sự kiện trọng yếu theo thời gian máy chủ.
3. Nhật ký cần bao gồm giá, kết quả, thanh toán, vận chuyển, kiểm duyệt, tranh chấp cùng tác nhân và nguồn.
4. Hệ thống hiển thị tác nhân, trước sau, nguồn và lý do khi cần.
5. Bản ghi gốc không được sửa bởi giao diện tra cứu; điều chỉnh là sự kiện mới có lý do.
6. Vận hành dùng nhật ký để xử lý sự cố hoặc tranh chấp.

## 4. Luồng thay thế

- Dữ liệu nhạy cảm được che theo vai trò; xuất hồ sơ theo quyền được cấp.
- Vận hành lọc theo khoảng thời gian và loại sự kiện để điều tra.
- Cần xuất hồ sơ cho hỗ trợ: kiểm tra quyền và ghi nhận lần xuất.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Không đủ quyền hoặc không có sự kiện | không lộ dữ liệu riêng, thông báo rõ. | TC-92 |
| Người dùng không có quyền xem giấy tờ hoặc tiền | Che dữ liệu, không trả trong phản hồi. | Chưa có TC riêng |
| Nhật ký sự kiện thiếu trước/sau | Đánh dấu thiếu và mở sự cố dữ liệu. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Có dấu vết phục vụ kiểm tra lại giá, tiền và quyết định.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Biện pháp vận hành cần quyền, lý do, trước/sau và nhật ký (FR-35, FR-36).
- Tín hiệu đặt giá ảo chỉ đưa vào xem xét thủ công; không tự hủy phiên (01b mục 11).
- Mã quy tắc/đề xuất liên quan trực tiếp: NFR-03, NFR-08; BR-30, BR-33.

## 8. Truy vết

FR-36; NFR-03, NFR-08; BR-30, BR-33; TC-92. BUC-13; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Thời hạn lưu và định dạng xuất chưa chốt.
- Quyền vận hành, ngưỡng can thiệp và mục chống đặt giá ảo thủ công cần PO duyệt.

