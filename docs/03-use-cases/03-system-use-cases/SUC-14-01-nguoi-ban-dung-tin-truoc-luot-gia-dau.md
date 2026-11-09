# SUC-14-01 — Người bán dừng tin trước lượt giá đầu

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-14-01 / BUC-14 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Người bán |
| Tác nhân phụ | Người đặt giá; người bán; đối tác thanh toán ở tầng B |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **người bán dừng tin trước lượt giá đầu** trong BUC-14. Mục tiêu nghiệp vụ: tin dừng không tạo người thắng hay giao dịch.

## 2. Tiền điều kiện

- Tin thuộc người bán và chưa có lượt giá hợp lệ.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Người bán chọn dừng và nêu lý do.
2. Hệ thống kiểm tra lại lịch sử giá cùng trạng thái tin.
3. Kiểm tra không có giá hợp lệ phải thực hiện ở trạng thái chính thức ngay lúc xác nhận dừng, tránh cạnh tranh với lượt mới.
4. Hệ thống dừng tin hoặc phiên chưa có giá, lưu lý do.
5. Lý do dừng và thời điểm phải công khai phù hợp, nhưng không tiết lộ dữ liệu riêng.
6. Hệ thống cập nhật trang công khai.

## 4. Luồng thay thế

- Nếu tin đang chờ mở, không mở phiên về sau.
- Tin chờ mở: hủy lịch mở và giữ lịch sử tin.
- Phiên đang mở chưa có giá: khóa nhận giá rồi công bố dừng.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Có giá hợp lệ trước khi xác nhận dừng | từ chối, hướng sang vận hành. | TC-47, TC-48 |
| Lượt giá hợp lệ ghi trước yêu cầu dừng | Từ chối tự dừng, chuyển vận hành. | Chưa có TC riêng |
| Đang giữ chỗ mua ngay | Không tự dừng; xử lý quyền giữ chỗ trước. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Tin dừng không tạo người thắng hay giao dịch.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Dừng/hủy sau giá đầu phải do vận hành có căn cứ; lượt giá cũ không tự thành giao dịch (BR-10, FR-19).
- Sự cố cần chính sách dừng, công bố và khôi phục (NFR-06).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-10; P-09.

## 8. Truy vết

FR-19; BR-10; P-09; TC-47, TC-48. BUC-14; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Trường hợp giữ chỗ mua ngay đang chạy cần quy tắc riêng.
- Quy tắc hoàn đặt trước khi hủy phiên, bù thời gian và kháng nghị chưa chốt.

