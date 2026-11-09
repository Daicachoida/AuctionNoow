# BUC-14 — Dừng hoặc hủy phiên có căn cứ

| Thuộc tính | Nội dung |
|---|---|
| Mã | BUC-14 |
| Phiên bản / trạng thái | 0.1 / `Đề xuất` |
| Tầng | `[A,B]` |

## 1. Mục tiêu nghiệp vụ
Khi hàng không còn, tin sai trọng yếu, nghi gian lận hoặc lỗi hệ thống, phiên được dừng đúng người, đúng căn cứ, các bên được báo, và người bán không lợi dụng việc dừng để bán riêng cho người dẫn đầu.

## 2. Tác nhân
- Chính: người bán (trước lượt giá đầu tiên), vận hành (sau đó).
- Phụ: người đặt giá, người xem phiên.

## 3. Điều kiện kích hoạt
Người bán bấm dừng, hoặc vận hành nhận được căn cứ dừng (hàng mất hoặc hỏng, tin sai, nghi gian lận, sự cố).

## 4. Kết quả mong muốn và giá trị kinh doanh
- Người bán tự dừng được trước lượt giá hợp lệ đầu tiên, tin dừng và không mở phiên (P-09, TC-47).
- Sau lượt giá đầu tiên chỉ vận hành được dừng, có lý do công bố (BR-10, TC-48, TC-49).
- Lượt giá cũ không tự chuyển thành giao dịch; mọi người đặt giá được thông báo (FR-19).
- Hủy vì gian lận hoặc lỗi hệ thống có căn cứ, người có thẩm quyền, cách báo và kháng nghị (BR-20).

## 5. Khác biệt giữa tầng A và tầng B
Tầng B thêm việc giải phóng tiền đặt trước của người đặt giá khi phiên bị dừng, chưa có quy tắc cụ thể.

## 6. Danh sách UC con

| UC | Tên |
|---|---|
| SUC-14-01 | Người bán dừng tin trước lượt giá đầu tiên |
| SUC-14-02 | Vận hành dừng hoặc hủy phiên có căn cứ |
| SUC-14-03 | Xử lý lượt giá đã có và thông báo các bên |

## 7. Truy vết
FR-19, FR-35 · BR-09, BR-10, BR-20 · P-09, P-20 · NFR-06 · TC-47 đến TC-49.

## 8. Điểm còn mở
- Có bù thời gian khi sự cố hệ thống không (NFR-06).
- Xử lý tiền đặt trước khi phiên bị dừng ở tầng B (D-08).
- Quy trình kháng nghị việc hủy phiên.
