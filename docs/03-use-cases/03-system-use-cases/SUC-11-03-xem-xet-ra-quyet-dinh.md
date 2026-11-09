# SUC-11-03 — Xem xét, ra quyết định

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-11-03 / BUC-11 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Vận hành |
| Tác nhân phụ | Người mua, người bán; đối tác thanh toán ở tầng B |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **xem xét, ra quyết định** trong BUC-11. Mục tiêu nghiệp vụ: quyết định có người chịu trách nhiệm và dấu vết tài chính nhất quán.

## 2. Tiền điều kiện

- Vụ có mã, bằng chứng và vận hành có quyền.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Vận hành so sánh chứng cứ hai bên với bản mô tả đã khóa và lịch sử giao.
2. Vận hành có thể yêu cầu thêm chứng cứ.
3. Quyết định phải chỉ ra từng chứng cứ được dùng, bản mô tả khóa và lý do chọn kết quả.
4. Vận hành ghi quyết định và căn cứ; chỉ tầng B ghi số tiền được hoàn/giải ngân qua đối tác. Tầng A ghi đề xuất giải quyết giữa hai bên nhưng không xác nhận hoặc chuyển tiền ngoài nền tảng.
5. Tầng B: nếu hoàn không cần trả hàng, ghi nghĩa vụ không bán lại/tặng lại hàng và cách xử lý đã được duyệt.
6. Tầng B chuyển yêu cầu hoàn hoặc giải ngân qua SUC-10-03 hoặc SUC-10-02; tầng A giữ hồ sơ để vận hành xem xét việc đóng thử nghiệm.

## 4. Luồng thay thế

- Tầng B có thể hoàn sau trả hàng, hoàn không cần trả, hoàn một phần khi đủ điều kiện, hoặc từ chối. Tầng A chỉ ghi kết quả xem xét và thỏa thuận hoàn trả bên ngoài nếu có; mỗi bên có đường kháng nghị.
- Người bán phản bác hàng giả: vận hành xét thêm lịch sử người mua, dấu hiệu tráo hàng.
- Hai bên đồng ý hoàn một phần: xác nhận số tiền và phần còn lại trước khi gửi đối tác.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Thiếu chứng cứ hoặc dấu hiệu lạm dụng | không tự hoàn chỉ vì chọn lý do hàng giả. | TC-79, TC-80, TC-104 đến TC-106, TC-108 |
| Vụ đang trong thời hạn kháng nghị | Không giải ngân trái chính sách. | Chưa có TC riêng |
| Vận hành chọn số hoàn vượt khoản có nguồn | Từ chối và yêu cầu sửa quyết định. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Quyết định có người chịu trách nhiệm và dấu vết tài chính nhất quán.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Vụ tranh chấp gắn giao dịch, lý do, chứng cứ, người xử lý và quyết định có căn cứ (BR-27).
- Tầng B chỉ hoàn/giải ngân sau xác nhận của đối tác; lý do hàng giả không tự đủ để hoàn (FR-48).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-27, BR-28, BR-42, BR-43; P-16, P-17, P-21.

## 8. Truy vết

FR-31, FR-47, FR-48; BR-27, BR-28, BR-42, BR-43; P-16, P-17, P-21; TC-79, TC-80, TC-104 đến TC-106, TC-108. BUC-11; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Cơ chế thu hồi tiền hoàn từ người bán và xử lý hàng giả chưa chốt.
- Quy trình hàng giả phát hiện muộn, nguồn tiền hoàn và lý do đổi ý thuộc D-09.

