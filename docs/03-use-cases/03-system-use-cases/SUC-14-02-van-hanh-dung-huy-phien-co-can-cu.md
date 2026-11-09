# SUC-14-02 — Vận hành dừng, hủy phiên có căn cứ

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-14-02 / BUC-14 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Vận hành |
| Tác nhân phụ | Người đặt giá; người bán; đối tác thanh toán ở tầng B |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **vận hành dừng, hủy phiên có căn cứ** trong BUC-14. Mục tiêu nghiệp vụ: phiên có trạng thái và quyết định có thể kiểm tra.

## 2. Tiền điều kiện

- Có căn cứ hàng mất, sai trọng yếu, gian lận hoặc sự cố.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Vận hành xem bằng chứng, lịch sử giá và thẩm quyền.
2. Vận hành chọn dừng tạm hoặc hủy, ghi lý do và tác động.
3. Quyết định dừng tạm và hủy vĩnh viễn cần phân biệt vì ảnh hưởng thời gian, giá, giao dịch và tiền đặt trước khác nhau.
4. Hệ thống khóa nhận giá, lưu quyết định, công bố lý do.
5. Vận hành phải ghi căn cứ có thể kiểm tra và người có thẩm quyền, tránh dùng thao tác dừng để bán ngoài phiên.
6. Hệ thống chuyển SUC-14-03 để xử lý các bên.

## 4. Luồng thay thế

- Nếu chỉ tạm dừng do sự cố, cách mở lại hoặc bù thời gian theo chính sách sẽ chốt.
- Sự cố hệ thống: tạm dừng theo NFR-06 và chờ quy tắc bù thời gian.
- Nghi gian lận chưa đủ chứng cứ: tạm dừng để điều tra, không tự hủy kết quả.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Thiếu căn cứ hoặc quyền | không hủy phiên. | TC-48, TC-49 |
| Phiên đã có giao dịch | Không dùng hủy phiên đơn giản, chuyển xử lý giao dịch. | Chưa có TC riêng |
| Nhiều vận hành quyết định cùng lúc | Áp một trạng thái chính thức, giữ mọi yêu cầu trong nhật ký. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Phiên có trạng thái và quyết định có thể kiểm tra.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Dừng/hủy sau giá đầu phải do vận hành có căn cứ; lượt giá cũ không tự thành giao dịch (BR-10, FR-19).
- Sự cố cần chính sách dừng, công bố và khôi phục (NFR-06).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-20; P-09, P-20; NFR-06.

## 8. Truy vết

FR-19, FR-35; BR-20; P-09, P-20; NFR-06; TC-48, TC-49. BUC-14; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Quy trình kháng nghị, bù thời gian và xử lý đặt trước tầng B chưa chốt.
- Quy tắc hoàn đặt trước khi hủy phiên, bù thời gian và kháng nghị chưa chốt.

