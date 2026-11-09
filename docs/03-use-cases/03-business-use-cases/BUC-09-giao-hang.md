# BUC-09 — Giao hàng

| Thuộc tính | Nội dung |
|---|---|
| Mã | BUC-09 |
| Phiên bản / trạng thái | 0.1 / `Đề xuất` |
| Tầng | `[A]` tự khai, `[B]` nguồn nhà vận chuyển |

## 1. Mục tiêu nghiệp vụ
Người bán bàn giao hàng đúng hạn qua đơn vị vận chuyển có mã theo dõi; trạng thái giao hàng có nguồn rõ ràng.

## 2. Tác nhân
- Chính: người bán.
- Phụ: người mua, vận hành.
- Hệ thống ngoài `[B]`: nhà vận chuyển.

## 3. Điều kiện kích hoạt
Giao dịch đủ điều kiện giao: tầng B khi tiền được xác nhận đang giữ; tầng A khi giao dịch thử nghiệm được tạo và hai bên tự thỏa thuận giao hàng ngoài nền tảng (TC-68), không cần hệ thống xác nhận thanh toán.

## 4. Kết quả mong muốn và giá trị kinh doanh
- Hạn bàn giao 3 ngày làm việc (P-13); quá hạn chuyển ngoại lệ, người mua được mở yêu cầu (TC-70).
- Mỗi trạng thái có nguồn và thời điểm: "người bán khai", "tự khai, chưa đối soát", "nhà vận chuyển xác nhận" (FR-28, BR-25).
- Địa chỉ giao hàng chỉ hiện cho vai trò cần dùng (FR-26).

## 5. Khác biệt giữa tầng A và tầng B

| Nội dung | Tầng A | Tầng B |
|---|---|---|
| Trạng thái đã giao | Người bán tự khai, không bắt đầu tính 15 ngày như giao đã xác minh (TC-72) | Lấy từ nhà vận chuyển (TC-71) |

## 6. Danh sách UC con

| UC | Tên |
|---|---|
| SUC-09-01 | Xem thông tin giao hàng và hạn bàn giao |
| SUC-09-02 | Nhập mã vận đơn |
| SUC-09-03 | Cập nhật và theo dõi trạng thái giao hàng |
| SUC-09-04 | Xử lý quá hạn gửi hàng và giao thất bại |

## 7. Truy vết
FR-26 đến FR-28, FR-32 · BR-25 · P-13, P-14 · TC-68 đến TC-72.

## 8. Điểm còn mở
- Danh sách đơn vị vận chuyển được chấp nhận; bảo hiểm.
- Ai chịu trách nhiệm khi giao thất bại hoặc hàng hỏng (01 mục 16, câu 7).
- Tự giao, gặp mặt chưa hỗ trợ (P-13).
