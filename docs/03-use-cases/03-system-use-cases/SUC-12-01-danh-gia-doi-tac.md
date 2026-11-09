# SUC-12-01 — Đánh giá đối tác

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-12-01 / BUC-12 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Người mua, người bán |
| Tác nhân phụ | Vận hành xử lý đánh giá vi phạm |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **đánh giá đối tác** trong BUC-12. Mục tiêu nghiệp vụ: mỗi bên tối đa một đánh giá có nguồn giao dịch.

## 2. Tiền điều kiện

- Giao dịch hoàn tất và còn trong 30 ngày đề xuất.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Một bên mở giao dịch, chọn 1 đến 5 sao và viết nhận xét.
2. Hệ thống kiểm tra quyền, hạn và chưa đánh giá lần nào.
3. Đánh giá gắn đúng một giao dịch và chiều đánh giá; chỉ hai bên của giao dịch được đánh giá nhau.
4. Hệ thống lưu đánh giá gắn giao dịch.
5. Trạng thái công khai phải phụ thuộc vụ tranh chấp, để đánh giá đang có tranh chấp không làm lệch uy tín ngay.
6. Hệ thống công khai hoặc giữ ẩn nếu vụ tranh chấp chưa đóng.

## 4. Luồng thay thế

- Tầng A dùng hoàn tất thử nghiệm do vận hành đóng; đánh giá vi phạm chuyển SUC-12-03.
- Người đánh giá bỏ dở trước gửi: không tạo đánh giá.
- Giao dịch thử nghiệm tầng A được đóng hợp lệ: cho đánh giá theo chính sách.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Đánh giá lần hai hoặc quá 30 ngày | từ chối; điểm đã gửi không sửa. | TC-85 đến TC-88 |
| Giao dịch hủy hoặc chưa hoàn tất | Không nhận đánh giá. | Chưa có TC riêng |
| Người dùng gửi lại cùng đánh giá | Trả bản đã lưu, không tạo bản thứ hai. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Mỗi bên tối đa một đánh giá có nguồn giao dịch.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Mỗi bên đánh giá một lần trên giao dịch hoàn tất trong hạn đề xuất (BR-29, P-18).
- Thông tin uy tín công khai không tiết lộ dữ liệu xác minh gốc (BR-30).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-29; P-18.

## 8. Truy vết

FR-33; BR-29; P-18; TC-85 đến TC-88. BUC-12; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Cách tính điểm, xử lý đánh giá trả đũa chưa chốt.
- Công thức điểm uy tín, nội dung vi phạm và cách chống đánh giá thao túng chưa chốt.

