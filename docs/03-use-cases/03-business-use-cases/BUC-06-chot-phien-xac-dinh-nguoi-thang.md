# BUC-06 — Chốt phiên, xác định người thắng

| Thuộc tính | Nội dung |
|---|---|
| Mã | BUC-06 |
| Phiên bản / trạng thái | 0.1 / `Đề xuất` |
| Tầng | `[A,B]` |

## 1. Mục tiêu nghiệp vụ
Khi phiên hết giờ, xác định kết quả đúng một lần theo quy tắc đã công bố, tạo giao dịch nếu có người thắng, và thông báo các bên.

## 2. Tác nhân
- Chính: hệ thống (tiến trình đóng phiên).
- Phụ: người thắng, người bán, vận hành (kiểm tra bằng chứng).

## 3. Điều kiện kích hoạt
Đến giờ đóng hiện hành (đã tính gia hạn ở SUC-05-02), hoặc phiên kết thúc bằng mua ngay (BUC-05).

## 4. Kết quả mong muốn và giá trị kinh doanh
- Đúng một người thắng và một giao dịch khi có giá hợp lệ; không có gì khi không có giá (BR-18, BR-19, TC-42, TC-43).
- Bằng chứng lưu đủ để kiểm tra lại kết quả (FR-17), phục vụ chỉ số "tính đúng đắn".
- Chạy lặp tiến trình không tạo thêm người thắng hay giao dịch (TC-44).

## 5. Khác biệt giữa tầng A và tầng B
Cùng luồng. Giao dịch ở tầng A đánh dấu "thử nghiệm" (01b mục 2).

## 6. Danh sách UC con

| UC | Tên |
|---|---|
| SUC-06-01 | Đóng phiên và xác định người thắng |
| SUC-06-02 | Đóng phiên không có giá hợp lệ |
| SUC-06-03 | Tạo giao dịch và thông báo kết quả |

## 7. Truy vết
FR-17, FR-18, FR-20, FR-21 · BR-17 đến BR-19, BR-21 · TC-42 đến TC-44, TC-57, TC-58.

## 8. Điểm còn mở
- Phiên không có giá: có tự đăng lại không (ma trận ngoại lệ 02 mục 6).
- Lưu bằng chứng ở mức nào, giữ bao lâu (NFR-03, BR-33).
- Lượt giá đến đúng giây đóng (xem SUC-05-02).
