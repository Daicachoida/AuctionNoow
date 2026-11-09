# SUC-07-04 — Xử lý sự kiện thanh toán trùng hoặc muộn

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-07-04 / BUC-07 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[B]` |
| Tác nhân chính | Hệ thống |
| Tác nhân phụ | Người bán; vận hành; đối tác thanh toán ở tầng B |

## 1. Mô tả ngắn

SUC này mô tả cách thực hiện **xử lý sự kiện thanh toán trùng hoặc muộn** trong BUC-07. Mục tiêu nghiệp vụ: lịch sử sự kiện đầy đủ, trạng thái tiền nhất quán.

## 2. Tiền điều kiện

- Có sự kiện từ đối tác thanh toán.
- Quyền và trạng thái đối tượng được kiểm tra lại tại lúc thực hiện; dữ liệu hiển thị trước đó không thay thế trạng thái chính thức.

## 3. Luồng chính

1. Hệ thống xác thực nguồn và mã sự kiện.
2. Hệ thống đối chiếu giao dịch cùng trạng thái hiện tại.
3. Mỗi thông báo ngoài cần có mã sự kiện hoặc khóa tương đương để chống lặp và lưu nguyên trạng dữ liệu nhận.
4. Hệ thống áp dụng chuyển trạng thái hợp lệ đúng một lần.
5. Hệ thống so sánh trạng thái trước/sau với ma trận chuyển hợp lệ; sự kiện muộn được giữ để điều tra và hoàn nếu cần.
6. Hệ thống lưu sự kiện và kết quả xử lý.

## 4. Luồng thay thế

- Sự kiện đến sau khi giao dịch hủy hoặc quá hạn chuyển hàng đối soát thủ công.
- Cùng mã sự kiện đến hai lần: trả kết quả lần đầu.
- Sự kiện hợp lệ đến trước giao diện quay về: trạng thái đối tác là nguồn chuẩn.

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Sự kiện trùng hoặc mâu thuẫn | không tạo giao dịch hay khoản tiền thứ hai. | TC-62, TC-63, TC-101 |
| Chữ ký hoặc nguồn không hợp lệ | Không áp dụng, ghi nhận sự cố bảo mật. | Chưa có TC riêng |
| Sự kiện thành công sau khi đã hoàn tiền | Không chuyển sang đã trả; mở đối soát lệch. | Chưa có TC riêng |

Yêu cầu bị từ chối không được âm thầm chuyển đối tượng sang trạng thái thành công. Những trường hợp chưa có TC riêng cần được bổ sung vào kế hoạch kiểm thử.

## 6. Hậu điều kiện

- **Thành công:** Lịch sử sự kiện đầy đủ, trạng thái tiền nhất quán.
- **Không thành công:** Giữ trạng thái chính thức trước thao tác, trừ các bản ghi yêu cầu, lỗi hoặc bằng chứng cần lưu để đối soát.

## 7. Quy tắc áp dụng

- Lời khai hoặc trang quay về không đủ xác nhận đã thanh toán (BR-22).
- Đã trả, đang giữ, đã giải ngân và đã hoàn phải được theo dõi riêng (FR-22, BR-38).
- Mã quy tắc/đề xuất liên quan trực tiếp: BR-22, BR-28, BR-38; NFR-02.

## 8. Truy vết

FR-23, FR-25; BR-22, BR-28, BR-38; NFR-02; TC-62, TC-63, TC-101. BUC-07; các TC nêu trên chỉ bao phủ những kịch bản đã có trong 01b.

## 9. Điểm còn mở

- Khóa chống lặp, thời hạn lưu và xử lý tiền đến muộn phụ thuộc đối tác.
- Đối tác thanh toán, nguồn xác nhận và cách đối soát thiếu/thừa tiền thuộc cổng D-04.

