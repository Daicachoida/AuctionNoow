# SUC-06-03 — Tạo giao dịch, thông báo kết quả

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-06-03 / BUC-06 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Hệ thống |
| Tác nhân phụ | Người mua, người bán; vận hành |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **tạo giao dịch, thông báo kết quả** trong BUC-06. Mục tiêu nghiệp vụ: một kết quả bán có đúng một giao dịch có thể truy vết.

## 2. Tiền điều kiện

- Có kết quả thắng hợp lệ hoặc mua ngay đã chốt.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Hệ thống tạo một giao dịch gắn phiên, lô, người mua, người bán, giá và phiên bản điều kiện.
2. Hệ thống đánh dấu thử nghiệm nếu ở tầng A.
3. Giao dịch phải giữ giá chốt và phiên bản điều kiện, không tham chiếu động tới tin có thể đổi sau này.
4. Hệ thống thông báo hai bên.
5. Thông báo người thắng nêu số tiền và hạn trả; thông báo người bán nêu trạng thái chờ thanh toán, chưa phải đã bán hoàn tất.
6. Người thắng mở trang xem hạn và số tiền phải trả.

## 4. Luồng thay thế

- Sự kiện tạo lặp: trả về giao dịch đã có, không tạo thêm.
- Mua ngay đã chốt: nguồn kết quả là nhánh mua ngay, nhưng vẫn một giao dịch cho lô.
- Thông báo gửi lỗi: giao dịch vẫn tồn tại và trang kết quả tra cứu được.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Không có người thắng hoặc phiên bị hủy | không tạo giao dịch. | TC-42, TC-43, TC-44, TC-57, TC-58 |
| Tạo giao dịch lặp từ cùng phiên | Trả giao dịch đã có. | Chưa có TC riêng |
| Giá hoặc người thắng không khớp kết quả chính thức | Không tạo giao dịch, báo vận hành. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Một kết quả bán có đúng một giao dịch có thể truy vết.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Một phiên có tối đa một kết quả chính thức; chạy lặp không tạo người thắng hay giao dịch mới (BR-19).
- Không có giá bảo lưu; nếu không có giá hợp lệ thì không có người thắng (BR-18).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-19, BR-21.

## 8. Truy vết

FR-20, FR-21; BR-19, BR-21; TC-42, TC-43, TC-44, TC-57, TC-58. BUC-06; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Hạn thanh toán P-11 và chi phí cuối cùng cần chốt.
- Cách lưu bằng chứng, lưu bao lâu và xử lý phiên không bán được cần được chốt.

