# SUC-06-01 — Đóng phiên, xác định người thắng

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-06-01 / BUC-06 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Hệ thống |
| Tác nhân phụ | Người mua, người bán; vận hành |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **đóng phiên, xác định người thắng** trong BUC-06. Mục tiêu nghiệp vụ: phiên có đúng một người thắng hoặc kết quả không bán được.

## 2. Tiền điều kiện

- Đã tới giờ đóng hiện hành và phiên còn đang mở.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Hệ thống khóa nhận lượt giá mới theo thời điểm máy chủ.
2. Hệ thống kiểm tra lần cuối giờ đóng sau mọi gia hạn.
3. Tiến trình đóng phải kiểm tra không còn gia hạn mới trước khi khóa; nếu một lượt hợp lệ vừa gia hạn, hẹn lại theo giờ đóng mới.
4. Hệ thống lấy lượt hợp lệ dẫn đầu và ghi một kết quả chính thức.
5. Bản ghi kết quả lưu người thắng, giá, lượt nguồn, thời điểm và phiên bản quy tắc; tạo giao dịch tách theo SUC-06-03.
6. Hệ thống lưu bằng chứng và chuyển sang SUC-06-03.

## 4. Luồng thay thế

- Nếu không có giá hợp lệ: SUC-06-02; mua ngay là nhánh kết thúc riêng ở SUC-05-04.
- Giá đến cùng lúc với đóng: thứ tự ghi nhận thành công quyết định; không dùng giờ thiết bị.
- Phiên đã có kết quả: trả kết quả cũ cho tiến trình chạy lặp.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Tiến trình chạy lặp hoặc giá đến sau mốc đóng | không tạo kết quả thứ hai. | TC-35, TC-42, TC-44 |
| Hai tiến trình cùng đóng | Chỉ một bản ghi kết quả chính thức. | Chưa có TC riêng |
| Lượt giá đã xác nhận mà bản ghi kết quả không thấy | Tạm dừng chốt và báo vận hành, không công bố sai. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Phiên có đúng một người thắng hoặc kết quả không bán được.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Một phiên có tối đa một kết quả chính thức; chạy lặp không tạo người thắng hay giao dịch mới (BR-19).
- Không có giá bảo lưu; nếu không có giá hợp lệ thì không có người thắng (BR-18).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-12, BR-17 đến BR-19.

## 8. Truy vết

FR-17, FR-18; BR-12, BR-17 đến BR-19; TC-35, TC-42, TC-44. BUC-06; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Cách lưu bằng chứng và thời hạn giữ chưa chốt.
- Cách lưu bằng chứng, lưu bao lâu và xử lý phiên không bán được cần được chốt.

