# SUC-11-05 — Xử lý hàng giả phát hiện sau 15 ngày

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-11-05 / BUC-11 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[B]` |
| Tác nhân chính | Vận hành |
| Tác nhân phụ | Người mua, người bán; đối tác thanh toán ở tầng B |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **xử lý hàng giả phát hiện sau 15 ngày** trong BUC-11. Mục tiêu nghiệp vụ: có hồ sơ xử lý hàng giả, chưa hứa hoàn ngay.

## 2. Tiền điều kiện

- Người mua báo cáo nghi hàng giả sau cửa sổ P-15.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Người mua gửi báo cáo và bằng chứng qua SUC-13-01.
2. Vận hành xác minh giao dịch, tin, người bán và chứng cứ.
3. Báo cáo phải giữ bản tin tại thời điểm bán, ảnh, thông tin xác thực và lịch sử người bán để xét hàng giả.
4. Vận hành tạm xử lý tin hoặc tài khoản nếu có căn cứ.
5. Việc xử lý người bán hoặc gỡ tin không tự đồng nghĩa được hoàn tiền sau giải ngân.
6. Hệ thống ghi kết quả báo cáo và thông báo quyền khiếu nại phù hợp.

## 4. Luồng thay thế

- Nếu có chính sách hỗ trợ ngoài 15 ngày được duyệt, mở quy trình riêng; không tự đảo giải ngân.
- Có nhiều giao dịch cùng người bán bị nghi giả: vận hành rà theo vụ liên quan.
- Người mua cung cấp kết luận giám định muộn: bổ sung hồ sơ và xem quyền theo quy định áp dụng.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Yêu cầu hoàn tự động sau cửa sổ | từ chối chuyển trạng thái tiền, giữ báo cáo để xét. | TC-107 |
| Đã quá 15 ngày | Không tạo hoàn tự động từ cơ chế bảo đảm P-15. | Chưa có TC riêng |
| Chứng cứ chưa đủ | Giữ báo cáo đang xét, không gắn nhãn gian lận chắc chắn. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Có hồ sơ xử lý hàng giả, chưa hứa hoàn ngay.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Vụ tranh chấp gắn giao dịch, lý do, chứng cứ, người xử lý và quyết định có căn cứ (BR-27).
- Tầng B chỉ hoàn/giải ngân sau xác nhận của đối tác; lý do hàng giả không tự đủ để hoàn (FR-48).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-31, BR-32; P-21; D-09.

## 8. Truy vết

FR-34, FR-46; BR-31, BR-32; P-21; D-09; TC-107. BUC-11; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- D-09 chưa chốt có hỗ trợ hoàn ngoài 15 ngày và lấy nguồn tiền ở đâu.
- Quy trình hàng giả phát hiện muộn, nguồn tiền hoàn và lý do đổi ý thuộc D-09.

