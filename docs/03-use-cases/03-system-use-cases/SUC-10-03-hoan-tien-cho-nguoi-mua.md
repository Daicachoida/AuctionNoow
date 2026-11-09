# SUC-10-03 — Hoàn tiền cho người mua

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-10-03 / BUC-10 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[B]` |
| Tác nhân chính | Hệ thống, vận hành |
| Tác nhân phụ | Người mua, người bán; đối tác thanh toán ở tầng B |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **hoàn tiền cho người mua** trong BUC-10. Mục tiêu nghiệp vụ: khoản tiền được hoàn nhất quán, không đồng thời giải ngân toàn bộ.

## 2. Tiền điều kiện

- Có quyết định hoàn hợp lệ hoặc giao dịch hủy đủ điều kiện.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Vận hành hoặc hệ thống xác nhận căn cứ và số tiền được hoàn.
2. Hệ thống kiểm tra khoản đang giữ, phần đã giải ngân và lịch sử hoàn.
3. Số tiền hoàn phải có quyết định nguồn, giới hạn không vượt phần còn giữ hoặc nguồn tiền được duyệt.
4. Hệ thống gửi lệnh hoàn có mã chống lặp.
5. Khi hoàn sau trả hàng, cần bằng chứng trả và điều kiện nhận hàng theo chính sách trước khi phát lệnh.
6. Hệ thống đối soát rồi thông báo người mua và người bán.

## 4. Luồng thay thế

- Hoàn một phần chỉ khi chính sách và hai bên cho phép; sau giải ngân đi quy trình riêng SUC-11-06.
- Hoàn một phần: lưu phần còn lại sẽ giải ngân hay tiếp tục giữ, không để trạng thái mơ hồ.
- Hoàn không cần trả hàng vì nghi giả: áp điều khoản xử lý hàng, không tự quyết chỉ từ lý do.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Lệnh trùng, số tiền vượt khoản có thể hoàn hoặc đối tác lỗi | không ghi đã hoàn khi chưa xác nhận. | TC-80, TC-104, TC-105 |
| Đã giải ngân toàn bộ và không có nguồn thu hồi | Không ghi đã hoàn, chuyển SUC-11-06. | Chưa có TC riêng |
| Đối tác phản hồi hoàn trùng | Chỉ một khoản hoàn, đối soát phần dư. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Khoản tiền được hoàn nhất quán, không đồng thời giải ngân toàn bộ.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Tranh chấp đúng hạn chặn giải ngân; một khoản không thể đồng thời có hai kết quả tài chính mâu thuẫn (BR-28, BR-39).
- Lệnh tài chính lặp hoặc phản hồi muộn phải đối soát trước khi đổi trạng thái (BR-38).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-28, BR-38; P-17, P-21.

## 8. Truy vết

FR-43, FR-47; BR-28, BR-38; P-17, P-21; TC-80, TC-104, TC-105. BUC-10; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Nguồn tiền hoàn sau giải ngân và cơ chế thu hồi từ người bán chưa chốt.
- Quyền ra lệnh hoàn/giải ngân, ranh giới với tranh chấp và xử lý sau giải ngân thuộc D-04/D-09.

