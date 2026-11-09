# SUC-03-06 — Mở phiên theo lịch, chụp quy tắc

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-03-06 / BUC-03 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Hệ thống |
| Tác nhân phụ | Vận hành; người mua chịu ảnh hưởng |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **mở phiên theo lịch, chụp quy tắc** trong BUC-03. Mục tiêu nghiệp vụ: một phiên đang mở với quy tắc bất biến để xét giá và tranh chấp.

## 2. Tiền điều kiện

- Tin đã duyệt, đủ điều kiện công khai và đến lịch mở.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Hệ thống kiểm tra tin, người bán và lịch.
2. Hệ thống chụp bản mô tả, giá, bước giá, mua ngay, điều kiện giao dịch.
3. Bản chụp phải gồm giá khởi điểm, bước giá, mua ngay, thời điểm, mô tả và điều khoản áp dụng cho phiên.
4. Hệ thống chuyển phiên sang đang mở.
5. Chỉ sau khi bản chụp lưu thành công mới chuyển phiên sang đang mở và nhận giá.
6. Trang phiên hiển thị giờ đóng và quy tắc chính thức.

## 4. Luồng thay thế

- Nếu lịch thay đổi trước mở, cần bản quy tắc mới và thông báo theo chính sách.
- Có yêu cầu hoãn hợp lệ trước mở: giữ chờ mở và công bố lịch mới.
- Lệnh mở chạy lại: giữ cùng một phiên và một bản quy tắc chính thức.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Tin chưa duyệt hoặc người bán mất quyền | không mở phiên, ghi lý do. | TC-15, TC-23 |
| Người bán bị khóa trước giờ mở | Không mở, chuyển vận hành xét ảnh hưởng. | Chưa có TC riêng |
| Bản chụp quy tắc không lưu được | Không nhận giá; báo lỗi vận hành. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Một phiên đang mở với quy tắc bất biến để xét giá và tranh chấp.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Tin thiếu trường, hàng bị cấm hoặc chưa duyệt không thể mở phiên (BR-06).
- Thông tin trọng yếu sau lượt giá đầu tiên phải giữ lịch sử và được vận hành xử lý (BR-09).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-06 đến BR-08.

## 8. Truy vết

FR-12, FR-13; BR-06 đến BR-08; TC-15, TC-23. BUC-03; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Cách hoãn mở và thông báo khi điều kiện phát hành thay đổi chưa chốt.
- Danh mục cấm, trường bắt buộc và quy trình sửa nội dung trọng yếu cần được duyệt trước khi mở tin công khai.

