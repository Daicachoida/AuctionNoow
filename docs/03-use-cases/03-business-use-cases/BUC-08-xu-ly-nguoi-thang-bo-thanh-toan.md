# BUC-08 — Xử lý người thắng bỏ thanh toán

| Thuộc tính | Nội dung |
|---|---|
| Mã | BUC-08 |
| Phiên bản / trạng thái | 0.1 / `Đề xuất` |
| Tầng | `[B]` đầy đủ; `[A]` chỉ ghi nhận và đo tỷ lệ bỏ |

## 1. Mục tiêu nghiệp vụ
Khi người thắng không trả đúng hạn, giao dịch được hủy có lý do, người bán được báo và đăng lại, người vi phạm chịu chế tài đã công bố trước.

## 2. Tác nhân
- Chính: hệ thống (phát hiện quá hạn), vận hành.
- Phụ: người thắng, người bán, đối tác thanh toán `[B]`.

## 3. Điều kiện kích hoạt
Quá hạn thanh toán (P-11: 48 giờ, nhắc ở 24 giờ).

## 4. Kết quả mong muốn và giá trị kinh doanh
- Giao dịch hủy có lý do, không tự trao quyền cho người đặt giá thứ hai (FR-24, TC-64).
- `[B]` tiền đặt trước xử lý theo quy tắc công bố trước, có nhật ký (BR-41, TC-100).
- Giảm bỏ thanh toán, chỉ số "tin cậy" của 01 mục 8.

## 5. Khác biệt giữa tầng A và tầng B
Tầng A không có tiền đặt trước nên không có chế tài tiền; chỉ đo tỷ lệ bỏ (01b mục 5, mục 10).

## 6. Danh sách UC con

| UC | Tên | Tầng |
|---|---|---|
| SUC-08-01 | Nhắc thanh toán, phát hiện quá hạn và hủy giao dịch | A, B |
| SUC-08-02 | Xử lý tiền đặt trước khi bỏ thanh toán | B |
| SUC-08-03 | Hạn chế tài khoản tái phạm | B |

## 7. Truy vết
FR-24, FR-35, FR-45 · BR-23, BR-40, BR-41 · P-07, P-11 · D-08 · TC-64, TC-65, TC-100.

## 8. Điểm còn mở
- Tỷ lệ đặt trước (5% đến 20% hay ngưỡng cố định cho hàng giá thấp), người nhận khoản bị mất, hạn trả.
- Có mời người đặt giá kế tiếp không (D-08).
- Mức hạn chế khi tái phạm.
- Xác minh pháp lý: đặt trước theo Điều 39 hay đặt cọc dân sự.
