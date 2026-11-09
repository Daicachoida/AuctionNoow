# SUC-09-04 — Xử lý quá hạn gửi, giao thất bại

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-09-04 / BUC-09 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Hệ thống, vận hành |
| Tác nhân phụ | Người mua; vận hành; nhà vận chuyển ở tầng B |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **xử lý quá hạn gửi, giao thất bại** trong BUC-09. Mục tiêu nghiệp vụ: giao dịch ở trạng thái ngoại lệ có người phụ trách.

## 2. Tiền điều kiện

- Quá hạn bàn giao hoặc có trạng thái giao thất bại.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Hệ thống đánh dấu ngoại lệ và thông báo hai bên.
2. Người mua có thể mở yêu cầu theo SUC-11-01.
3. Quá hạn bàn giao phải dùng lịch ngày làm việc đã công bố và không tính từ tin đăng.
4. Vận hành kiểm tra vận đơn, bằng chứng và trách nhiệm.
5. Vận hành cần phân biệt chưa gửi, giao thất bại, hàng thất lạc và người mua không nhận để quyết định đúng nhánh.
6. Vận hành ghi hướng xử lý theo chính sách được duyệt.

## 4. Luồng thay thế

- Nếu giao lại được, lưu mốc và nguồn mới; nếu hủy, chuyển tranh chấp hoặc hoàn tiền ở tầng B.
- Người bán cung cấp bằng chứng gửi muộn: bổ sung hồ sơ, không xóa dấu quá hạn.
- Nhà vận chuyển giao lại thành công: cập nhật mốc giao mới từ nguồn đáng tin.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Không có bằng chứng | không tự ghi đã giao hoặc hoàn tất. | TC-70 |
| Không có mã theo dõi mà người bán tự khai đã gửi | Không coi hoàn tất nghĩa vụ. | Chưa có TC riêng |
| Người mua mở yêu cầu khi đang ngoại lệ | Cấp mã vụ, chặn hoàn tất theo chính sách. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Giao dịch ở trạng thái ngoại lệ có người phụ trách.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Mọi trạng thái giao hàng có nguồn và thời điểm; tự khai khác xác nhận của nhà vận chuyển (BR-25).
- Địa chỉ chỉ hiển thị cho vai trò cần dùng (FR-26).
- Mã quy tắc/đề xuất liên quan trực tiếp: P-13, P-16.

## 8. Truy vết

FR-27, FR-28, FR-32; P-13, P-16; TC-70. BUC-09; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Chi phí giao lại và trách nhiệm hàng hỏng, thất lạc chưa chốt.
- Nguồn xác minh giao hàng, đơn vị vận chuyển và trách nhiệm khi giao thất bại cần được chốt.

