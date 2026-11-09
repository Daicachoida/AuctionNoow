# SUC-14-03 — Xử lý lượt giá đã có, thông báo

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-14-03 / BUC-14 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Hệ thống |
| Tác nhân phụ | Người đặt giá; người bán; đối tác thanh toán ở tầng B |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **xử lý lượt giá đã có, thông báo** trong BUC-14. Mục tiêu nghiệp vụ: các bên thấy tác động, lịch sử không bị xóa.

## 2. Tiền điều kiện

- Phiên đã dừng hoặc hủy theo quyết định hợp lệ.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Hệ thống giữ nguyên lịch sử giá và đánh dấu không còn hiệu lực để tạo giao dịch.
2. Hệ thống xác định người đặt giá, người bán và người mua ngay bị ảnh hưởng.
3. Lịch sử giá phải giữ nguyên với dấu trạng thái sau dừng/hủy; không xóa chứng cứ để người dùng kiểm tra.
4. Hệ thống thông báo lý do và đường kháng nghị.
5. Tầng B cần xác định khoản đặt trước của từng người và chỉ hoàn/giải phóng theo quy tắc đã phê duyệt, qua đối tác.
6. Tầng B mở quy trình giải phóng đặt trước theo đối tác sau khi có quy tắc được duyệt.

## 4. Luồng thay thế

- Thông báo thất bại được gửi lại; kết quả chính thức vẫn tra cứu trên trang phiên.
- Có người đặt giá chưa nhận thông báo: trạng thái công khai vẫn hiển thị lý do dừng.
- Có kháng nghị: giữ hồ sơ và xét theo quy trình, không khôi phục phiên tự động.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Không tự chuyển lượt dẫn đầu thành giao dịch hoặc tự chi khoản đặt trước | Từ chối hoặc giữ trạng thái hiện hành; ghi lý do để người dùng hoặc vận hành xử lý. | TC-49 |
| Tiền đặt trước chưa có quy tắc hoàn khi hủy | Chặn lệnh tài chính và chuyển vận hành/pháp lý. | Chưa có TC riêng |
| Tiến trình thông báo chạy lặp | Không tạo giao dịch hoặc kết quả phiên mới. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Các bên thấy tác động, lịch sử không bị xóa.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Dừng/hủy sau giá đầu phải do vận hành có căn cứ; lượt giá cũ không tự thành giao dịch (BR-10, FR-19).
- Sự cố cần chính sách dừng, công bố và khôi phục (NFR-06).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-20, BR-40; P-09.

## 8. Truy vết

FR-19, FR-35; BR-20, BR-40; P-09; TC-49. BUC-14; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Quy tắc hoàn đặt trước khi hủy phiên, kháng nghị và giữ chỗ mua ngay chưa chốt.
- Quy tắc hoàn đặt trước khi hủy phiên, bù thời gian và kháng nghị chưa chốt.

