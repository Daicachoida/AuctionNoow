# SUC-07-01 — Xem thông tin thanh toán

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-07-01 / BUC-07 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Người thắng |
| Tác nhân phụ | Người bán; vận hành; đối tác thanh toán ở tầng B |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **xem thông tin thanh toán** trong BUC-07. Mục tiêu nghiệp vụ: người thắng hiểu số tiền và trạng thái trước khi hành động.

## 2. Tiền điều kiện

- Có giao dịch gắn người thắng.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Người thắng mở giao dịch.
2. Hệ thống hiển thị giá chốt, tiền đặt trước nếu có, phí vận chuyển và hạn trả.
3. Số tiền phải trả ở tầng B trừ tiền đặt trước đúng một lần; phí và vận chuyển phải nêu bên chịu.
4. Hệ thống phân biệt tiền đã trả, đang giữ và đã giải ngân.
5. Trang cần cho thấy nguồn xác nhận của từng trạng thái: lời tự khai, đối tác hoặc vận hành.
6. Người thắng chọn bước thanh toán phù hợp tầng.

## 4. Luồng thay thế

- Tầng A hiển thị cảnh báo chuyển khoản ngoài nền tảng không được bảo vệ; tầng B hiện phần còn lại sau đặt trước.
- Tầng A: nêu rõ đây là giao dịch thử nghiệm và rủi ro tự chuyển khoản.
- Tầng B: trạng thái đối tác đang xử lý thì không khuyến khích trả lần hai.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Không có quyền xem giao dịch | từ chối và không lộ dữ liệu người khác. | TC-57, TC-58, TC-66 |
| Khoản đặt trước chưa đối soát | Không hiển thị như đã trả chắc chắn. | Chưa có TC riêng |
| Người xem không phải bên giao dịch | Ẩn địa chỉ và số tiền chi tiết theo quyền. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Người thắng hiểu số tiền và trạng thái trước khi hành động.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Lời khai hoặc trang quay về không đủ xác nhận đã thanh toán (BR-22).
- Đã trả, đang giữ, đã giải ngân và đã hoàn phải được theo dõi riêng (FR-22, BR-38).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-21, BR-22; P-11, P-12.

## 8. Truy vết

FR-20 đến FR-22; BR-21, BR-22; P-11, P-12; TC-57, TC-58, TC-66. BUC-07; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Phí và hạn trả cuối cùng chờ PO, đối tác.
- Đối tác thanh toán, nguồn xác nhận và cách đối soát thiếu/thừa tiền thuộc cổng D-04.

