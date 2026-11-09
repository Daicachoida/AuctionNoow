# SUC-04-03 — Đề xuất mặt hàng

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-04-03 / BUC-04 |
| Phiên bản / trạng thái | 0.2 / `Ngoài MVP — chờ PO` |
| Tầng | `Ngoài MVP` |
| Tác nhân chính | Hệ thống |
| Tác nhân phụ | Người bán có tin công khai |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **đề xuất mặt hàng** trong BUC-04. Mục tiêu nghiệp vụ: chỉ khi được duyệt mới có danh sách đề xuất. Chưa triển khai trong MVP hiện tại.

## 2. Tiền điều kiện

- PO phê duyệt phạm vi và có tin được phép công khai.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Hệ thống chọn tin theo tiêu chí được phê duyệt.
2. Hệ thống loại tin ẩn, gỡ hoặc đã hết khả dụng.
3. Bản đề xuất đơn giản chỉ dùng dữ liệu tin công khai; cá nhân hóa cần nguồn dữ liệu và cơ sở xử lý được duyệt.
4. Hệ thống hiển thị đề xuất và lý do cơ bản.
5. Thứ tự đề xuất, lý do gợi ý và cách loại tin hết hạn phải được kiểm thử trước phát hành.
6. Người xem có thể mở chi tiết tin.

## 4. Luồng thay thế

- Bản đơn giản có thể dùng cùng danh mục hoặc phiên sắp kết thúc; cá nhân hóa phải có yêu cầu mới.
- Không đủ tin phù hợp: hiển thị danh mục phổ biến nếu đã được duyệt.
- Người dùng tắt cá nhân hóa: không dùng lịch sử riêng để xếp hạng.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Chưa có quyết định PO hoặc cơ sở dữ liệu hợp lệ | không bật tính năng. | Chưa có TC |
| Chưa có FR được PO duyệt | Không triển khai vào MVP. | Chưa có TC riêng |
| Tin bị gỡ hoặc hết giờ trong lúc tính | Loại khỏi kết quả trước khi hiển thị. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Chỉ khi được duyệt mới có danh sách đề xuất.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Chỉ tin đã duyệt và đang hiển thị được trả về cho khách (FR-10).
- Thông tin công khai không gồm giấy tờ hoặc dữ liệu riêng của người bán (BR-30).
- Mã quy tắc/đề xuất liên quan trực tiếp: 01b mục 5.

## 8. Truy vết

01 mục 9.3; 01b mục 5; BUC-04. BUC-04; chưa có FR/TC được duyệt.

## 9. Điểm còn mở

- Chưa có FR hay TC; cần PO duyệt và rà BR-33 nếu dùng dữ liệu hành vi.
- Thứ tự tìm kiếm/đề xuất và phạm vi dữ liệu hành vi cần được chốt nếu mở rộng ngoài MVP.

