# SUC-09-01 — Xem thông tin giao hàng, hạn bàn giao

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-09-01 / BUC-09 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Người bán |
| Tác nhân phụ | Người mua; vận hành; nhà vận chuyển ở tầng B |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **xem thông tin giao hàng, hạn bàn giao** trong BUC-09. Mục tiêu nghiệp vụ: người bán biết việc phải làm mà dữ liệu riêng không lộ ngoài vai trò.

## 2. Tiền điều kiện

- Giao dịch đủ điều kiện giao theo tầng.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Người bán mở trang giao hàng.
2. Hệ thống kiểm tra quyền và nguồn xác nhận giao dịch.
3. Hạn bàn giao được tính từ mốc đủ điều kiện giao, không từ lúc phiên đóng; tầng B cần xác nhận tiền đang giữ.
4. Hệ thống hiển thị địa chỉ cần thiết, đơn vị vận chuyển và hạn bàn giao đề xuất 3 ngày làm việc.
5. Chỉ người bán liên quan và vai trò vận hành được phép mới xem địa chỉ giao hàng; truy cập cần dấu vết.
6. Người bán chuẩn bị gửi hàng.

## 4. Luồng thay thế

- Tầng A dùng xác nhận thử nghiệm, tầng B cần tiền đang giữ được đối tác xác nhận.
- Người mua đổi địa chỉ sau khi đã chốt: chuyển quy trình đồng ý riêng, không âm thầm sửa đơn.
- Tầng A có lời khai trả tiền: hiển thị là thử nghiệm, không gắn nhãn đã thanh toán.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Không đủ điều kiện hoặc sai người bán | không hiển thị địa chỉ. | TC-68 |
| Tiền tầng B chưa được xác nhận đang giữ | Không hiện địa chỉ để bắt đầu giao. | Chưa có TC riêng |
| Người bán bị mất quyền nhưng có giao dịch đang chạy | Chuyển vận hành xử lý nghĩa vụ hiện có. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Người bán biết việc phải làm mà dữ liệu riêng không lộ ngoài vai trò.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Mọi trạng thái giao hàng có nguồn và thời điểm; tự khai khác xác nhận của nhà vận chuyển (BR-25).
- Địa chỉ chỉ hiển thị cho vai trò cần dùng (FR-26).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-25, BR-30; P-13.

## 8. Truy vết

FR-26; BR-25, BR-30; P-13; TC-68. BUC-09; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Thời hạn P-13 và danh sách nhà vận chuyển chưa chốt.
- Nguồn xác minh giao hàng, đơn vị vận chuyển và trách nhiệm khi giao thất bại cần được chốt.

