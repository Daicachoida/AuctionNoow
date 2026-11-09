# SUC-05-03 — Xem trang phiên, theo dõi giá

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-05-03 / BUC-05 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Khách, người mua |
| Tác nhân phụ | Người bán; vận hành; đối tác thanh toán ở tầng B |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **xem trang phiên, theo dõi giá** trong BUC-05. Mục tiêu nghiệp vụ: trang phản ánh trạng thái chính thức gần nhất có thể tra cứu.

## 2. Tiền điều kiện

- Phiên được phép hiển thị.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Người xem mở trang phiên.
2. Hệ thống trả giá khởi điểm, giá dẫn đầu, giá tối thiểu tiếp theo, giờ đóng hiện hành.
3. Giá tối thiểu kế tiếp phải tính từ giá dẫn đầu chính thức và bậc bước giá hiện hành.
4. Hệ thống cập nhật trạng thái và lịch sử giá được phép xem.
5. Cần hiển thị lý do phiên tạm dừng, đã đóng hoặc đang giữ chỗ mua ngay; nút hành động theo trạng thái thật.
6. Người xem chọn đặt giá hoặc mua ngay khi đủ điều kiện.

## 4. Luồng thay thế

- Tầng A hiển thị cảnh báo không bảo vệ tiền; sau lượt giá đầu, nút mua ngay biến mất.
- Người xem bị vượt giá khi đang mở trang: làm mới giá, hạn và nút đặt.
- Phiên không có lượt giá: hiển thị giá khởi điểm làm giá đầu tối thiểu.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Dữ liệu hiển thị chậm | tải lại từ trạng thái chính thức, không dùng đồng hồ thiết bị phân xử. | TC-23, TC-50, TC-54, TC-102 |
| Trang cũ hiển thị mua ngay sau giá đầu | Yêu cầu gửi lên vẫn bị từ chối. | Chưa có TC riêng |
| Người xem bị mất kết nối | Không suy đoán mình còn dẫn đầu; khi kết nối lại lấy trạng thái máy chủ. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Trang phản ánh trạng thái chính thức gần nhất có thể tra cứu.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Chỉ lượt giá đã được ghi bền vững mới làm đổi người dẫn đầu (BR-14).
- Giờ máy chủ và thứ tự ghi nhận chính thức phân xử cạnh tranh giá/mua ngay (BR-12, BR-15, BR-36).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-08, BR-37.

## 8. Truy vết

FR-13, FR-16, FR-38; BR-08, BR-37; TC-23, TC-50, TC-54, TC-102. BUC-05; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Mức chi tiết lịch sử giá công khai và SLA cập nhật chưa chốt.
- Bước giá, giữ chỗ mua ngay và tiền đặt trước chỉ là tham số đề xuất; phải cập nhật TC khi PO chốt.

