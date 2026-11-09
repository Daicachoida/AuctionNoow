# BUC-12 — Đánh giá

| Thuộc tính | Nội dung |
|---|---|
| Mã | BUC-12 |
| Phiên bản / trạng thái | 0.1 / `Đề xuất` |
| Tầng | `[A,B]` |

## 1. Mục tiêu nghiệp vụ
Sau giao dịch hoàn tất, hai bên đánh giá nhau để xây tín hiệu uy tín cho các giao dịch sau.

## 2. Tác nhân
- Chính: người mua, người bán.
- Phụ: vận hành (xử lý đánh giá vi phạm).

## 3. Điều kiện kích hoạt
Giao dịch ở trạng thái hoàn tất (BUC-10), trong 30 ngày kể từ lúc đó (P-18).

## 4. Kết quả mong muốn và giá trị kinh doanh
- Mỗi bên đánh giá đúng một lần, thang 1 đến 5 sao kèm nhận xét, không sửa sau khi gửi (TC-85, TC-86).
- Đánh giá của giao dịch đang tranh chấp được ẩn đến khi vụ đóng (TC-87).
- Quá 30 ngày thì không cho đánh giá (TC-88).
- Góp phần cơ chế tin cậy, mục tiêu 4 của 01.

## 5. Khác biệt giữa tầng A và tầng B
Cùng luồng; ở tầng A điều kiện "hoàn tất" là hoàn tất thử nghiệm do vận hành đóng (BUC-10).

## 6. Danh sách UC con

| UC | Tên |
|---|---|
| SUC-12-01 | Đánh giá đối tác sau giao dịch |
| SUC-12-02 | Xem uy tín công khai của người dùng |
| SUC-12-03 | Báo cáo đánh giá vi phạm |

## 7. Truy vết
FR-33, FR-34 · BR-29, BR-30 · P-18 · TC-85 đến TC-88.

## 8. Điểm còn mở
- Cách hạn chế thao túng uy tín (01 mục 16, câu 9), ví dụ đánh giá chéo giữa tài khoản liên quan.
- Công thức hiển thị điểm uy tín công khai.
