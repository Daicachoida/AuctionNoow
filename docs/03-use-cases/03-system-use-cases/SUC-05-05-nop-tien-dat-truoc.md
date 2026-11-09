# SUC-05-05 — Nộp tiền đặt trước

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-05-05 / BUC-05 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[B]` |
| Tác nhân chính | Người mua |
| Tác nhân phụ | Người bán; vận hành; đối tác thanh toán ở tầng B |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **nộp tiền đặt trước** trong BUC-05. Mục tiêu nghiệp vụ: có khoản đặt trước hợp lệ cho phiên; tiền không đi vào tài khoản dự án.

## 2. Tiền điều kiện

- Phiên đang mở và đối tác giữ tiền đã được phê duyệt.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Hệ thống hiển thị khoản đặt trước, hạn hoàn và trường hợp mất trước khi người mua xác nhận.
2. Người mua yêu cầu nộp qua đối tác.
3. Khoản đặt trước phải gắn riêng với phiên, người mua và trạng thái đối tác; không dùng số dư chung không truy vết.
4. Hệ thống chờ xác nhận đối soát.
5. Trước lượt giá đầu, hệ thống kiểm tra khoản còn đang giữ hợp lệ, không chỉ từng được thanh toán.
6. Khi đối tác xác nhận, hệ thống gắn khoản đang giữ với đúng người và phiên.

## 4. Luồng thay thế

- Người không thắng được hoàn hoặc giải phóng; người thắng chuyển khoản thành phần đã trả theo SUC-07-03.
- Người dùng nộp cho nhiều phiên: từng khoản được quản lý riêng theo quyết định D-08.
- Người không thắng: gửi giải phóng/hoàn trong hạn được công bố và đối soát kết quả.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Chưa có xác nhận hoặc sự kiện trùng | không mở quyền đặt giá hoặc ghi hai khoản. | TC-96 đến TC-99, TC-101 |
| Đối tác chưa xác nhận giữ tiền | Từ chối lượt giá đầu, hiển thị đang chờ. | Chưa có TC riêng |
| Khoản bị hoàn hoặc hết hiệu lực trước khi đặt | Không mở quyền đặt giá. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Có khoản đặt trước hợp lệ cho phiên; tiền không đi vào tài khoản dự án.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Chỉ lượt giá đã được ghi bền vững mới làm đổi người dẫn đầu (BR-14).
- Giờ máy chủ và thứ tự ghi nhận chính thức phân xử cạnh tranh giá/mua ngay (BR-12, BR-15, BR-36).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-11, BR-40, BR-41; P-07.

## 8. Truy vết

FR-44, FR-45; BR-11, BR-40, BR-41; P-07; TC-96 đến TC-99, TC-101. BUC-05; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- D-08: tỷ lệ, thời điểm thu, nhiều phiên đồng thời, pháp lý và đối tác chưa chốt.
- Bước giá, giữ chỗ mua ngay và tiền đặt trước chỉ là tham số đề xuất; phải cập nhật TC khi PO chốt.

