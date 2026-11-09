# SUC-10-01 — Hoàn tất giao dịch tự động

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-10-01 / BUC-10 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[B]` |
| Tác nhân chính | Hệ thống |
| Tác nhân phụ | Người mua, người bán; đối tác thanh toán ở tầng B |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **hoàn tất giao dịch tự động** trong BUC-10. Mục tiêu nghiệp vụ: giao dịch đủ điều kiện giải ngân, chưa đồng nghĩa đã chi tiền.

## 2. Tiền điều kiện

- Giao được xác minh.
- Hết 15 ngày lịch.
- Không có tranh chấp chặn.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Hệ thống kiểm tra mốc giao và cửa sổ P-15.
2. Hệ thống xác nhận không có tranh chấp đúng hạn hoặc kháng nghị đang mở.
3. Thời điểm kết thúc 15 ngày tính từ giao được xác minh theo giờ máy chủ và lịch đã công bố.
4. Hệ thống ghi đủ điều kiện hoàn tất.
5. Trước khi đủ điều kiện giải ngân, kiểm tra vụ tranh chấp, kháng nghị, hoàn tiền và trạng thái vận chuyển lần cuối.
6. Hệ thống chuyển sang SUC-10-02 để giải ngân theo đối tác.

## 4. Luồng thay thế

- Người mua bấm đã nhận sớm không rút ngắn cửa sổ; tranh chấp mở đúng hạn dừng luồng.
- Người mua xác nhận đã nhận sớm: lưu xác nhận nhưng giữ cửa sổ 15 ngày.
- Có vụ tranh chấp mở trong ngày cuối: giữ tiền và chuyển BUC-11.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Thiếu bằng chứng giao hoặc đối tác chưa xác nhận | không hoàn tất tự động. | TC-73 đến TC-75, TC-78 |
| Chỉ có lời người bán khai đã giao | Không bắt đầu đếm 15 ngày. | Chưa có TC riêng |
| Tiến trình hoàn tất chạy lặp | Giữ một kết quả, không gửi lệnh giải ngân mới. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Giao dịch đủ điều kiện giải ngân, chưa đồng nghĩa đã chi tiền.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Tranh chấp đúng hạn chặn giải ngân; một khoản không thể đồng thời có hai kết quả tài chính mâu thuẫn (BR-28, BR-39).
- Lệnh tài chính lặp hoặc phản hồi muộn phải đối soát trước khi đổi trạng thái (BR-38).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-26, BR-28, BR-39; P-15.

## 8. Truy vết

FR-29, FR-42; BR-26, BR-28, BR-39; P-15; TC-73 đến TC-75, TC-78. BUC-10; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Có giải ngân sớm khi người mua hài lòng không là D-09 còn mở.
- Quyền ra lệnh hoàn/giải ngân, ranh giới với tranh chấp và xử lý sau giải ngân thuộc D-04/D-09.

