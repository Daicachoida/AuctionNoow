# SUC-11-04 — Kháng nghị

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-11-04 / BUC-11 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Người mua, người bán |
| Tác nhân phụ | Người mua, người bán; đối tác thanh toán ở tầng B |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **kháng nghị** trong BUC-11. Mục tiêu nghiệp vụ: vụ có kết quả kháng nghị và lịch sử đầy đủ.

## 2. Tiền điều kiện

- Có quyết định vừa thông báo và còn trong 48 giờ đề xuất.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Bên liên quan mở quyết định và gửi kháng nghị kèm chứng cứ mới.
2. Hệ thống kiểm tra thời hạn và số lần kháng nghị.
3. Kháng nghị phải gắn với quyết định cụ thể; lưu chứng cứ mới và thời điểm nộp.
4. Hệ thống lưu hồ sơ, thông báo vận hành.
5. Người xét kháng nghị cần thấy quyết định cũ cùng toàn bộ lịch sử và lý do thay đổi nếu đảo kết quả.
6. Tầng B tiếp tục chặn giải ngân tới khi kháng nghị đúng hạn được giải quyết.

## 4. Luồng thay thế

- Mỗi bên tối đa một lần theo P-16; vận hành ra quyết định sau xem chứng cứ mới.
- Kháng nghị đúng hạn nhưng chứng cứ chưa tải xong do lỗi: ghi nhận trạng thái nộp theo chính sách được duyệt.
- Một bên rút kháng nghị: lưu sự kiện, tiếp tục theo quyết định còn hiệu lực.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Quá 48 giờ, không có chứng cứ mới hoặc đã dùng lượt | từ chối có lý do. | TC-81, TC-82 |
| Kháng nghị chỉ lặp lại lý do cũ không có chứng cứ mới | Từ chối hoặc yêu cầu bổ sung theo P-16. | Chưa có TC riêng |
| Lệnh giải ngân đang chờ khi kháng nghị được ghi | Chặn/đối soát trước khi chi. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Vụ có kết quả kháng nghị và lịch sử đầy đủ.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Vụ tranh chấp gắn giao dịch, lý do, chứng cứ, người xử lý và quyết định có căn cứ (BR-27).
- Tầng B chỉ hoàn/giải ngân sau xác nhận của đối tác; lý do hàng giả không tự đủ để hoàn (FR-48).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-27, BR-39; P-16.

## 8. Truy vết

FR-31; BR-27, BR-39; P-16; TC-81, TC-82. BUC-11; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Quy trình người duyệt kháng nghị độc lập và thời hạn xử lý chưa chốt.
- Quy trình hàng giả phát hiện muộn, nguồn tiền hoàn và lý do đổi ý thuộc D-09.

