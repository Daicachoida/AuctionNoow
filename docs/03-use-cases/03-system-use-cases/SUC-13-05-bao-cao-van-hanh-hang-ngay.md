# SUC-13-05 — Báo cáo vận hành hằng ngày

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-13-05 / BUC-13 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Vận hành |
| Tác nhân phụ | Người dùng gửi báo cáo; các bên liên quan |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **báo cáo vận hành hằng ngày** trong BUC-13. Mục tiêu nghiệp vụ: có báo cáo kỳ với định nghĩa chỉ số nhất quán.

## 2. Tiền điều kiện

- Đến kỳ báo cáo và vận hành có quyền.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Hệ thống tổng hợp số phiên mở, kết thúc, có giá và có người thắng.
2. Hệ thống tổng hợp giao dịch, hủy, tranh chấp và trạng thái tiền theo tầng.
3. Định nghĩa tử số, mẫu số và ngày ghi nhận phải khớp 01/01b; trạng thái tự khai tầng A tách khỏi thanh toán đã đối soát.
4. Vận hành mở báo cáo và kiểm tra mốc thời gian.
5. Báo cáo phải cho truy lại các giao dịch cấu thành, phục vụ kiểm tra sai lệch.
6. Hệ thống cho truy vết số liệu về bản ghi nguồn.

## 4. Luồng thay thế

- Tầng A không tính lời tự khai là thanh toán thành công.
- Không có phiên trong ngày: hiển thị 0 và định nghĩa kỳ, không báo lỗi.
- Có đối soát tiền chưa xong: đánh dấu số liệu tạm thời.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Nguồn dữ liệu thiếu hoặc đối soát lệch | đánh dấu chưa hoàn chỉnh thay vì báo số chắc chắn. | TC-93 |
| Giao dịch bị ghi hai lần do sự kiện trùng | Loại trùng theo bản ghi chính thức. | Chưa có TC riêng |
| Dữ liệu nhật ký không đầy đủ | Cảnh báo báo cáo chưa hoàn chỉnh cho vận hành. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Có báo cáo kỳ với định nghĩa chỉ số nhất quán.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Biện pháp vận hành cần quyền, lý do, trước/sau và nhật ký (FR-35, FR-36).
- Tín hiệu đặt giá ảo chỉ đưa vào xem xét thủ công; không tự hủy phiên (01b mục 11).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-22; 01b mục 8.

## 8. Truy vết

FR-37; BR-22; 01 mục 8; 01b mục 8; TC-93. BUC-13; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Kỳ đo, ngưỡng mục tiêu và quyền xuất báo cáo chưa chốt.
- Quyền vận hành, ngưỡng can thiệp và mục chống đặt giá ảo thủ công cần PO duyệt.

