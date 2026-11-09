# BUC-11 — Tranh chấp, trả hàng, hoàn tiền

| Thuộc tính | Nội dung |
|---|---|
| Mã | BUC-11 |
| Phiên bản / trạng thái | 0.1 / `Đề xuất` |
| Tầng | `[A,B]` tranh chấp; `[B]` trả hàng, hoàn tiền theo P-21 |

## 1. Mục tiêu nghiệp vụ
Người mua có đường khiếu nại khi không nhận hàng, hàng sai hoặc hàng giả; nền tảng ra quyết định dựa trên chứng cứ, có lý do và nhật ký.

## 2. Tác nhân
- Chính: người mua, người bán, vận hành.
- Hệ thống ngoài `[B]`: đối tác thanh toán (thực thi hoàn).

## 3. Điều kiện kích hoạt
Tầng A: hai bên bất đồng về giao dịch ngoài nền tảng hoặc người mua báo chưa nhận hàng; vận hành tiếp nhận thủ công. Tầng B: trong 15 ngày lịch sau giao được xác minh, hoặc quá hạn gửi hàng mà hàng chưa tới (P-16).

## 4. Kết quả mong muốn và giá trị kinh doanh
- Vụ có mã theo dõi và khóa chứng cứ; ở tầng B, vụ mở đúng hạn chặn giải ngân (FR-30, TC-76, TC-78).
- Người bán có 3 ngày làm việc phản hồi; vận hành quyết định trong mục tiêu 5 ngày làm việc; mỗi bên kháng nghị một lần trong 48 giờ (P-16, TC-77, TC-81, TC-82).
- Lý do trả hàng hợp lệ theo P-21, không có "đổi ý" (TC-103); không hoàn không cần trả hàng chỉ vì người mua chọn lý do (FR-48, TC-106).
- Lạm dụng bị hạn chế theo quy trình công bố (BR-43, TC-108).

## 5. Khác biệt giữa tầng A và tầng B
Tầng A xử lý thủ công, không có lệnh hoàn tiền từ hệ thống; nếu hai bên đã chuyển tiền thật ngoài nền tảng, họ tự thực hiện thỏa thuận hoàn trả và vận hành chỉ lưu bằng chứng, không xác nhận đã hoàn. Tầng B thực thi hoàn qua đối tác và áp dụng đầy đủ P-21.

## 6. Danh sách UC con

| UC | Tên | Tầng |
|---|---|---|
| SUC-11-01 | Mở tranh chấp hoặc yêu cầu trả hàng | A, B |
| SUC-11-02 | Người bán phản hồi tranh chấp | A, B |
| SUC-11-03 | Vận hành xem xét và ra quyết định | A, B |
| SUC-11-04 | Kháng nghị quyết định | A, B |
| SUC-11-05 | Xử lý hàng giả phát hiện sau 15 ngày | B |
| SUC-11-06 | Tranh chấp sau khi đã giải ngân | B |

## 7. Truy vết
FR-30 đến FR-32, FR-46 đến FR-48 · BR-27, BR-28, BR-39, BR-42, BR-43 · P-16, P-17, P-21 · D-09 · TC-76 đến TC-84, TC-103 đến TC-108.

## 8. Điểm còn mở
- Hàng giả phát hiện sau 15 ngày: có hỗ trợ hoàn không (D-09).
- Cơ chế thu hồi tiền hoàn từ người bán (giữ tiền, ký quỹ, đòi sau).
- Bỏ lý do "đổi ý" cần PO duyệt riêng.
- Nghĩa vụ của nền tảng theo Luật Bảo vệ quyền lợi người tiêu dùng 2023 (chưa đọc văn bản luật).
