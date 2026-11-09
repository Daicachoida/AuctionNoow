# SUC-03-05 — Sửa tin theo trạng thái cho phép

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-03-05 / BUC-03 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Người bán, vận hành |
| Tác nhân phụ | Vận hành; người mua chịu ảnh hưởng |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **sửa tin theo trạng thái cho phép** trong BUC-03. Mục tiêu nghiệp vụ: lịch sử nội dung được giữ; quy tắc đã chụp không bị ghi đè.

## 2. Tiền điều kiện

- Tin thuộc người bán.
- Trạng thái cho phép sửa.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Người bán yêu cầu sửa tin.
2. Hệ thống kiểm tra trạng thái và đã có giá hợp lệ hay chưa.
3. Hệ thống so sánh trường trước/sau để xác định thay đổi có ảnh hưởng quyết định đặt giá hay không.
4. Hệ thống cho sửa trường được phép, lưu phiên bản mới.
5. Nếu vận hành cho sửa theo chính sách, bản cũ, lý do, thời điểm và thông báo tới người đã đặt giá phải được giữ.
6. Nếu ảnh hưởng người tham gia, vận hành xem xét và thông báo.

## 4. Luồng thay thế

- Trước giá đầu tiên có thể sửa nội dung không ảnh hưởng giá; sau đó sai sót trọng yếu chuyển sang BUC-14.
- Sửa lỗi chính tả không trọng yếu trước giá đầu: lưu phiên bản mới.
- Sau giá đầu, phát hiện ảnh khác hàng thực: tạm dừng phiên để vận hành xét BUC-14.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Tự đổi giá khởi điểm hoặc mô tả trọng yếu sau giá đầu tiên | từ chối. | TC-20, TC-21 |
| Người bán sửa trực tiếp giá sau giá đầu | Từ chối, không đổi quy tắc phiên. | Chưa có TC riêng |
| Hai bản sửa cạnh tranh | Yêu cầu tải lại phiên bản mới, tránh ghi đè. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Lịch sử nội dung được giữ; quy tắc đã chụp không bị ghi đè.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Tin thiếu trường, hàng bị cấm hoặc chưa duyệt không thể mở phiên (BR-06).
- Thông tin trọng yếu sau lượt giá đầu tiên phải giữ lịch sử và được vận hành xử lý (BR-09).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-09, BR-10; P-04.

## 8. Truy vết

FR-11; BR-09, BR-10; P-04; TC-20, TC-21. BUC-03; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Danh sách trường trọng yếu và quy trình xử lý sai sót cần chốt.
- Danh mục cấm, trường bắt buộc và quy trình sửa nội dung trọng yếu cần được duyệt trước khi mở tin công khai.

