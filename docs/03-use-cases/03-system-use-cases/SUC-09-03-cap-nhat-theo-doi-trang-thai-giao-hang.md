# SUC-09-03 — Cập nhật, theo dõi trạng thái giao hàng

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-09-03 / BUC-09 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Hệ thống, nhà vận chuyển |
| Tác nhân phụ | Người mua; vận hành; nhà vận chuyển ở tầng B |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **cập nhật, theo dõi trạng thái giao hàng** trong BUC-09. Mục tiêu nghiệp vụ: lịch sử giao có nguồn phân biệt tự khai và xác minh.

## 2. Tiền điều kiện

- Có giao dịch đang vận chuyển.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Hệ thống nhận trạng thái cùng nguồn và thời điểm.
2. Hệ thống kiểm tra chuyển trạng thái hợp lệ và lưu lịch sử.
3. Từng trạng thái vận chuyển phải có thời điểm nguồn gửi và thời điểm hệ thống nhận để xử lý cập nhật muộn.
4. Người mua, người bán theo dõi tiến trình.
5. Trạng thái giao thành công ở tầng B mở mốc 15 ngày; tự khai tầng A cần vận hành xác minh riêng trước đóng thử nghiệm.
6. Tầng B chỉ bắt đầu cửa sổ 15 ngày khi giao được xác minh.

## 4. Luồng thay thế

- Tầng A người bán tự khai đã giao nhưng không tự bắt đầu 15 ngày; vận hành có thể kiểm tra bằng chứng.
- Nhà vận chuyển sửa trạng thái giao thành công thành giao thất bại: mở ngoại lệ, không âm thầm hoàn tất.
- Người bán khai đã giao ở tầng A: gắn nhãn chưa đối soát.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Cập nhật trùng, ngược hoặc không rõ nguồn | lưu đối soát, không chuyển trạng thái sai. | TC-71, TC-72 |
| Sự kiện vận chuyển trùng | Không tạo mốc giao hoặc cửa sổ 15 ngày lần hai. | Chưa có TC riêng |
| Nguồn gửi không xác thực | Lưu để điều tra, không thay trạng thái chính thức. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Lịch sử giao có nguồn phân biệt tự khai và xác minh.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Mọi trạng thái giao hàng có nguồn và thời điểm; tự khai khác xác nhận của nhà vận chuyển (BR-25).
- Địa chỉ chỉ hiển thị cho vai trò cần dùng (FR-26).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-25, BR-26; P-13, P-15.

## 8. Truy vết

FR-27 đến FR-29; BR-25, BR-26; P-13, P-15; TC-71, TC-72. BUC-09; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Tiêu chí xác minh giao ở tầng A và tích hợp nhà vận chuyển chưa chốt.
- Nguồn xác minh giao hàng, đơn vị vận chuyển và trách nhiệm khi giao thất bại cần được chốt.

