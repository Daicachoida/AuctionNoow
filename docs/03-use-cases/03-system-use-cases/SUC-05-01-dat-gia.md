# SUC-05-01 — Đặt giá

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-05-01 / BUC-05 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Người mua |
| Tác nhân phụ | Người bán; vận hành; đối tác thanh toán ở tầng B |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **đặt giá** trong BUC-05. Mục tiêu nghiệp vụ: lịch sử giá có thể kiểm tra lại; không có hai lượt cùng giá cùng được nhận.

## 2. Tiền điều kiện

- Phiên đang mở.
- Tài khoản đủ điều kiện.
- Tầng B có đặt trước hợp lệ.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Người mua xem giá tối thiểu và xác nhận số tiền định đặt.
2. Hệ thống xét quyền, trạng thái phiên và giá trên trạng thái mới nhất.
3. Mọi kiểm tra giá phải diễn ra trên trạng thái phiên mới nhất tại một điểm xử lý có thứ tự; không dựa vào giá hiển thị trên trang đã cũ.
4. Hệ thống ghi bền vững lượt hợp lệ theo một thứ tự chính thức.
5. Lượt được xác nhận mới được cập nhật người dẫn đầu, lịch sử và thông báo; nếu ghi bền vững thất bại thì không trả chấp nhận.
6. Hệ thống trả chấp nhận hoặc từ chối có lý do, cập nhật người dẫn đầu.

## 4. Luồng thay thế

- Lượt hợp lệ trong 2 phút cuối kích hoạt SUC-05-02; vận hành hủy lượt có căn cứ theo P-08.
- Hai người cùng đặt 120.000 khi đang dẫn 110.000: chỉ một lượt được nhận; người sau thấy giá tối thiểu mới.
- Người mua yêu cầu hủy do nhập nhầm: chuyển vận hành; lượt không tự biến mất.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Giá thấp, người bán tự đặt, người dẫn đầu tự nâng, tài khoản khóa hoặc phiên đóng | từ chối, không đổi giá. | TC-24, TC-29 đến TC-36, TC-41, TC-45, TC-46 |
| Hai giá đồng thời đạt mức tối thiểu trên ảnh chụp cũ | Xét tuần tự trên trạng thái mới; lượt sau có thể bị từ chối. | Chưa có TC riêng |
| Gửi lại cùng yêu cầu do mạng chậm | Trả kết quả của yêu cầu gốc theo khóa chống lặp, không nhân đôi lượt. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Lịch sử giá có thể kiểm tra lại; không có hai lượt cùng giá cùng được nhận.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Chỉ lượt giá đã được ghi bền vững mới làm đổi người dẫn đầu (BR-14).
- Giờ máy chủ và thứ tự ghi nhận chính thức phân xử cạnh tranh giá/mua ngay (BR-12, BR-15, BR-36).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-02, BR-03, BR-11 đến BR-16; P-06, P-08.

## 8. Truy vết

FR-14 đến FR-16; BR-02, BR-03, BR-11 đến BR-16; P-06, P-08; TC-24, TC-29 đến TC-36, TC-41, TC-45, TC-46. BUC-05; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Bước giá P-06, chống gửi lặp và ranh giới xác nhận cần chốt.
- Bước giá, giữ chỗ mua ngay và tiền đặt trước chỉ là tham số đề xuất; phải cập nhật TC khi PO chốt.

