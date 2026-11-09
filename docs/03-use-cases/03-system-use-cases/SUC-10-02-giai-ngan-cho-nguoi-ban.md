# SUC-10-02 — Giải ngân cho người bán

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-10-02 / BUC-10 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[B]` |
| Tác nhân chính | Hệ thống |
| Tác nhân phụ | Người mua, người bán; đối tác thanh toán ở tầng B |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **giải ngân cho người bán** trong BUC-10. Mục tiêu nghiệp vụ: khoản tiền có kết quả giải ngân duy nhất.

## 2. Tiền điều kiện

- Giao dịch đủ điều kiện.
- Tiền đang giữ.
- Không có tranh chấp chặn.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Hệ thống kiểm tra lại quyền giải ngân và trạng thái khoản tiền.
2. Hệ thống gửi một lệnh giải ngân có mã chống lặp tới đối tác.
3. Lệnh giải ngân phải tham chiếu giao dịch, khoản đang giữ, người bán và số tiền sau mọi khoản hoàn/điều chỉnh.
4. Hệ thống đối soát kết quả.
5. Hệ thống ghi trạng thái đang giải ngân riêng với đã giải ngân; chỉ xác nhận đối tác mới đóng khoản.
6. Chỉ khi đối tác xác nhận mới ghi đã giải ngân và thông báo.

## 4. Luồng thay thế

- Lệnh đang xử lý hoặc phản hồi muộn: giữ trạng thái chờ đối soát.
- Đối tác trả đang xử lý: chờ đối soát, không gửi lệnh mới tùy tiện.
- Vận hành chặn do tranh chấp đúng hạn: giữ khoản đang giữ và ghi lý do.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Lệnh trùng hoặc tranh chấp xuất hiện trước ranh giới chốt | không chi trả hai lần hoặc trái chính sách. | TC-67, TC-78, TC-84 |
| Tranh chấp được ghi trước lệnh giải ngân | Từ chối lệnh, không trả tiền. | Chưa có TC riêng |
| Đối tác trả lỗi hoặc không rõ kết quả | Đối soát mã lệnh trước khi thử lại. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Khoản tiền có kết quả giải ngân duy nhất.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Tranh chấp đúng hạn chặn giải ngân; một khoản không thể đồng thời có hai kết quả tài chính mâu thuẫn (BR-28, BR-39).
- Lệnh tài chính lặp hoặc phản hồi muộn phải đối soát trước khi đổi trạng thái (BR-38).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-24, BR-28, BR-38, BR-39.

## 8. Truy vết

FR-42; BR-24, BR-28, BR-38, BR-39; TC-67, TC-78, TC-84. BUC-10; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Ranh giới tranh chấp với giải ngân và quyền ra lệnh của đối tác chưa chốt.
- Quyền ra lệnh hoàn/giải ngân, ranh giới với tranh chấp và xử lý sau giải ngân thuộc D-04/D-09.

