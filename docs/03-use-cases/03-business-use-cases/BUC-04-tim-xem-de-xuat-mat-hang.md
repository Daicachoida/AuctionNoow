# BUC-04 — Tìm, xem và đề xuất mặt hàng

| Thuộc tính | Nội dung |
|---|---|
| Mã | BUC-04 |
| Phiên bản / trạng thái | 0.1 / `Đề xuất`; phần đề xuất mặt hàng là ngoài MVP, chờ PO |
| Tầng | `[A,B]` |

## 1. Mục tiêu nghiệp vụ
Người mua tìm được và đánh giá được hàng phù hợp; nền tảng tăng cơ hội một phiên có người đặt giá bằng cách đưa đúng hàng tới đúng người.

## 2. Tác nhân
- Chính: khách, người mua.
- Phụ: hệ thống tìm kiếm và đề xuất.

## 3. Điều kiện kích hoạt
Người dùng vào trang chủ, tìm kiếm, lọc theo danh mục hoặc xem một tin.

## 4. Kết quả mong muốn và giá trị kinh doanh
- Chỉ tin đã duyệt và đang hiển thị mới được trả về (TC-25).
- Trang chi tiết cho thấy mô tả, người bán, giá, mốc thời gian, chi phí bổ sung, quy tắc phiên (FR-10).
- Góp phần chỉ số thanh khoản: tỷ lệ phiên có lượt giá hợp lệ (01 mục 8).

## 5. Khác biệt giữa tầng A và tầng B
Không khác.

## 6. Danh sách UC con

| UC | Tên | Phạm vi |
|---|---|---|
| SUC-04-01 | Tìm kiếm và lọc tin | MVP |
| SUC-04-02 | Xem chi tiết tin | MVP |
| SUC-04-03 | Đề xuất mặt hàng cho người dùng | **Ngoài MVP, đề xuất** |

## 7. Truy vết
FR-10 · TC-23, TC-25 đến TC-28.
SUC-04-03 chưa có FR trong 02; 01 mục 9.3 và 01b mục 5 đang loại "gợi ý cá nhân hóa" khỏi MVP.

## 8. Điểm còn mở
- **Đề xuất mặt hàng:** PO cần chốt mức độ. Bản đơn giản (cùng danh mục, phiên sắp kết thúc, phiên nhiều lượt giá) có thể thêm sớm. Bản cá nhân hóa (dựa lịch sử xem và đặt giá) cần FR mới trong 02, dữ liệu hành vi, và rà soát dữ liệu cá nhân (BR-33).
- Kết quả tìm kiếm dựa trên tiêu chí nào khi nhiều tin khớp (thứ tự sắp xếp chưa chốt).
