# BUC-03 — Đăng hàng và duyệt tin

| Thuộc tính | Nội dung |
|---|---|
| Mã | BUC-03 |
| Phiên bản / trạng thái | 0.1 / `Đề xuất` |
| Tầng | `[A,B]` |

## 1. Mục tiêu nghiệp vụ
Người bán đưa một lô hàng lên đấu giá với thông tin đủ rõ; vận hành kiểm duyệt để chặn hàng cấm, mô tả sai; phiên mở theo quy tắc đã công bố.

## 2. Tác nhân
- Chính: người bán, vận hành (kiểm duyệt).
- Phụ: hệ thống (chụp quy tắc phiên, mở phiên theo lịch).

## 3. Điều kiện kích hoạt
Người bán đã được xác minh (BUC-02) và muốn đăng hàng.

## 4. Kết quả mong muốn và giá trị kinh doanh
- Tin đủ trường bắt buộc, được duyệt, vào trạng thái chờ mở rồi đang mở (BR-06, BR-07).
- Người mua thấy thông tin đủ để quyết định đặt giá (FR-10).
- Nội dung trọng yếu bị khóa sau lượt giá đầu tiên, tạo cơ sở khi xét tranh chấp "không đúng mô tả" (BR-09).

## 5. Khác biệt giữa tầng A và tầng B
Cùng luồng. Tầng A duyệt thủ công 100% tin đầu tiên của mỗi người bán và mọi tin bị gắn cờ (P-04, 01b mục 4.2).

## 6. Danh sách UC con

| UC | Tên |
|---|---|
| SUC-03-01 | Tạo bản nháp tin |
| SUC-03-02 | Cấu hình phiên đấu giá (thời lượng, giá khởi điểm, mua ngay) |
| SUC-03-03 | Xem lại tổng hợp và gửi duyệt |
| SUC-03-04 | Vận hành duyệt, yêu cầu sửa, từ chối tin |
| SUC-03-05 | Sửa tin theo trạng thái cho phép |
| SUC-03-06 | Mở phiên theo lịch và chụp quy tắc áp dụng |

## 7. Truy vết
FR-06 đến FR-09, FR-11, FR-12 · BR-06 đến BR-10 · P-02 đến P-06, P-10 · TC-14 đến TC-22.

## 8. Điểm còn mở
- Trường bắt buộc theo danh mục; danh mục cấm và hạn chế (cổng, BR-34).
- Chuẩn xác thực đồ sưu tầm (P-03 cấm tuyên bố "đã xác thực" nếu chưa có quy trình).
- Ai có quyền duyệt tin trong thử nghiệm (01b mục 13, câu 2).
- Cách xử lý phiên đang mở khi mô tả đổi trọng yếu (FR-11, P-04).
