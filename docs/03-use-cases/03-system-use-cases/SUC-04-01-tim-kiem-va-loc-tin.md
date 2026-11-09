# SUC-04-01 — Tìm kiếm và lọc tin

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-04-01 / BUC-04 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Khách, người mua |
| Tác nhân phụ | Người bán có tin công khai |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **tìm kiếm và lọc tin** trong BUC-04. Mục tiêu nghiệp vụ: danh sách tìm kiếm chỉ chứa tin được phép công khai.

## 2. Tiền điều kiện

- Có trang tìm kiếm công khai.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Người xem nhập từ khóa hoặc chọn danh mục, trạng thái.
2. Hệ thống lọc tin đã duyệt, đang hiển thị.
3. Bộ lọc trạng thái phải dựa trạng thái công khai, không lấy nháp, chờ duyệt hoặc tin gỡ.
4. Hệ thống trả danh sách cùng giá và thời điểm phù hợp.
5. Kết quả nên hiển thị giá và giờ đóng hiện hành để người xem phân biệt phiên còn tham gia được.
6. Người xem mở tin cần xem.

## 4. Luồng thay thế

- Không có kết quả: hiển thị trạng thái rỗng và cho đổi bộ lọc.
- Đổi bộ lọc: thực hiện truy vấn mới mà không đổi trạng thái tin.
- Không có từ khóa: cho duyệt danh mục và trạng thái theo chính sách.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Tin bị ẩn, gỡ hoặc chưa duyệt | không xuất hiện. | TC-25 đến TC-28 |
| Tin bị gỡ trong lúc tìm | Không trả ở trang kết quả mới. | Chưa có TC riêng |
| Bộ lọc không hợp lệ | Báo lựa chọn hợp lệ, không hiển thị tin riêng. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Danh sách tìm kiếm chỉ chứa tin được phép công khai.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Chỉ tin đã duyệt và đang hiển thị được trả về cho khách (FR-10).
- Thông tin công khai không gồm giấy tờ hoặc dữ liệu riêng của người bán (BR-30).


## 8. Truy vết

FR-10; TC-25 đến TC-28. BUC-04; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Thứ tự sắp xếp và bộ lọc bổ sung chưa chốt.
- Thứ tự tìm kiếm/đề xuất và phạm vi dữ liệu hành vi cần được chốt nếu mở rộng ngoài MVP.

