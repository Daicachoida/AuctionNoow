# BUC-13 — Giám sát, kiểm duyệt, chống đặt giá ảo

| Thuộc tính | Nội dung |
|---|---|
| Mã | BUC-13 |
| Phiên bản / trạng thái | 0.1 / `Đề xuất`; phần chống đặt giá ảo chờ PO duyệt (M-D5) |
| Tầng | `[A,B]` |

## 1. Mục tiêu nghiệp vụ
Vận hành tiếp nhận báo cáo, kiểm duyệt nội dung, phát hiện hành vi đặt giá ảo ở mức thủ công, và có nhật ký cùng báo cáo để điều hành thử nghiệm.

## 2. Tác nhân
- Chính: vận hành.
- Phụ: người dùng gửi báo cáo, người bán, người mua.

## 3. Điều kiện kích hoạt
Có báo cáo từ người dùng, tin bị gắn cờ, cảnh báo cụm tài khoản bất thường, hoặc đến kỳ báo cáo cuối ngày.

## 4. Kết quả mong muốn và giá trị kinh doanh
- Báo cáo gian lận, hàng giả có mã vụ việc, người phụ trách, cách tạm xử lý (FR-34, BR-31, TC-89).
- Ẩn tin, khóa tài khoản có lý do, thông báo người bán, có nhật ký (TC-90); khóa quyền đặt giá không tự sửa lượt giá cũ (TC-91).
- Phát hiện cụm bất thường: tài khoản mới đặt giá sát giờ, cùng thiết bị, cùng SĐT hoặc địa chỉ giao hàng; phiên nghi ngờ tạm dừng, không tự hủy kết quả (01b mục 11, TC-94, TC-95).
- Mọi thay đổi trọng yếu có nhật ký tác nhân, thời điểm, trước và sau, lý do (FR-36, TC-92); báo cáo cuối ngày (FR-37, TC-93).

## 5. Khác biệt giữa tầng A và tầng B
Không khác về luồng. Tầng B thêm báo cáo liên quan tiền (thanh toán, hoàn, tranh chấp).

## 6. Danh sách UC con

| UC | Tên |
|---|---|
| SUC-13-01 | Gửi và tiếp nhận báo cáo tin, người dùng, hành vi đặt giá |
| SUC-13-02 | Kiểm duyệt: ẩn, gỡ tin |
| SUC-13-03 | Khóa hoặc hạn chế tài khoản |
| SUC-13-04 | Phát hiện và xử lý đặt giá ảo ở mức thủ công |
| SUC-13-05 | Báo cáo vận hành hằng ngày |
| SUC-13-06 | Tra cứu nhật ký thay đổi |

## 7. Truy vết
FR-09, FR-34 đến FR-37 · BR-02, BR-03, BR-20, BR-31, BR-32 · P-20 · 01b mục 11 · TC-89 đến TC-95.

## 8. Điểm còn mở
- Mục 11 của 01b cần PO duyệt và được thêm thành BR (hiện BR-03 chỉ chặn người bán tự đặt giá).
- Tiêu chí can thiệp, hủy kết quả, kháng nghị (ma trận ngoại lệ 02 mục 6).
- Số nhân sự vận hành và quyền hạn từng người (D-07).
