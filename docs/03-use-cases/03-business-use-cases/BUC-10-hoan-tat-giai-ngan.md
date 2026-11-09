# BUC-10 — Hoàn tất giao dịch, giải ngân

| Thuộc tính | Nội dung |
|---|---|
| Mã | BUC-10 |
| Phiên bản / trạng thái | 0.1 / `Đề xuất` |
| Tầng | `[B]` tự động; `[A]` đóng thủ công |

## 1. Mục tiêu nghiệp vụ
Đóng giao dịch khi đã giao và không còn tranh chấp; tầng B chuyển tiền cho người bán hoặc hoàn cho người mua đúng một lần.

## 2. Tác nhân
- Chính: hệ thống, vận hành.
- Phụ: người bán, người mua.
- Hệ thống ngoài `[B]`: đối tác thanh toán.

## 3. Điều kiện kích hoạt
Tầng A: hai bên cung cấp bằng chứng giao hàng ngoài nền tảng để vận hành xem xét và không còn tranh chấp mở. Tầng B: giao hàng được xác minh (BUC-09) và hết cửa sổ 15 ngày lịch không có tranh chấp đúng hạn (P-15), hoặc có quyết định hoàn tiền từ BUC-11.

## 4. Kết quả mong muốn và giá trị kinh doanh
- Một giao dịch không ở hai kết quả cuối mâu thuẫn (BR-28).
- Lệnh giải ngân hoặc hoàn lặp không chuyển tiền hai lần (FR-42, FR-43, BR-38, TC-67).
- Tranh chấp đúng hạn chặn giải ngân (BR-39, TC-78); bấm "đã nhận" sớm không rút ngắn 15 ngày (TC-74).

## 5. Khác biệt giữa tầng A và tầng B

| Nội dung | Tầng A | Tầng B |
|---|---|---|
| Hoàn tất | Vận hành kiểm tra bằng chứng giao hàng, bảo đảm không có tranh chấp mở rồi đóng ở trạng thái "hoàn tất thử nghiệm", để đánh giá (BUC-12) mở được | Tự động sau 15 ngày không tranh chấp |
| Tiền | Hai bên có thể tự giao dịch tiền thật ngoài nền tảng; hệ thống không xác nhận, hoàn hoặc giải ngân | Giải ngân, hoàn qua đối tác |

Hướng xử lý tầng A đã được PO chọn: đóng thủ công theo TC-110 đến TC-113. TC-73 chỉ áp dụng tầng B vì lời khai giao hàng ở tầng A không bắt đầu cửa sổ 15 ngày.

## 6. Danh sách UC con

| UC | Tên | Tầng |
|---|---|---|
| SUC-10-01 | Hoàn tất giao dịch tự động | B |
| SUC-10-02 | Giải ngân cho người bán | B |
| SUC-10-03 | Hoàn tiền cho người mua | B |
| SUC-10-04 | Vận hành đóng giao dịch thủ công | A |

## 7. Truy vết
FR-29, FR-41 đến FR-43 · BR-26, BR-28, BR-38, BR-39 · P-15, P-17 · TC-67, TC-73 đến TC-75, TC-78, TC-84, TC-110 đến TC-113.

## 8. Điểm còn mở
- Có cho giải ngân sớm khi người mua xác nhận hài lòng không (D-09).
- Quyền ra lệnh giải ngân và hoàn của nền tảng với đối tác (cổng D-04).
- Tiêu chí bằng chứng giao hàng vận hành dùng để đóng giao dịch ở tầng A.
