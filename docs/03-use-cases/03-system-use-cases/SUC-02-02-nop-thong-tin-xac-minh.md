# SUC-02-02 — Nộp thông tin xác minh

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-02-02 / BUC-02 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Người bán |
| Tác nhân phụ | Vận hành; dịch vụ xác minh nếu được chọn |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **nộp thông tin xác minh** trong BUC-02. Mục tiêu nghiệp vụ: hồ sơ chờ vận hành hoặc dịch vụ xác minh xét duyệt.

## 2. Tiền điều kiện

- Có hồ sơ người bán chưa xác minh hoặc cần xác minh lại.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Người bán xem danh sách thông tin cần nộp theo loại.
2. Người bán cung cấp thông tin và bằng chứng.
3. Tài liệu nộp được lưu trong vùng giới hạn quyền; người mua chỉ có thể thấy trạng thái xác minh sau khi duyệt.
4. Hệ thống kiểm tra đủ trường và ghi nhận bản nộp.
5. Hệ thống gắn lần nộp với phiên bản yêu cầu xác minh để vận hành biết đã xét theo quy tắc nào.
6. Hồ sơ chuyển sang đang xét, hiển thị thời gian dự kiến.

## 4. Luồng thay thế

- Bổ sung sau yêu cầu sửa: tạo lần nộp mới, giữ lịch sử lần trước.
- Người bán nộp bổ sung theo yêu cầu: giữ lần nộp cũ và lý do bổ sung.
- Người bán rút hồ sơ đang xét: chuyển theo quy trình, quyền bán vẫn chưa mở.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Thiếu dữ liệu hoặc tệp không hợp lệ | báo lỗi theo trường, không mở quyền bán. | TC-08, TC-09 |
| Thiếu giấy tờ bắt buộc | Báo theo trường, không chuyển sang đang xét. | Chưa có TC riêng |
| Tệp không đọc được hoặc nghi không an toàn | Từ chối tệp và yêu cầu nộp lại. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Hồ sơ chờ vận hành hoặc dịch vụ xác minh xét duyệt.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Chỉ hồ sơ xác minh đạt mới mở quyền bán; dữ liệu giấy tờ không công khai (BR-04, BR-30).
- Tầng A chỉ mở cá nhân và shop nếu M-S1 được PO duyệt.
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-04, BR-30.

## 8. Truy vết

FR-03, FR-04; BR-04, BR-30; TC-08, TC-09. BUC-02; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Trường xác minh, CCCD ở tầng A và thời gian xét chưa chốt.
- Trường xác minh, thời hạn hiệu lực và thẩm quyền duyệt phụ thuộc quy trình xác minh được phê duyệt.

