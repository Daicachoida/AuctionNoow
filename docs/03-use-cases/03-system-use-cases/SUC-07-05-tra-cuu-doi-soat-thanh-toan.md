# SUC-07-05 — Tra cứu, đối soát thanh toán

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-07-05 / BUC-07 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Vận hành |
| Tác nhân phụ | Người bán; vận hành; đối tác thanh toán ở tầng B |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **tra cứu, đối soát thanh toán** trong BUC-07. Mục tiêu nghiệp vụ: có hồ sơ đối soát và dấu vết xử lý lệch.

## 2. Tiền điều kiện

- Vận hành có quyền xem giao dịch và nhật ký.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Vận hành tìm giao dịch hoặc mã tham chiếu.
2. Hệ thống hiển thị trạng thái giao dịch, nguồn xác nhận và lịch sử sự kiện.
3. Vận hành phải thấy luồng đặt trước, phần còn lại, giữ tiền, giải ngân và hoàn như các khoản riêng.
4. Vận hành so với dữ liệu đối tác ở tầng B hoặc lời khai ở tầng A.
5. Bất kỳ điều chỉnh tài chính nào cũng phải đi qua sự kiện nghiệp vụ/đối tác, không sửa trực tiếp giá chốt hoặc bản ghi gốc.
6. Vận hành ghi kết quả đối soát và mở vụ ngoại lệ nếu lệch.

## 4. Luồng thay thế

- Tầng A chỉ ghi chưa đối soát nếu không có nguồn đáng tin.
- Đối tác có khoản dư: mở vụ xử lý dư tiền theo hợp đồng.
- Tầng A có hai lời khai mâu thuẫn: đánh dấu tranh chấp, không tự đối soát thành công.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Không đủ quyền hoặc số tiền lệch | không sửa trực tiếp giá chốt hay đánh dấu đã trả tùy tiện. | TC-59, TC-61 đến TC-63 |
| Mã tham chiếu trùng nhiều giao dịch | Chặn xác nhận tự động và rà gian lận. | Chưa có TC riêng |
| Thiếu quyền xem dữ liệu thanh toán | Ẩn trường nhạy cảm và ghi yêu cầu truy cập nếu cần. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Có hồ sơ đối soát và dấu vết xử lý lệch.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Lời khai hoặc trang quay về không đủ xác nhận đã thanh toán (BR-22).
- Đã trả, đang giữ, đã giải ngân và đã hoàn phải được theo dõi riêng (FR-22, BR-38).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-21, BR-22, BR-38.

## 8. Truy vết

FR-25, FR-36; BR-21, BR-22, BR-38; TC-59, TC-61 đến TC-63. BUC-07; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Quyền vận hành và quy trình xử lý thiếu, thừa, chargeback chưa chốt.
- Đối tác thanh toán, nguồn xác nhận và cách đối soát thiếu/thừa tiền thuộc cổng D-04.

