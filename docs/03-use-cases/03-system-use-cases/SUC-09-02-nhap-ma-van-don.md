# SUC-09-02 — Nhập mã vận đơn

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-09-02 / BUC-09 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Người bán |
| Tác nhân phụ | Người mua; vận hành; nhà vận chuyển ở tầng B |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **nhập mã vận đơn** trong BUC-09. Mục tiêu nghiệp vụ: có mã vận đơn và nguồn trạng thái rõ ràng.

## 2. Tiền điều kiện

- Giao dịch chờ gửi và người bán có quyền.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Người bán chọn đơn vị được chấp nhận và nhập mã vận đơn.
2. Hệ thống kiểm tra định dạng, lưu mã và thời điểm.
3. Mã vận đơn cần gắn đúng giao dịch, nhà vận chuyển, thời điểm bàn giao và nguồn người bán khai.
4. Hệ thống ghi nguồn người bán khai, chuyển trạng thái đã bàn giao.
5. Việc nhập mã không được tự tạo trạng thái đã giao; cần nguồn vận chuyển hoặc kiểm tra thủ công.
6. Hệ thống thông báo người mua.

## 4. Luồng thay thế

- Tầng B chờ nhà vận chuyển xác nhận tiếp; tầng A tiếp tục hiển thị chưa đối soát.
- Người bán nhập sai trước khi bên vận chuyển xác nhận: cho sửa có lịch sử.
- Mã vận đơn đã dùng cho giao dịch khác: chuyển vận hành kiểm tra.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Mã thiếu hoặc sửa sau khi đã xác nhận | yêu cầu giải thích và lưu lịch sử. | TC-69 |
| Mã sai định dạng hoặc đơn vị không nằm danh sách | Không nhận như vận đơn hợp lệ. | Chưa có TC riêng |
| Người bán bấm lưu lặp | Chỉ một bản ghi trạng thái mới, giữ nguyên lịch sử. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Có mã vận đơn và nguồn trạng thái rõ ràng.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Mọi trạng thái giao hàng có nguồn và thời điểm; tự khai khác xác nhận của nhà vận chuyển (BR-25).
- Địa chỉ chỉ hiển thị cho vai trò cần dùng (FR-26).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-25; P-13.

## 8. Truy vết

FR-27, FR-28; BR-25; P-13; TC-69. BUC-09; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Chuẩn mã vận đơn và quyền sửa chưa chốt.
- Nguồn xác minh giao hàng, đơn vị vận chuyển và trách nhiệm khi giao thất bại cần được chốt.

