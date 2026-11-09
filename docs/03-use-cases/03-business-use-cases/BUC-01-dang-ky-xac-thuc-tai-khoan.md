# BUC-01 — Đăng ký, xác thực tài khoản

| Thuộc tính | Nội dung |
|---|---|
| Mã | BUC-01 |
| Phiên bản / trạng thái | 0.1 / `Đề xuất` |
| Tầng | `[A,B]` |

## 1. Mục tiêu nghiệp vụ
Người dùng có một tài khoản đủ điều kiện để mua (và về sau bán), danh tính giao dịch rõ ràng, đã đồng ý điều khoản hiện hành.

## 2. Tác nhân
- Chính: khách chưa đăng nhập, người dùng.
- Hệ thống ngoài: dịch vụ gửi email, SMS.
- Phụ: vận hành (khóa tài khoản, xem ở BUC-13).

## 3. Điều kiện kích hoạt
Khách muốn đặt giá, đăng bán hoặc dùng chức năng yêu cầu đăng nhập (TC-05).

## 4. Kết quả mong muốn và giá trị kinh doanh
- Chỉ tài khoản đã xác thực email, SĐT và đồng ý điều khoản mới đặt giá được (P-01, BR-05), giảm tài khoản rác và đặt giá ảo.
- Thông tin công khai của người dùng không lộ dữ liệu nhạy cảm (BR-30).
- Thay đổi hồ sơ không làm đổi danh tính của giao dịch cũ (FR-02).

## 5. Khác biệt giữa tầng A và tầng B
Không khác về luồng. Tầng B có thể cần thêm xác minh khi kích hoạt KYC (01 mục 9.1, chưa chốt điều kiện).

## 6. Danh sách UC con

| UC | Tên |
|---|---|
| SUC-01-01 | Đăng ký tài khoản |
| SUC-01-02 | Xác thực email |
| SUC-01-03 | Xác thực số điện thoại |
| SUC-01-04 | Đồng ý điều khoản (lưu phiên bản) |
| SUC-01-05 | Đăng nhập, đăng xuất, khôi phục truy cập |
| SUC-01-06 | Xem và sửa hồ sơ cá nhân |
| SUC-01-07 | Xem hồ sơ công khai của người dùng khác |

## 7. Truy vết
FR-01, FR-02, FR-05 · BR-02, BR-05, BR-30 · P-01 · TC-01 đến TC-07.

## 8. Điểm còn mở
- Phương thức xác thực cụ thể (FR-01 ghi "sẽ chọn").
- Ngưỡng tuổi và cách kiểm tra (P-01 chỉ tự xác nhận, cần rà pháp lý).
- Có cần CCCD ngay ở tầng A không (01b mục 13, câu 3).
- Nhà cung cấp SMS và email.
