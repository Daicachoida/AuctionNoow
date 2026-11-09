# BUC-05 — Đặt giá và mua ngay

| Thuộc tính | Nội dung |
|---|---|
| Mã | BUC-05 |
| Phiên bản / trạng thái | 0.1 / `Đề xuất` (bản mẫu định dạng) |
| Tầng | `[A,B]`; tiền đặt trước chỉ ở `[B]` |

## 1. Mục tiêu nghiệp vụ
Người mua tham gia cạnh tranh giá trên một phiên đang mở, hoặc mua ngay trước khi có lượt giá đầu tiên, để giành quyền mua lô hàng. Người bán khám phá được mức giá qua cạnh tranh (01 mục 3 và 6).

## 2. Tác nhân
- Chính: người mua.
- Phụ: người bán (xem diễn biến, không được đặt giá), vận hành (hủy lượt giá có lý do).
- Hệ thống ngoài `[B]`: đối tác thanh toán (giữ tiền đặt trước, xác nhận thanh toán mua ngay).

## 3. Điều kiện kích hoạt
Người mua mở trang một phiên đang mở và muốn đặt giá hoặc mua ngay.

## 4. Kết quả mong muốn và giá trị kinh doanh
- Mỗi lượt giá được xác nhận hoặc từ chối rõ ràng, đúng một thứ tự chính thức, truy vết được (mục tiêu 2 của 01, chỉ số "tính đúng đắn").
- Phiên có người dẫn đầu hợp lệ để BUC-06 xác định người thắng (chỉ số "phiên có lượt giá hợp lệ").
- Một lô hàng chỉ có một kết quả bán chính thức (BR-36).

## 5. Khác biệt giữa tầng A và tầng B

| Nội dung | Tầng A | Tầng B |
|---|---|---|
| Điều kiện đặt giá | Xác thực email, SĐT, đồng ý điều khoản | Thêm tiền đặt trước hợp lệ đang giữ cho phiên (FR-44, P-07) |
| Cảnh báo | Hiển thị cảnh báo không có bảo vệ tiền (TC-102, M-D2) | Không cần cảnh báo này |
| Mua ngay có thanh toán | Xác nhận mua ngay tạo giao dịch thử nghiệm ngay; hai bên tự thanh toán ngoài nền tảng, hệ thống không xác nhận tiền (TC-109) | Giữ chỗ 10 phút, chờ đối tác xác nhận (P-10) |

## 6. Danh sách UC con

| UC | Tên | Tầng |
|---|---|---|
| SUC-05-01 | Đặt giá | A, B |
| SUC-05-02 | Gia hạn phiên ở 2 phút cuối | A, B |
| SUC-05-03 | Xem trang phiên và theo dõi giá | A, B |
| SUC-05-04 | Mua ngay và giữ chỗ | A, B |
| SUC-05-05 | Nộp tiền đặt trước | B |
| SUC-05-06 | Thông báo bị vượt giá và kết quả phiên | A, B |

## 7. Truy vết
FR-12 đến FR-16, FR-38 đến FR-40, FR-44 · BR-02, 03, 05, 08, 11 đến 19, 35 đến 37, 40, 41 · P-05, P-06, P-07, P-08, P-10 · TC-01 đến 05, 24, 29 đến 41, 45, 46, 50 đến 56, 94 đến 97, 102, 109, 114.

## 8. Điểm còn mở
- Mua ngay có bật trong MVP không (ảnh hưởng TC-50 đến TC-56, TC-109 và TC-114).
- Tiền đặt trước ở tầng B: tỷ lệ, thời điểm thu, người có nhiều phiên đồng thời (D-08).
- Thời hạn lưu khóa chống gửi lặp (NFR-02).
