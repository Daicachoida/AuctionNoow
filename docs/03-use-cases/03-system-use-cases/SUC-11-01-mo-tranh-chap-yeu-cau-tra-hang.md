# SUC-11-01 — Mở tranh chấp, yêu cầu trả hàng

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-11-01 / BUC-11 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Người mua |
| Tác nhân phụ | Người mua, người bán; đối tác thanh toán ở tầng B |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **mở tranh chấp, yêu cầu trả hàng** trong BUC-11. Mục tiêu nghiệp vụ: vụ tranh chấp có lịch sử, nguồn chứng cứ và trạng thái chặn rõ.

## 2. Tiền điều kiện

- Tầng A: có giao dịch thử nghiệm ngoài nền tảng và hai bên bất đồng. Tầng B: có giao dịch đủ điều kiện khiếu nại theo P-16.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Người mua chọn giao dịch, lý do và gửi mô tả, bằng chứng.
2. Hệ thống kiểm tra phạm vi phù hợp: tầng A tiếp nhận để vận hành xử lý thủ công; tầng B kiểm tra thời hạn và lý do theo P-16, P-21.
3. Lý do, chứng cứ và mốc thời gian phải gắn giao dịch cụ thể; bản mô tả tin tại lúc đấu giá được khóa để đối chiếu.
4. Hệ thống cấp mã vụ, khóa bản mô tả tin cùng chứng cứ, báo người bán.
5. Tầng B, việc tạo vụ hợp lệ và chặn giải ngân cần được xử lý nhất quán để không mở vụ mà tiền vẫn chi.
6. Tầng B chặn giải ngân khi vụ mở đúng hạn.

## 4. Luồng thay thế

- Tầng A xử lý thủ công, không có lệnh hoàn tiền qua hệ thống; nếu đã chuyển tiền thật bên ngoài, hai bên tự thỏa thuận hoàn trả và vận hành chỉ lưu bằng chứng. Tầng B áp P-21, không có lý do đổi ý theo đề xuất.
- Không nhận hàng khi quá hạn gửi/giao: cho mở trước mốc giao được xác minh.
- Nghi hàng giả sau 15 ngày: chuyển SUC-11-05, không tự hoàn.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Yêu cầu ngoài hạn hoặc không đủ dữ liệu | nêu đường báo cáo phù hợp, không tự hoàn. | TC-75, TC-76, TC-78, TC-103 |
| Người mua chọn đổi ý | Từ chối nếu P-21 được duyệt theo đề xuất. | Chưa có TC riêng |
| Gửi vụ trùng cùng lý do | Hiển thị vụ đang mở, không tạo hai khoản hoàn. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Vụ tranh chấp có lịch sử, nguồn chứng cứ và trạng thái chặn rõ.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Vụ tranh chấp gắn giao dịch, lý do, chứng cứ, người xử lý và quyết định có căn cứ (BR-27).
- Tầng B chỉ hoàn/giải ngân sau xác nhận của đối tác; lý do hàng giả không tự đủ để hoàn (FR-48).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-27, BR-39; P-16, P-21.

## 8. Truy vết

FR-30, FR-46; BR-27, BR-39; P-16, P-21; TC-75, TC-76, TC-78, TC-103. BUC-11; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Bỏ lý do đổi ý cần PO duyệt; quyền ngoài cửa sổ cần rà pháp lý.
- Quy trình hàng giả phát hiện muộn, nguồn tiền hoàn và lý do đổi ý thuộc D-09.

