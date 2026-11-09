# BUC-02 — Xác minh người bán

| Thuộc tính | Nội dung |
|---|---|
| Mã | BUC-02 |
| Phiên bản / trạng thái | 0.1 / `Đề xuất` |
| Tầng | `[A]` thủ công, `[B]` mở rộng |

## 1. Mục tiêu nghiệp vụ
Chỉ người bán đã được xác minh mới phát hành tin, để người mua có cơ sở tin cậy và nền tảng đáp ứng yêu cầu về xác thực người bán.

## 2. Tác nhân
- Chính: người dùng muốn bán, vận hành (duyệt hồ sơ).
- Phụ: dịch vụ xác minh danh tính nếu thuê ngoài (chưa chọn).

## 3. Điều kiện kích hoạt
Người dùng đã có tài khoản (BUC-01) và chọn đăng ký bán hàng.

## 4. Kết quả mong muốn và giá trị kinh doanh
- Hồ sơ đi qua các trạng thái `chưa xác minh → đang xét → đạt / bị từ chối / cần xác minh lại` (FR-03).
- Người mua thấy trạng thái xác minh, không thấy giấy tờ (FR-05, BR-30).
- Đáp ứng cổng BR-04 trước khi mở quyền bán.

## 5. Khác biệt giữa tầng A và tầng B

| Nội dung | Tầng A | Tầng B |
|---|---|---|
| Loại người bán | Chỉ cá nhân và shop (M-S1, chờ PO duyệt) | Mở thêm doanh nghiệp, nhà phân phối khi có quy trình xác minh tổ chức |
| Cách duyệt | Vận hành duyệt thủ công | Có thể dùng dịch vụ xác minh |

## 6. Danh sách UC con

| UC | Tên |
|---|---|
| SUC-02-01 | Tạo hồ sơ người bán và chọn loại |
| SUC-02-02 | Nộp thông tin xác minh |
| SUC-02-03 | Vận hành duyệt hồ sơ người bán |
| SUC-02-04 | Xác minh lại khi hết hiệu lực |

Chặn đăng bán khi chưa đạt (TC-08, 09, 11) và từ chối loại chưa mở (TC-13) được mô tả trong luồng thay thế của SUC-02-01 và SUC-02-03.

## 7. Truy vết
FR-03, FR-04, FR-05 · BR-01, BR-04, BR-30 · P-01 · M-S1 · TC-08 đến TC-13.

## 8. Điểm còn mở
- Dữ liệu xác minh theo từng loại người bán; thời hạn hiệu lực.
- Có xác minh CCCD ở tầng A không.
- Ai duyệt và thời gian xét dự kiến (TC-09 yêu cầu hiển thị).
- Cổng pháp lý: Luật TMĐT 2025 và Nghị định 248/2026/NĐ-CP.
