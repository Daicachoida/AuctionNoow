# SUC-05-02 — Gia hạn ở 2 phút cuối

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-05-02 / BUC-05 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Hệ thống |
| Tác nhân phụ | Người bán; vận hành; đối tác thanh toán ở tầng B |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **gia hạn ở 2 phút cuối** trong BUC-05. Mục tiêu nghiệp vụ: giờ đóng chính thức nhất quán với lịch sử giá.

## 2. Tiền điều kiện

- Lượt giá vừa được xác nhận hợp lệ trước giờ đóng.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Hệ thống lấy thời điểm xác nhận trên máy chủ.
2. Nếu thời gian còn lại không quá 2 phút, hệ thống đặt giờ đóng bằng thời điểm đó cộng 2 phút.
3. So sánh thời điểm xác nhận lượt hợp lệ với giờ đóng hiện hành, không với giờ đóng gốc hay đồng hồ người mua.
4. Hệ thống lưu thay đổi cùng lượt giá.
5. Việc ghi lượt giá và giờ đóng mới cần là một kết quả nhất quán để không có giá được nhận nhưng gia hạn bị bỏ sót.
6. Hệ thống phát giờ đóng mới trên trang phiên.

## 4. Luồng thay thế

- Mỗi lượt hợp lệ kế tiếp trong 2 phút cuối tiếp tục tính lại; lượt ngoài cửa sổ giữ giờ cũ.
- Giá lúc đúng mốc còn 2 phút: thuộc cửa sổ gia hạn.
- Hai giá hợp lệ liên tiếp gần nhau: mỗi lần tính lại từ giờ đóng hiện hành.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Lượt từ chối hoặc đến từ thời điểm đóng trở đi | không gia hạn. | TC-37 đến TC-40 |
| Giá xác nhận đúng hoặc sau giờ đóng | Từ chối, không gia hạn. | Chưa có TC riêng |
| Thông báo cập nhật giờ đóng thất bại | Giờ chính thức vẫn theo bản ghi; trang truy vấn lại được. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Giờ đóng chính thức nhất quán với lịch sử giá.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Chỉ lượt giá đã được ghi bền vững mới làm đổi người dẫn đầu (BR-14).
- Giờ máy chủ và thứ tự ghi nhận chính thức phân xử cạnh tranh giá/mua ngay (BR-12, BR-15, BR-36).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-12, BR-17.

## 8. Truy vết

FR-13, FR-17; BR-12, BR-17; TC-37 đến TC-40. BUC-05; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Cách xử lý thông báo chậm khi người dùng thấy đồng hồ cũ cần đặc tả.
- Bước giá, giữ chỗ mua ngay và tiền đặt trước chỉ là tham số đề xuất; phải cập nhật TC khi PO chốt.

