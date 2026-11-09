# SUC-13-04 — Phát hiện, xử lý đặt giá ảo thủ công

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-13-04 / BUC-13 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Vận hành |
| Tác nhân phụ | Người dùng gửi báo cáo; các bên liên quan |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **phát hiện, xử lý đặt giá ảo thủ công** trong BUC-13. Mục tiêu nghiệp vụ: có hồ sơ xem xét đặt giá ảo và biện pháp có lý do.

## 2. Tiền điều kiện

- Có cụm đặt giá bất thường hoặc báo cáo.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Hệ thống đánh dấu phiên có nhiều tài khoản mới đặt sát giờ hoặc tín hiệu liên quan.
2. Vận hành xem lịch sử giá, tài khoản, thiết bị và địa chỉ theo quyền.
3. Tín hiệu trùng thiết bị, SĐT hoặc địa chỉ cần được xem là dấu hiệu, không kết luận gian lận tự động.
4. Vận hành ghi nhận đánh giá rủi ro.
5. Vận hành phải rà vai trò người bán, chuỗi giá, thời điểm và quan hệ tài khoản trước khi tạm dừng.
6. Nếu cần, tạm dừng phiên theo BUC-14 và thông báo, không tự hủy kết quả.

## 4. Luồng thay thế

- Tín hiệu trùng SĐT hoặc địa chỉ chỉ kích hoạt kiểm tra, chưa chứng minh gian lận.
- Chỉ có nhiều tài khoản mới cùng đặt sát giờ: đánh dấu để xem xét.
- Có chứng cứ thông đồng: chuyển quy trình dừng/hủy và xử lý tài khoản.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Không đủ căn cứ | không hủy giá hoặc khóa tài khoản tự động. | TC-94, TC-95 |
| Trùng địa chỉ do cùng hộ gia đình | Không tự hủy giá. | Chưa có TC riêng |
| Không có quyền xem dữ liệu nhạy cảm | Chỉ hiển thị tín hiệu tổng hợp hoặc yêu cầu người có quyền. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Có hồ sơ xem xét đặt giá ảo và biện pháp có lý do.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Biện pháp vận hành cần quyền, lý do, trước/sau và nhật ký (FR-35, FR-36).
- Tín hiệu đặt giá ảo chỉ đưa vào xem xét thủ công; không tự hủy phiên (01b mục 11).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-03, BR-20; 01b mục 11.

## 8. Truy vết

FR-34 đến FR-36; BR-03, BR-20; 01b mục 11; TC-94, TC-95. BUC-13; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- M-D5 và BR mới cho quy tắc này chưa được duyệt.
- Quyền vận hành, ngưỡng can thiệp và mục chống đặt giá ảo thủ công cần PO duyệt.

