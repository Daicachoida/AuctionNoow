# SUC-08-01 — Nhắc, phát hiện quá hạn, hủy giao dịch

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-08-01 / BUC-08 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Hệ thống |
| Tác nhân phụ | Người thắng, người bán; đối tác thanh toán ở tầng B |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **nhắc, phát hiện quá hạn, hủy giao dịch** trong BUC-08. Mục tiêu nghiệp vụ: giao dịch quá hạn có kết quả rõ; người thứ hai không tự thắng.

## 2. Tiền điều kiện

- Giao dịch chưa có thanh toán đáng tin và đến mốc P-11.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Hệ thống nhắc người thắng tại mốc đề xuất 24 giờ.
2. Khi hết hạn đề xuất 48 giờ, hệ thống kiểm tra trạng thái đối soát mới nhất.
3. Trước khi hủy phải kiểm tra phản hồi đối tác đến gần hạn và các sự kiện đang chờ đối soát.
4. Nếu vẫn chưa trả, hệ thống hủy có lý do và thông báo hai bên.
5. Hủy có lý do, thời điểm và người/tiến trình thực hiện; không tự chuyển quyền mua cho người thứ hai.
6. Người bán được xem đường đăng lại sau rà soát.

## 4. Luồng thay thế

- Tầng A chỉ ghi nhận bỏ thanh toán thử nghiệm, không xử lý tiền.
- Người thắng thanh toán trước hạn nhưng xác nhận đến muộn: chuyển đối soát, chưa xử phạt tự động.
- Tầng A không có đối soát: chỉ ghi nhận bỏ theo tiêu chí thử nghiệm được duyệt.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Sự kiện đối tác đến muộn | không tự đảo trạng thái hủy, chuyển SUC-07-04. | TC-64, TC-65 |
| Thanh toán đã được đối tác xác nhận trước hạn | Không hủy vì bộ đếm cũ. | Chưa có TC riêng |
| Tiến trình quá hạn chạy lại | Không hủy hoặc gửi phạt lần hai. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Giao dịch quá hạn có kết quả rõ; người thứ hai không tự thắng.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Quá hạn không tự trao quyền mua cho người trả giá kế tiếp (FR-24).
- Mất tiền đặt trước chỉ theo quy tắc công bố trước và sau cổng pháp lý/đối tác (BR-40, BR-41).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-23; P-11.

## 8. Truy vết

FR-24; BR-23; P-11; TC-64, TC-65. BUC-08; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Hạn trả, cho mời người đặt giá kế tiếp và điều kiện đăng lại chưa chốt.
- Hạn trả, người nhận khoản đặt trước bị mất và chế tài tái phạm thuộc D-08.

