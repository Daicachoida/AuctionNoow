# SUC-08-02 — Xử lý tiền đặt trước khi bỏ thanh toán

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-08-02 / BUC-08 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[B]` |
| Tác nhân chính | Hệ thống, vận hành |
| Tác nhân phụ | Người thắng, người bán; đối tác thanh toán ở tầng B |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **xử lý tiền đặt trước khi bỏ thanh toán** trong BUC-08. Mục tiêu nghiệp vụ: khoản đặt trước có kết quả tài chính duy nhất và nhật ký.

## 2. Tiền điều kiện

- Người thắng quá hạn.
- Có khoản đặt trước đang giữ.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Hệ thống kiểm tra điều khoản đã công bố khi người mua nộp.
2. Vận hành xác nhận căn cứ mất hoặc hoàn theo chính sách hợp lệ.
3. Quyết định mất tiền phải dựa điều khoản người mua đã thấy trước khi nộp, không áp chính sách mới hồi tố.
4. Hệ thống gửi yêu cầu tới đối tác và chờ đối soát.
5. Từng lệnh chuyển/hoàn tiền đặt trước phải có mã chống lặp và xác nhận của đối tác.
6. Hệ thống ghi kết quả và thông báo các bên.

## 4. Luồng thay thế

- Nếu tranh chấp về căn cứ, tạm giữ và chuyển vận hành xem xét.
- Người thắng kháng nghị lý do bỏ thanh toán: tạm ngừng phân bổ nếu chính sách cho phép.
- Đối tác báo khoản đã hoàn: ghi kết quả đã hoàn, không đòi lại tự động.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Chưa rõ người nhận hoặc chưa qua cổng pháp lý | không tự phân bổ khoản tiền. | TC-100, TC-101 |
| Chưa xác định người nhận khoản bị mất | Không gửi lệnh phân bổ. | Chưa có TC riêng |
| Tiền đặt trước không khớp phiên hoặc người mua | Chặn xử lý, mở đối soát. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Khoản đặt trước có kết quả tài chính duy nhất và nhật ký.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Quá hạn không tự trao quyền mua cho người trả giá kế tiếp (FR-24).
- Mất tiền đặt trước chỉ theo quy tắc công bố trước và sau cổng pháp lý/đối tác (BR-40, BR-41).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-40, BR-41; P-07; D-08.

## 8. Truy vết

FR-45; BR-40, BR-41; P-07; D-08; TC-100, TC-101. BUC-08; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Tỷ lệ, người nhận khoản bị mất, căn cứ pháp lý và quy trình kháng nghị chưa chốt.
- Hạn trả, người nhận khoản đặt trước bị mất và chế tài tái phạm thuộc D-08.

