# SUC-08-03 — Hạn chế tài khoản tái phạm

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-08-03 / BUC-08 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[B]` |
| Tác nhân chính | Vận hành |
| Tác nhân phụ | Người thắng, người bán; đối tác thanh toán ở tầng B |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **hạn chế tài khoản tái phạm** trong BUC-08. Mục tiêu nghiệp vụ: quyền đặt giá bị hạn chế theo quyết định có thể kiểm tra.

## 2. Tiền điều kiện

- Có lịch sử bỏ thanh toán đã xác minh.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Vận hành xem số vụ và bằng chứng.
2. Vận hành đối chiếu ngưỡng xử lý đã công bố.
3. Quyết định hạn chế chỉ tác động hành động mới; lượt giá và kết quả cũ cần xem xét riêng.
4. Vận hành áp dụng hạn chế có thời hạn và lý do.
5. Lưu số lần vi phạm, căn cứ, thời hạn và người quyết định để xử lý kháng nghị.
6. Hệ thống thông báo và lưu đường kháng nghị.

## 4. Luồng thay thế

- Tầng A chỉ đo tỷ lệ bỏ, không áp chế tài tiền; hạn chế ở tầng A cần quyết định riêng.
- Người dùng hoàn thành thời hạn hạn chế: mở lại quyền nếu không còn điều kiện khóa khác.
- Kháng nghị được chấp nhận: gỡ hạn chế bằng sự kiện mới, giữ lịch sử.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Không đủ căn cứ hoặc người thao tác không có quyền | không khóa. | Chưa có TC |
| Vi phạm chưa đối soát | Không tính thành tái phạm chắc chắn. | Chưa có TC riêng |
| Khóa đang ảnh hưởng phiên có người này dẫn đầu | Chuyển vận hành xét, không tự đổi người thắng. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Quyền đặt giá bị hạn chế theo quyết định có thể kiểm tra.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Quá hạn không tự trao quyền mua cho người trả giá kế tiếp (FR-24).
- Mất tiền đặt trước chỉ theo quy tắc công bố trước và sau cổng pháp lý/đối tác (BR-40, BR-41).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-02, BR-23; P-07, P-20; D-08.

## 8. Truy vết

FR-35; BR-02, BR-23; P-07, P-20; D-08. BUC-08; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Ngưỡng tái phạm, thời hạn khóa và quyền kháng nghị chưa chốt.
- Hạn trả, người nhận khoản đặt trước bị mất và chế tài tái phạm thuộc D-08.

