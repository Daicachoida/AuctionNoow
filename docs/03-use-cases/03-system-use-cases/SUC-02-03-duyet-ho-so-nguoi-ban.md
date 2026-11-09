# SUC-02-03 — Duyệt hồ sơ người bán

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-02-03 / BUC-02 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Vận hành |
| Tác nhân phụ | Vận hành; dịch vụ xác minh nếu được chọn |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **duyệt hồ sơ người bán** trong BUC-02. Mục tiêu nghiệp vụ: trạng thái xác minh có thể truy vết; dữ liệu gốc không công khai.

## 2. Tiền điều kiện

- Hồ sơ đang xét và vận hành có quyền duyệt.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Vận hành mở hồ sơ và bằng chứng.
2. Vận hành đối chiếu theo chính sách áp dụng.
3. Vận hành kiểm tra trùng lặp và mối liên hệ tài khoản theo chính sách, không chỉ kiểm đủ trường.
4. Vận hành chọn đạt, từ chối hoặc yêu cầu bổ sung và ghi lý do.
5. Quyết định phải lưu người duyệt, căn cứ, thời điểm, phiên bản tiêu chí và chỉ công khai trạng thái tổng quát.
6. Hệ thống lưu người duyệt, thời điểm, thông báo kết quả.

## 4. Luồng thay thế

- Nếu đạt: mở quyền phát hành tin; nếu từ chối: hiển thị lý do và đường nộp lại.
- Có hồ sơ cần bổ sung: chuyển về yêu cầu bổ sung kèm từng trường cần sửa.
- Hồ sơ đã đạt nhưng thông tin đổi trọng yếu: yêu cầu xét lại thay vì tự duy trì huy hiệu.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Thiếu thẩm quyền hoặc bằng chứng không đủ | không chuyển sang đạt. | TC-10, TC-11 |
| Hai người duyệt cùng lúc | Chỉ quyết định hợp lệ đầu tiên được áp dụng, người sau thấy trạng thái mới. | Chưa có TC riêng |
| Bằng chứng hết hạn | Không duyệt đạt; yêu cầu nộp tài liệu còn hiệu lực. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Trạng thái xác minh có thể truy vết; dữ liệu gốc không công khai.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Chỉ hồ sơ xác minh đạt mới mở quyền bán; dữ liệu giấy tờ không công khai (BR-04, BR-30).
- Tầng A chỉ mở cá nhân và shop nếu M-S1 được PO duyệt.
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-04, BR-30.

## 8. Truy vết

FR-03 đến FR-05; BR-04, BR-30; TC-10, TC-11. BUC-02; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Tiêu chuẩn duyệt và quyền của từng vai trò vận hành cần chốt.
- Trường xác minh, thời hạn hiệu lực và thẩm quyền duyệt phụ thuộc quy trình xác minh được phê duyệt.

