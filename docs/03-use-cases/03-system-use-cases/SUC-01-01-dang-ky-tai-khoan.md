# SUC-01-01 — Đăng ký tài khoản

| Thuộc tính | Nội dung |
|---|---|
| Mã / BUC cha | SUC-01-01 / BUC-01 |
| Phiên bản / trạng thái | 0.2 / `Đề xuất` |
| Tầng | `[A,B]` |
| Tác nhân chính | Khách chưa đăng nhập |
| Tác nhân phụ | Dịch vụ gửi email và SMS |

## 1. Mô tả ngắn
Khách tạo tài khoản bằng email và số điện thoại, đồng ý điều khoản. Tài khoản mới chưa xác thực nên chưa đặt giá được. Một tài khoản có thể vừa mua vừa bán (P-01); quyền bán chỉ mở sau khi người dùng đi qua BUC-02.

## 2. Tiền điều kiện
- Khách chưa có tài khoản dùng email hoặc SĐT này.
- Hệ thống đang có phiên bản điều khoản hiện hành để hiển thị (BR-05).

## 3. Luồng chính
1. Khách chọn đăng ký (từ nút đăng ký, hoặc bị chuyển sang khi bấm đặt giá lúc chưa đăng nhập, TC-05).
2. Khách nhập thông tin bắt buộc: email, số điện thoại, thông tin xác thực đăng nhập (phương thức chưa chốt, FR-01), tên hiển thị.
3. Hệ thống kiểm tra định dạng email và số điện thoại, và email, SĐT chưa gắn với tài khoản khác.
4. Hệ thống hiển thị điều khoản và chính sách bảo vệ dữ liệu cá nhân. Khách tự xác nhận đủ tuổi tham gia theo điều khoản (P-01) và bấm đồng ý (SUC-01-04).
5. Hệ thống tạo tài khoản ở trạng thái email chưa xác thực, SĐT chưa xác thực, và lưu phiên bản điều khoản đã đồng ý cùng thời điểm (BR-05).
6. Hệ thống gửi mã xác thực tới email (SUC-01-02) và SĐT (SUC-01-03).
7. Hệ thống đăng nhập khách vào tài khoản mới và nêu rõ việc cần làm để đặt giá: xác thực email và SĐT.

## 4. Luồng thay thế
- **Khách xem tin trước khi xác thực:** tài khoản chưa xác thực xem tin, tìm kiếm bình thường nhưng không đặt giá được (TC-01, TC-02).
- **Khách bỏ dở sau khi nhập thông tin:** chưa tạo tài khoản, không lưu dữ liệu ngoài những gì cần cho phiên đăng ký đang mở.
- **Khách cố đặt giá hoặc đăng bán khi chưa đồng ý điều khoản:** bị chặn và hiển thị điều khoản; sau khi đồng ý, hệ thống lưu phiên bản (TC-04).
- **Email hoặc SĐT đã gắn với tài khoản khác:** hướng khách sang đăng nhập hoặc khôi phục truy cập (SUC-01-05).

## 5. Ngoại lệ và từ chối

| Tình huống | Hệ thống phản hồi | TC |
|---|---|---|
| Email hoặc SĐT sai định dạng | Báo lỗi đúng trường, không tạo tài khoản | Chưa có TC |
| Email hoặc SĐT đã gắn với tài khoản khác | Từ chối, hướng dẫn đăng nhập hoặc khôi phục truy cập | Chưa có TC |
| Khách không đồng ý điều khoản | Không tạo tài khoản | TC-04 (một phần) |
| Khách không xác nhận đủ tuổi | Không tạo tài khoản | Chưa có TC |
| Dịch vụ email hoặc SMS lỗi | Tài khoản vẫn tạo; cho phép gửi lại mã sau; chưa đặt giá được tới khi xác thực xong | Chưa có TC |
| Khách chưa xác thực cố đặt giá | Chặn, nêu bước còn thiếu | TC-01, TC-02 |

## 6. Hậu điều kiện
- Có tài khoản với email và SĐT ở trạng thái chưa xác thực.
- Có bản ghi đồng ý điều khoản kèm phiên bản và thời điểm (BR-05).
- Tài khoản chưa có hồ sơ người bán.
- Sự kiện tạo tài khoản được ghi nhật ký (SUC-15-02).

## 7. Quy tắc áp dụng
- P-01: một tài khoản có thể vừa mua vừa bán; xác thực email và SĐT trước khi đặt giá; người tham gia tự xác nhận đủ tuổi.
- BR-05: lưu phiên bản điều khoản đã đồng ý.
- NFR-04: thu thập dữ liệu tối thiểu, bảo vệ khi truyền và lưu trữ.

## 8. Truy vết
FR-01 · BR-02, BR-05 · P-01 · NFR-04 · TC-01, TC-02, TC-04, TC-05.

## 9. Điểm còn mở
- **Phương thức xác thực đăng nhập** (mật khẩu, mã một lần, đăng nhập qua bên thứ ba): FR-01 ghi "sẽ chọn", chưa chốt.
- **Một SĐT hoặc một email có thể gắn nhiều tài khoản không.** 01b mục 11 dùng SĐT trùng làm dấu hiệu đặt giá ảo, nên đề xuất mỗi SĐT và email chỉ một tài khoản; cần PO duyệt.
- **Ngưỡng tuổi và cách kiểm tra:** P-01 chỉ tự xác nhận, cần rà pháp lý.
- **Chống đăng ký hàng loạt** (bot, tài khoản giả): 02 chưa có yêu cầu; liên quan rủi ro đặt giá ảo.
- **Thông báo "email đã tồn tại"** có thể để lộ ai đã đăng ký; cần chọn giữa tiện dụng và bảo mật.
- **Thời điểm đồng ý điều khoản:** TC-04 chặn ở bước đăng bán hoặc đặt giá, SUC này đề xuất đồng ý ngay lúc đăng ký và hỏi lại khi điều khoản đổi phiên bản (SUC-01-04). Cần xác nhận.
- Chưa có TC cho các ngoại lệ ở bảng trên; nên bổ sung vào 01b.
