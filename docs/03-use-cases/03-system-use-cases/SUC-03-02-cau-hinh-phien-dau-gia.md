# SUC-03-02 — Cấu hình phiên đấu giá

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-03-02 / BUC-03 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Người bán |
| Tác nhân phụ | Vận hành; người mua chịu ảnh hưởng |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **cấu hình phiên đấu giá** trong BUC-03. Mục tiêu nghiệp vụ: cấu hình phiên nằm trong bản nháp, chưa mở nhận giá.

## 2. Tiền điều kiện

- Có bản nháp tin hợp lệ.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Người bán chọn giá khởi điểm, thời lượng và lịch mở.
2. Hệ thống hiển thị 3, 5 hoặc 7 ngày cùng bước giá đề xuất.
3. Hệ thống tính trước thời điểm đóng dự kiến theo thời lượng và múi giờ hiển thị; mọi xét ranh giới dùng giờ máy chủ.
4. Người bán tùy chọn giá mua ngay nếu tính năng được bật.
5. Giá mua ngay, nếu có, được kiểm tra với giá khởi điểm và bước giá hiện hành rồi chụp cùng quy tắc phiên.
6. Hệ thống kiểm tra giá, thời gian và lưu cấu hình.

## 4. Luồng thay thế

- Không bật mua ngay: phiên chỉ nhận đặt giá thủ công.
- Thay thời lượng khi chưa có giá: tính lại lịch và cho xem trước trước khi lưu.
- Không chọn mua ngay: không hiển thị nhánh giữ chỗ ở trang phiên.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Giá dưới 10.000 VND, sai bội số hoặc mua ngay dưới mức tối thiểu | từ chối cấu hình. | Chưa có TC |
| Thời điểm mở nằm trong quá khứ hoặc đóng trước mở | Từ chối cấu hình thời gian. | Chưa có TC riêng |
| Giá không đúng bội số VND | Báo lỗi giá; chưa gửi duyệt. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Cấu hình phiên nằm trong bản nháp, chưa mở nhận giá.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Tin thiếu trường, hàng bị cấm hoặc chưa duyệt không thể mở phiên (BR-06).
- Thông tin trọng yếu sau lượt giá đầu tiên phải giữ lịch sử và được vận hành xử lý (BR-09).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-08, BR-35; P-05, P-06, P-10.

## 8. Truy vết

FR-12, FR-38; BR-08, BR-35; P-05, P-06, P-10. BUC-03; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- P-05, P-06, P-10 và việc bật mua ngay trong MVP chờ PO.
- Danh mục cấm, trường bắt buộc và quy trình sửa nội dung trọng yếu cần được duyệt trước khi mở tin công khai.

