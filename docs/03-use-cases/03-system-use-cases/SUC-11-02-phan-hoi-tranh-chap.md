# SUC-11-02 — Phản hồi tranh chấp

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-11-02 / BUC-11 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Người bán |
| Tác nhân phụ | Người mua, người bán; đối tác thanh toán ở tầng B |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **phản hồi tranh chấp** trong BUC-11. Mục tiêu nghiệp vụ: hồ sơ có phản hồi hoặc ghi nhận quá hạn rõ.

## 2. Tiền điều kiện

- Có vụ tranh chấp đang chờ phản hồi và đúng người bán.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Người bán mở vụ, xem lý do và chứng cứ được phép.
2. Người bán gửi giải trình cùng chứng cứ trong 3 ngày làm việc đề xuất.
3. Phản hồi cần phân biệt đồng ý hoàn, đề xuất giải pháp khác và phản bác kèm chứng cứ.
4. Hệ thống lưu phiên bản, thời điểm và thông báo vận hành.
5. Thời hạn 3 ngày làm việc tính từ thông báo hợp lệ; hệ thống lưu thời điểm đã nhận để vận hành kiểm tra.
6. Vận hành tiếp tục xét vụ.

## 4. Luồng thay thế

- Không phản hồi đúng hạn: chuyển ưu tiên cho vận hành, không tự xử thua.
- Người bán đồng ý hoàn: vẫn cần quyết định và đối soát tầng B trước khi tiền chuyển.
- Người bán cần thêm thời gian: vận hành quyết định và thông báo người mua theo quy chế.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Chứng cứ không hợp lệ hoặc sai quyền | từ chối nhưng giữ vụ mở. | TC-77, TC-79 |
| Người không thuộc giao dịch gửi phản hồi | Từ chối truy cập. | Chưa có TC riêng |
| Phản hồi sau hạn | Lưu để xét nếu chính sách cho phép, không xóa cờ quá hạn. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Hồ sơ có phản hồi hoặc ghi nhận quá hạn rõ.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Vụ tranh chấp gắn giao dịch, lý do, chứng cứ, người xử lý và quyết định có căn cứ (BR-27).
- Tầng B chỉ hoàn/giải ngân sau xác nhận của đối tác; lý do hàng giả không tự đủ để hoàn (FR-48).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-27, BR-39; P-16.

## 8. Truy vết

FR-30, FR-31; BR-27, BR-39; P-16; TC-77, TC-79. BUC-11; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Thời hạn phản hồi và loại chứng cứ cần PO duyệt.
- Quy trình hàng giả phát hiện muộn, nguồn tiền hoàn và lý do đổi ý thuộc D-09.

