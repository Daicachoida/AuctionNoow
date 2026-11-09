# SUC-04-02 — Xem chi tiết tin

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-04-02 / BUC-04 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Khách, người mua |
| Tác nhân phụ | Người bán có tin công khai |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **xem chi tiết tin** trong BUC-04. Mục tiêu nghiệp vụ: người xem có thông tin trước khi quyết định.

## 2. Tiền điều kiện

- Tin được phép công khai.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Người xem mở tin.
2. Hệ thống hiển thị ảnh, mô tả, tình trạng, khiếm khuyết và hồ sơ người bán công khai.
3. Trang phải hiển thị rõ phí vận chuyển và chính sách trả hàng trước hành động đặt giá.
4. Hệ thống hiển thị giá, mốc thời gian, phí, vận chuyển và quy tắc phiên.
5. Giờ đóng hiển thị là giờ hiện hành đã tính gia hạn, kèm trạng thái tin/phiên; dữ liệu máy chủ là chuẩn.
6. Người xem có thể chuyển sang đặt giá hoặc mua ngay nếu đủ điều kiện.

## 4. Luồng thay thế

- Người chưa đăng nhập vẫn xem được và được hướng dẫn đăng nhập khi giao dịch.
- Phiên đã kết thúc: vẫn xem thông tin được phép nhưng không đặt giá.
- Tin có mua ngay nhưng đã có giá: ẩn lựa chọn mua ngay.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Tin bị gỡ hoặc không công khai | không hiển thị dữ liệu giao dịch như tin đang bán. | TC-23 |
| Tin bị ẩn sau khi trang đang mở | Khi thực hiện giao dịch, hệ thống kiểm tra lại và từ chối. | Chưa có TC riêng |
| Dữ liệu người bán nhạy cảm | Không đưa vào giao diện hoặc phản hồi cho khách. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Người xem có thông tin trước khi quyết định.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Chỉ tin đã duyệt và đang hiển thị được trả về cho khách (FR-10).
- Thông tin công khai không gồm giấy tờ hoặc dữ liệu riêng của người bán (BR-30).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-08, BR-30.

## 8. Truy vết

FR-05, FR-10, FR-13; BR-08, BR-30; TC-23. BUC-04; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Chuẩn hiển thị bằng chứng xác thực và phí cuối cùng chưa chốt.
- Thứ tự tìm kiếm/đề xuất và phạm vi dữ liệu hành vi cần được chốt nếu mở rộng ngoài MVP.

