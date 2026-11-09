# SUC-07-03 — Thanh toán qua đối tác

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-07-03 / BUC-07 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[B]` |
| Tác nhân chính | Người thắng |
| Tác nhân phụ | Người bán; vận hành; đối tác thanh toán ở tầng B |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **thanh toán qua đối tác** trong BUC-07. Mục tiêu nghiệp vụ: tiền được ghi nhận theo nguồn đáng tin; không tự giải ngân.

## 2. Tiền điều kiện

- Giao dịch đang chờ trả.
- Đối tác giữ tiền đã đạt cổng D-04.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Người thắng xem khoản còn lại sau đặt trước.
2. Người thắng thanh toán qua đối tác.
3. Hệ thống nhận và kiểm tra xác nhận có thể đối soát.
4. Hệ thống ghi riêng đã trả và đang giữ, lưu mã tham chiếu.
5. Xác nhận từ đối tác phải mang giao dịch, số tiền, mã tham chiếu và trạng thái phù hợp với khoản còn lại.
6. Đã trả, đang giữ, đủ điều kiện giải ngân và đã giải ngân là các trạng thái khác nhau; ghi riêng mốc và nguồn.
7. Hệ thống thông báo các bên.

## 4. Luồng thay thế

- Thanh toán thiếu hoặc thừa chuyển đối soát; trang quay về chỉ hiển thị đang xử lý tới khi có xác nhận.
- Người trả thiếu: giữ trạng thái cần đối soát/chưa hoàn tất theo chính sách.
- Đối tác báo thất bại rồi báo thành công: đưa vào quy trình SUC-07-04, không ghi đè mù.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Quá hạn hoặc đối tác báo thất bại | không ghi đã trả, mở nhánh SUC-08-01. | TC-61, TC-66, TC-99 |
| Trang quay về thành công nhưng chưa có webhook | Hiển thị chờ xác nhận, không mở giao hàng. | Chưa có TC riêng |
| Số tiền không khớp hoặc giao dịch đã hủy | Chặn chuyển trạng thái tự động, báo vận hành. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Tiền được ghi nhận theo nguồn đáng tin; không tự giải ngân.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Lời khai hoặc trang quay về không đủ xác nhận đã thanh toán (BR-22).
- Đã trả, đang giữ, đã giải ngân và đã hoàn phải được theo dõi riêng (FR-22, BR-38).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-22, BR-24, BR-38; P-11, P-12.

## 8. Truy vết

FR-22, FR-23, FR-41, FR-45; BR-22, BR-24, BR-38; P-11, P-12; TC-61, TC-66, TC-99. BUC-07; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Đối tác, cách giữ tiền, phí, thuế và chargeback chưa chốt.
- Đối tác thanh toán, nguồn xác nhận và cách đối soát thiếu/thừa tiền thuộc cổng D-04.

