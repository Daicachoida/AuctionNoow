# SUC-11-06 — Tranh chấp sau giải ngân

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-11-06 / BUC-11 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[B]` |
| Tác nhân chính | Vận hành |
| Tác nhân phụ | Người mua, người bán; đối tác thanh toán ở tầng B |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **tranh chấp sau giải ngân** trong BUC-11. Mục tiêu nghiệp vụ: vụ việc được xử lý có căn cứ, tiền chỉ đổi trạng thái khi đối soát.

## 2. Tiền điều kiện

- Tiền đã giải ngân, sau đó có khiếu nại.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Vận hành mở hồ sơ tách khỏi tranh chấp chặn giải ngân.
2. Vận hành thu chứng cứ và xác minh trạng thái tiền đã chi.
3. Cần xác định tiền đã tới người bán hay còn đang xử lý ở đối tác trước khi chọn biện pháp.
4. Vận hành quyết định biện pháp theo quy chế và đối tác.
5. Vận hành lưu căn cứ đòi hoàn, kết quả liên hệ người bán, đối tác và quyền khiếu nại của người mua.
6. Hệ thống thông báo các bên và ghi lịch sử xử lý.

## 4. Luồng thay thế

- Có thể yêu cầu người bán hoàn, dùng cơ chế đảm bảo khác hoặc chuyển hỗ trợ pháp lý nếu đã được quy định.
- Đối tác báo giải ngân chưa hoàn tất: kiểm tra có thể chặn theo hợp đồng, không suy đoán.
- Người bán tự nguyện hoàn: chỉ ghi đã hoàn sau đối soát nguồn chuyển tiền.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Không còn tiền đang giữ | không ghi đã hoàn hoặc hứa thu hồi ngay. | TC-83 |
| Đã giải ngân và người bán không đồng ý | Không tự ghi tiền đã thu hồi. | Chưa có TC riêng |
| Tranh chấp mở sau giải ngân nhưng cùng vụ cũ | Liên kết hồ sơ, không tạo kết quả tài chính mâu thuẫn. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Vụ việc được xử lý có căn cứ, tiền chỉ đổi trạng thái khi đối soát.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Vụ tranh chấp gắn giao dịch, lý do, chứng cứ, người xử lý và quyết định có căn cứ (BR-27).
- Tầng B chỉ hoàn/giải ngân sau xác nhận của đối tác; lý do hàng giả không tự đủ để hoàn (FR-48).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-27, BR-28, BR-38; P-17.

## 8. Truy vết

FR-31, FR-43; BR-27, BR-28, BR-38; P-17; TC-83. BUC-11; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Cơ chế thu hồi sau giải ngân chưa chốt.
- Quy trình hàng giả phát hiện muộn, nguồn tiền hoàn và lý do đổi ý thuộc D-09.

