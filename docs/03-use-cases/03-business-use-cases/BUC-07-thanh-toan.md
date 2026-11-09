# BUC-07 — Thanh toán

| Thuộc tính | Nội dung |
|---|---|
| Mã | BUC-07 |
| Phiên bản / trạng thái | 0.1 / `Đề xuất` |
| Tầng | `[A]` ghi nhận tự khai, `[B]` thanh toán bảo đảm |

## 1. Mục tiêu nghiệp vụ
Người thắng trả tiền cho giao dịch, và nền tảng ghi nhận đúng trạng thái tiền để không bao giờ gộp "đã trả" với "đã chi cho người bán".

## 2. Tác nhân
- Chính: người thắng.
- Phụ: người bán, vận hành (đối soát).
- Hệ thống ngoài `[B]`: đối tác thanh toán / giữ tiền (chưa chọn).

## 3. Điều kiện kích hoạt
Giao dịch được tạo ở BUC-06; người thắng có hạn thanh toán.

## 4. Kết quả mong muốn và giá trị kinh doanh
- Chỉ nguồn đáng tin cậy mới đổi trạng thái sang `đã thanh toán` (BR-22).
- Tiền vào cơ chế giữ đã xác minh, ghi `đang giữ` khi có bằng chứng từ đối tác (FR-41, BR-24).
- Sự kiện trùng, muộn, mâu thuẫn không tạo giao dịch hay trạng thái sai (FR-23).

## 5. Khác biệt giữa tầng A và tầng B

| Nội dung | Tầng A | Tầng B |
|---|---|---|
| Tiền | Hai bên có thể tự chuyển tiền thật ngoài nền tảng; hệ thống chỉ lưu lời khai "người thắng khai, chưa đối soát", không nhận, giữ, xác nhận hoặc bảo vệ tiền (M-D2, TC-59) | Qua đối tác; tiền đặt trước chuyển thành phần đã trả, người thắng trả phần còn lại trong 48 giờ (FR-45, P-11) |
| Chỉ số thanh toán | Không tính khai báo tự khai | Tính khi có đối soát |

## 6. Danh sách UC con

| UC | Tên | Tầng |
|---|---|---|
| SUC-07-01 | Xem thông tin thanh toán của giao dịch | A, B |
| SUC-07-02 | Ghi nhận thanh toán tự khai | A |
| SUC-07-03 | Thanh toán qua đối tác | B |
| SUC-07-04 | Xử lý sự kiện thanh toán trùng hoặc đến muộn | B |
| SUC-07-05 | Vận hành tra cứu và đối soát thanh toán | A, B |

## 7. Truy vết
FR-20 đến FR-25, FR-41, FR-45 · BR-21 đến BR-24, BR-38 · P-11, P-12 · TC-57 đến TC-63, TC-65, TC-66, TC-99, TC-101.

## 8. Điểm còn mở
- Đối tác thanh toán, chủ thể giữ tiền, phí, thuế (cổng D-04).
- Hạn trả 48 giờ so với 3 đến 4 ngày của các sàn khác (02 mục 9.5).
- Xử lý thanh toán thiếu hoặc thừa tiền.
