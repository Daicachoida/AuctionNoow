# SUC-02-04 — Xác minh lại khi hết hiệu lực

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-02-04 / BUC-02 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Người bán, vận hành |
| Tác nhân phụ | Vận hành; dịch vụ xác minh nếu được chọn |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **xác minh lại khi hết hiệu lực** trong BUC-02. Mục tiêu nghiệp vụ: hồ sơ có kỳ xác minh mới và lịch sử kỳ cũ.

## 2. Tiền điều kiện

- Hồ sơ xác minh hết hiệu lực hoặc bị yêu cầu xác minh lại.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Hệ thống đánh dấu cần xác minh lại và chặn phát hành tin mới.
2. Người bán cập nhật thông tin, bằng chứng.
3. Hệ thống cần phân biệt hồ sơ hết hạn với tài khoản bị khóa; cả hai có thể chặn tin mới nhưng lý do và đường xử lý khác nhau.
4. Vận hành xét lại như SUC-02-03.
5. Sau khi đạt lại, quyền bán mở theo chính sách; các quyết định và tin đã phát hành trước đó vẫn có lịch sử riêng.
6. Hệ thống mở lại quyền bán khi đạt.

## 4. Luồng thay thế

- Tin và giao dịch đang tồn tại được rà riêng; không tự xóa lịch sử.
- Người bán không nộp lại: giữ cần xác minh lại và không mở tin mới.
- Vận hành từ chối lần nộp lại: hiển thị lý do, tiếp tục chặn quyền bán.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Người bán cố đăng tin khi chưa đạt | chặn và nêu việc cần làm. | TC-12 |
| Hồ sơ đang xét lại mà cố phát hành tin | Từ chối với trạng thái đang xét. | Chưa có TC riêng |
| Thông tin mới mâu thuẫn giao dịch đang chạy | Chuyển vận hành rà ảnh hưởng; không sửa giao dịch cũ. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Hồ sơ có kỳ xác minh mới và lịch sử kỳ cũ.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Chỉ hồ sơ xác minh đạt mới mở quyền bán; dữ liệu giấy tờ không công khai (BR-04, BR-30).
- Tầng A chỉ mở cá nhân và shop nếu M-S1 được PO duyệt.
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-04.

## 8. Truy vết

FR-03, FR-04; BR-04; TC-12. BUC-02; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Thời hạn hiệu lực và ảnh hưởng lên phiên đang mở chưa chốt.
- Trường xác minh, thời hạn hiệu lực và thẩm quyền duyệt phụ thuộc quy trình xác minh được phê duyệt.

