# SUC-12-02 — Xem uy tín công khai

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-12-02 / BUC-12 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Người dùng |
| Tác nhân phụ | Vận hành xử lý đánh giá vi phạm |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **xem uy tín công khai** trong BUC-12. Mục tiêu nghiệp vụ: người xem có tín hiệu uy tín có thể kiểm tra nguồn tổng hợp.

## 2. Tiền điều kiện

- Hồ sơ có dữ liệu uy tín được phép công khai.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Người xem mở hồ sơ người bán hoặc mua.
2. Hệ thống tổng hợp đánh giá từ giao dịch đủ điều kiện.
3. Điểm tổng hợp phải chỉ dùng đánh giá đủ điều kiện, loại bản bị gỡ và nêu số lượng đánh giá.
4. Hệ thống loại đánh giá đang bị ẩn.
5. Hồ sơ xác minh và điểm uy tín là hai dữ liệu khác nhau, không diễn giải là bảo đảm hàng thật.
6. Hệ thống hiển thị điểm, số lượng và trạng thái xác minh không lộ dữ liệu nhạy cảm.

## 4. Luồng thay thế

- Chưa có đánh giá: hiển thị chưa đủ dữ liệu thay vì điểm mặc định gây hiểu nhầm.
- Đánh giá mới đang ẩn do tranh chấp: không tính vào điểm công khai.
- Người bán chưa có giao dịch: hiển thị chưa có đánh giá.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Hồ sơ bị hạn chế hoặc yêu cầu dữ liệu riêng | chỉ trả phần công khai. | Chưa có TC |
| Yêu cầu xem nhận xét đã bị gỡ | Không trả nội dung vi phạm. | Chưa có TC riêng |
| Dữ liệu tính điểm bị thiếu | Hiển thị trạng thái chưa cập nhật, không đoán điểm. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Người xem có tín hiệu uy tín có thể kiểm tra nguồn tổng hợp.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Mỗi bên đánh giá một lần trên giao dịch hoàn tất trong hạn đề xuất (BR-29, P-18).
- Thông tin uy tín công khai không tiết lộ dữ liệu xác minh gốc (BR-30).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-29, BR-30; P-18.

## 8. Truy vết

FR-05, FR-33; BR-29, BR-30; P-18. BUC-12; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Công thức điểm và cách hiển thị số đánh giá ít chưa chốt.
- Công thức điểm uy tín, nội dung vi phạm và cách chống đánh giá thao túng chưa chốt.

