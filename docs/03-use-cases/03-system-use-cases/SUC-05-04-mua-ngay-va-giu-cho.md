# SUC-05-04 — Mua ngay và giữ chỗ

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-05-04 / BUC-05 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Người mua |
| Tác nhân phụ | Người bán; vận hành; đối tác thanh toán ở tầng B |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **mua ngay và giữ chỗ** trong BUC-05. Mục tiêu nghiệp vụ: một lô chỉ có một kết quả bán; ở tầng B, giữ chỗ thất bại có lịch sử.

## 2. Tiền điều kiện

- Phiên đang mở, mua ngay bật và chưa có giá hợp lệ.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Người mua xem giá mua ngay, tổng phí và xác nhận.
2. Hệ thống xét lại tính khả dụng cùng lúc với nhận giá.
3. Yêu cầu mua ngay cạnh tranh cùng thứ tự chính thức với lượt đặt giá đầu tiên để chỉ một nhánh thắng.
4. Tầng A: nếu hợp lệ, chốt ngay một giao dịch thử nghiệm; hai bên tự thanh toán ngoài nền tảng và hệ thống không xác nhận tiền.
5. Tầng B: nếu hợp lệ, khóa lô độc quyền 10 phút, tạm dừng phiên và chỉ chốt khi đối tác xác nhận thanh toán trong hạn.
6. Ở tầng B, khi giữ chỗ hết hạn, phục hồi đúng thời gian còn lại trước giữ chỗ nhưng tối thiểu 2 phút, lưu lần thất bại của tài khoản (P-10).

## 4. Luồng thay thế

- Hai người cùng mua ngay: chỉ một kết quả bán được tạo; người còn lại thấy hết khả dụng.
- Tầng B: người mua hủy trước hạn thì xử lý theo quy tắc giữ chỗ được duyệt, không tự chốt bán.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Có giá hợp lệ trước hoặc người khác đã mua ngay | Từ chối; nếu tầng B hết hạn giữ chỗ thì mở lại với ít nhất 2 phút còn lại. | TC-50 đến TC-56, TC-109, TC-114 |
| Tầng B: thanh toán chỉ quay về trang thành công | Không coi đã trả, chờ đối tác xác nhận. | Chưa có TC riêng |
| Tầng B: giữ chỗ thất bại lần thứ hai của cùng tài khoản | Từ chối theo P-10, nếu được duyệt. | TC-56 |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Một lô chỉ có một kết quả bán; ở tầng A không xác nhận tiền, ở tầng B giữ chỗ thất bại có lịch sử.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Chỉ lượt giá đã được ghi bền vững mới làm đổi người dẫn đầu (BR-14).
- Giờ máy chủ và thứ tự ghi nhận chính thức phân xử cạnh tranh giá/mua ngay (BR-12, BR-15, BR-36).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-35 đến BR-37; P-10.

## 8. Truy vết

FR-38 đến FR-40; BR-35 đến BR-37; P-10; TC-50 đến TC-56, TC-109, TC-114; BUC-05.

## 9. Điểm còn mở

- P-10 chưa duyệt cho tầng B; tầng A chốt giao dịch thử nghiệm ngay, không chờ hoặc xác nhận thanh toán ngoài nền tảng.
- Bước giá, giữ chỗ mua ngay và tiền đặt trước chỉ là tham số đề xuất; phải cập nhật TC khi PO chốt.

