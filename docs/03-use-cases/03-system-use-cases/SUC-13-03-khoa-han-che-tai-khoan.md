# SUC-13-03 — Khóa, hạn chế tài khoản

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-13-03 / BUC-13 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Vận hành |
| Tác nhân phụ | Người dùng gửi báo cáo; các bên liên quan |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **khóa, hạn chế tài khoản** trong BUC-13. Mục tiêu nghiệp vụ: quyền mới bị hạn chế, lịch sử cũ giữ nguyên.

## 2. Tiền điều kiện

- Có vi phạm hoặc dấu hiệu rủi ro đã được xem xét.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Vận hành kiểm tra tài khoản, bằng chứng và quyền.
2. Vận hành chọn phạm vi khóa đặt giá hoặc bán hàng, thời hạn và lý do.
3. Phạm vi hạn chế có thể là đặt giá, đăng tin hoặc toàn tài khoản; không được đồng nhất các mức.
4. Hệ thống áp dụng cho hành động mới, ghi nhật ký và thông báo.
5. Thời điểm hiệu lực, hết hạn và người quyết định phải có nhật ký; mở quyền lại là sự kiện riêng.
6. Ảnh hưởng lên phiên, giao dịch đang chạy được mở xử lý riêng.

## 4. Luồng thay thế

- Có thể mở lại sau rà soát hoặc kháng nghị theo quy chế.
- Khóa tạm trong khi điều tra: thông báo và cho đường kháng nghị phù hợp.
- Có giao dịch đang giao: vận hành vẫn phải xử lý nghĩa vụ và dữ liệu cần thiết.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Khóa tài khoản có giá đang dẫn đầu | không tự xóa lượt giá cũ. | TC-91 |
| Thiếu lý do công bố theo quy chế | Không áp hạn chế. | Chưa có TC riêng |
| Tài khoản bị khóa thử đặt giá mới | Từ chối trước khi xét giá. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Quyền mới bị hạn chế, lịch sử cũ giữ nguyên.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Biện pháp vận hành cần quyền, lý do, trước/sau và nhật ký (FR-35, FR-36).
- Tín hiệu đặt giá ảo chỉ đưa vào xem xét thủ công; không tự hủy phiên (01b mục 11).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-02, BR-20; P-20.

## 8. Truy vết

FR-35, FR-36; BR-02, BR-20; P-20; TC-91. BUC-13; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Ngưỡng khóa, thời hạn và thẩm quyền chưa chốt.
- Quyền vận hành, ngưỡng can thiệp và mục chống đặt giá ảo thủ công cần PO duyệt.

