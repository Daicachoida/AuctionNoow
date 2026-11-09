# SUC-06-02 — Đóng phiên không có giá hợp lệ

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-06-02 / BUC-06 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Hệ thống |
| Tác nhân phụ | Người mua, người bán; vận hành |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **đóng phiên không có giá hợp lệ** trong BUC-06. Mục tiêu nghiệp vụ: phiên kết thúc không có người thắng.

## 2. Tiền điều kiện

- Đã tới giờ đóng và không có lượt giá hợp lệ.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Hệ thống khóa nhận giá.
2. Hệ thống xác nhận không có giá hợp lệ trong lịch sử chính thức.
3. Hệ thống phải xét cả lượt bị hủy bởi vận hành theo lịch sử hiệu lực, không chỉ đếm mọi lượt từng gửi.
4. Hệ thống ghi kết quả không bán được.
5. Kết quả không bán được phải giữ được nguyên nhân không có giá và lịch sử đóng phiên.
6. Hệ thống thông báo người bán, không tạo giao dịch.

## 4. Luồng thay thế

- Người bán có thể đăng lại sau quy trình được duyệt.
- Tin có người xem nhưng không đặt: vẫn không tạo người thắng.
- Người bán đăng lại: tạo phiên mới theo quy trình, không sửa kết quả cũ.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Tiến trình chạy lặp | giữ nguyên kết quả, không tạo giao dịch. | TC-43, TC-44 |
| Tiến trình đóng lặp | Không tạo thêm kết quả hay giao dịch. | Chưa có TC riêng |
| Có lượt hợp lệ xuất hiện trước mốc đóng nhưng chưa được phản ánh | Rà thứ tự sự kiện trước khi công bố không bán được. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Phiên kết thúc không có người thắng.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Một phiên có tối đa một kết quả chính thức; chạy lặp không tạo người thắng hay giao dịch mới (BR-19).
- Không có giá bảo lưu; nếu không có giá hợp lệ thì không có người thắng (BR-18).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-18, BR-19.

## 8. Truy vết

FR-17, FR-18; BR-18, BR-19; TC-43, TC-44. BUC-06; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Có tự đăng lại hay không chưa chốt.
- Cách lưu bằng chứng, lưu bao lâu và xử lý phiên không bán được cần được chốt.

