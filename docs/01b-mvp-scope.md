# 01b — Phạm vi MVP chi tiết

## 1. Thông tin tài liệu

| Thuộc tính | Nội dung |
|---|---|
| Dự án | AuctionNoow — marketplace đấu giá, triển khai tại Việt Nam trước |
| Phiên bản | 0.1 — bản đề xuất MVP chi tiết, chờ PO duyệt |
| Đầu vào | [01-product-scope.md](01-product-scope.md), [02-requirements-business-rules.md](02-requirements-business-rules.md) |
| Mục đích | Xác định chính xác MVP gồm gì, không gồm gì, theo thứ tự nào, và điều kiện để đi tiếp |
| Chủ quyết định | Chủ dự án / Product Owner (PO) |
| Trạng thái | `Đề xuất` — chưa có hiệu lực cho đến khi PO ghi nhận |

**Quy ước:** `Đã chốt` = PO đã quyết định; `Đề xuất` = BA đề xuất, chờ PO; `Cổng` = điều kiện bắt buộc phải thỏa trước khi làm việc tương ứng với tiền thật hoặc người dùng thật. Mã FR, BR, P, D lấy từ file 02; file này không tạo mã yêu cầu mới, chỉ chọn và sắp xếp lại.

## 2. Tóm tắt quyết định cần PO duyệt

Tài liệu 01 và 02 đã chốt mục tiêu giữ tiền đến khi đủ điều kiện giải ngân. Tuy nhiên, trong thực tế việc này phụ thuộc đối tác thanh toán, khung pháp lý giữ tiền và rà soát luật đấu giá, chưa có cái nào đã hoàn tất. Vì vậy file này đề xuất chia MVP thành hai tầng:

- **Tầng A — Thử nghiệm kín, không tiền thật:** người dùng thật, đăng hàng, đấu giá, chốt người thắng và ghi nhận giao dịch. Thanh toán và giải ngân không đi qua hệ thống; giao dịch được đánh dấu rõ là "thử nghiệm".
- **Tầng B — Thanh toán bảo đảm:** chỉ mở khi có đối tác giữ tiền đã ký, đã rà pháp lý và đã thử đối soát (cổng phát hành D-04).

PO cần quyết định:

| Mã | Quyết định | Đề xuất của BA |
|---|---|---|
| M-D1 | Chấp nhận tách MVP thành tầng A và tầng B | Có |
| M-D2 | Tầng A có cho người thắng tự chuyển khoản cho người bán ngoài hệ thống không | Không cho hệ thống nhận tiền. Người thắng và người bán có thể tự thỏa thuận ngoài nền tảng, nhưng khi đó nền tảng không bảo vệ khoản tiền. Trang phiên và trang giao dịch phải hiển thị cảnh báo này rõ ràng, và người dùng phải bấm xác nhận đã đọc |
| M-D3 | Thời điểm mở tầng A cho người dùng ngoài vòng kín | Sau khi đạt tiêu chí ở mục 9 |
| M-D4 | Cơ chế "đồng ý đã đọc cảnh báo" ở M-D2 có cần lưu phiên bản nội dung cảnh báo không | Có. Lưu cùng phiên bản điều khoản theo BR-05 |
| M-D5 | Mục 11 (chống đặt giá ảo ở mức thủ công) có đưa vào MVP không | Có, ở mức thủ công. Chưa tự động hóa |

Nếu PO không đồng ý tách tầng và muốn giữ tiền ngay trong MVP đầu tiên, thời gian dự kiến phụ thuộc hoàn toàn vào việc có đối tác hay không. Khi đó, BA khuyến nghị đưa việc tìm đối tác thành công việc đầu tiên, trước khi viết code cho thanh toán.

## 3. Mục tiêu của MVP

MVP không cố gắng là sàn hoàn chỉnh. Mục tiêu là trả lời bốn câu hỏi bằng dữ liệu thực:

1. Người dùng có đặt giá và hoàn tất giao dịch qua đấu giá tăng dần hay không? (Tương ứng mục tiêu 1 và 3 của file 01)
2. Quy trình đấu giá có kết quả đúng và truy vết được dưới tải nhỏ đến vừa, kể cả khi đặt giá sát giờ? (mục tiêu 2)
3. Cơ chế tin cậy tối thiểu (xác minh, đánh giá, báo cáo, tranh chấp thủ công) có đủ để người dùng quay lại? (mục tiêu 4)
4. Mô hình có chịu được việc mở rộng sang tầng B mà không phải viết lại lõi đấu giá? (mục tiêu 5)

## 4. Phạm vi trong MVP

### 4.1. Nhóm chức năng và mã yêu cầu

| Nhóm | Mã yêu cầu trong file 02 | Tầng |
|---|---|---|
| Tài khoản, xác thực cơ bản | FR-01, FR-02, FR-05 | A, B |
| Hồ sơ người bán và xác minh cơ bản | FR-03, FR-04 (phần xác minh tối thiểu) | A (thủ công), B |
| Đăng hàng và duyệt tin | FR-06, FR-07, FR-08, FR-09, FR-11 | A, B |
| Xem tin và tìm kiếm cơ bản | FR-10 | A, B |
| Đấu giá tăng dần và mua ngay | FR-12 đến FR-19, FR-38 đến FR-40 | A, B |
| Tạo giao dịch và ghi nhận trạng thái | FR-20, FR-21, FR-22, FR-23, FR-27, FR-28 | A (ghi nhận thử nghiệm), B đầy đủ |
| Thanh toán bảo đảm | FR-24, FR-25, FR-41, FR-42, FR-43 | B |
| Vận chuyển | FR-26, FR-29 | A (tự khai, đánh dấu chưa đối soát), B (có nhà vận chuyển) |
| Tranh chấp và hoàn tất | FR-30, FR-31, FR-32 | A (xử lý thủ công), B |
| Đánh giá và uy tín | FR-33 | A |
| Báo cáo và vận hành | FR-34, FR-35, FR-36, FR-37 | A, B |

### 4.2. Hàng hóa trong MVP

Theo P-02 và quyết định D-01 đã chốt:
- Hàng vật lý mới, cũ và đồ sưu tầm thông thường.
- Nhóm ưu tiên: đồ gia dụng, điện tử, thời trang, sách, đồ sưu tầm thông thường.
- Giới hạn giá khởi điểm tối thiểu 10.000 VND (P-06).

Danh mục cấm và hạn chế chưa chốt, nên tầng A phải duyệt thủ công 100% tin đầu tiên của mỗi người bán và mọi tin bị gắn cờ (P-04).

### 4.3. Loại người bán trong MVP

Cả bốn loại (cá nhân, shop, doanh nghiệp, nhà phân phối) dùng cùng chức năng đăng bán cơ bản, khác nhau ở thông tin xác minh (P-01). Tầng A chỉ mở cho cá nhân và shop để giảm phạm vi xác minh; doanh nghiệp và nhà phân phối vào sau khi có quy trình xác minh tổ chức.

**Đề xuất M-S1:** tầng A chỉ mở cho cá nhân và shop. Cần PO duyệt.

### 4.4. Thời lượng và quy tắc đấu giá

- Thời lượng phiên: 3, 5 hoặc 7 ngày, mặc định 7 ngày (P-05).
- Giá khởi điểm và giá đặt: số nguyên VND, bội số 1.000 VND (P-06).
- Bậc bước giá theo bảng ở P-06 của file 02.
- Gia hạn 2 phút cuối theo BR-17 đã chốt.
- Không đặt cọc (P-07). Không giá bảo lưu, không tự trả giá hộ (đã chốt).
- Người mua không tự rút giá; vận hành có thể hủy lượt giá có lý do (P-08).
- Mua ngay: chỉ hiển thị trước lượt giá hợp lệ đầu tiên; giữ chỗ 10 phút; khôi phục phiên có giới hạn (P-10).

### 4.5. Quy tắc thời gian

Thời điểm máy chủ là chuẩn duy nhất (BR-12, NFR-01). Mọi tranh chấp về thời điểm đặt giá được xử lý bằng nhật ký máy chủ, không dùng đồng hồ thiết bị người mua.

## 5. Ngoài phạm vi MVP

| Hạng mục | Lý do | Mã tham chiếu |
|---|---|---|
| Tự giữ tiền trong tài khoản dự án hoặc ví nội bộ | Vướng pháp lý, không được phép theo mục tiêu đã chốt | 02 mục 2.2, FR-41 |
| Đấu giá nhiều lô, đấu giá ngược | Làm tăng số nhánh trạng thái đáng kể | 02 mục 2.2 |
| Tự động đặt giá hộ, giá bảo lưu | Đã chốt loại bỏ cho MVP | D-02 |
| Nhập catalog hàng loạt, API đối tác, app di động riêng | Không cần thiết để chứng minh luồng lõi | 01 mục 9.3 |
| Nhiều nhân viên cho một shop | Cần phân quyền riêng | 01 mục 9.3 |
| Tài sản phải sang tên, hàng số, dịch vụ, hàng dễ hỏng | Cần quy trình và giấy phép riêng | P-02 |
| Tự giao / gặp mặt | Thiếu bằng chứng độc lập | P-13 |
| Đặt cọc, điểm phạt tự động | Chưa có dữ liệu thử nghiệm | P-07 |
| Đa tiền tệ, quốc tế, livestream | Không thuộc phạm vi thị trường đầu tiên | 01 mục 9.3 |
| Gợi ý cá nhân hóa, chống gian lận nâng cao | Ưu tiên quy tắc thủ công trước | 01 mục 9.3 |

## 6. Luồng MVP từ đầu đến cuối

Luồng dưới đây áp dụng cho cả hai tầng; khác biệt được ghi chú ở từng bước.

1. **Đăng ký:** người dùng đăng ký, xác thực email và số điện thoại trước khi đặt giá (FR-01, P-01). Đồng ý điều khoản và hệ thống lưu phiên bản điều khoản (BR-05).
2. **Tạo hồ sơ người bán:** chọn cá nhân hoặc shop; nộp thông tin xác minh tối thiểu. Trạng thái: `chưa xác minh → đang xét → đạt / bị từ chối` (FR-03).
3. **Đăng hàng:** tạo bản nháp với các trường bắt buộc, ảnh thực tế, tình trạng, khiếm khuyết, phí vận chuyển, chính sách trả hàng (FR-06, P-03). Xem lại tổng thông tin người mua sẽ thấy (FR-07).
4. **Duyệt tin:** tin vào `chờ duyệt`. Vận hành duyệt thủ công tin đầu tiên và tin bị gắn cờ (FR-09, P-04). Tin không đạt được giữ `cần sửa` kèm lý do (FR-08).
5. **Mở phiên:** phiên được mở theo thời điểm đã công bố. Hệ thống chụp lại quy tắc áp dụng (FR-12).
6. **Đặt giá:** người mua gửi giá; hệ thống trả `được chấp nhận` hoặc `bị từ chối` kèm lý do (FR-14, FR-15). Gia hạn 2 phút được áp dụng nếu có (FR-13, BR-17).
7. **Mua ngay (nếu bật):** chỉ khả dụng trước lượt giá hợp lệ đầu tiên; giữ chỗ 10 phút (FR-38 đến FR-40).
8. **Đóng phiên:** khóa nhận giá, xác định kết quả một lần, lưu bằng chứng (FR-17, FR-18, BR-19).
9. **Tạo giao dịch:** chỉ khi có người thắng hợp lệ; giao dịch gắn với phiên, người thắng, giá chốt và phiên bản điều kiện (FR-20).
10. **Thanh toán:**
   - Tầng A: người thắng tự khai đã chuyển khoản ngoài nền tảng. Hệ thống ghi nhận là "người thắng khai, chưa đối soát". Trạng thái này không được coi là `đã thanh toán` theo BR-22 (M-D2).
   - Tầng B: người thắng trả qua đối tác trong 48 giờ; chỉ đổi trạng thái sau xác nhận từ đối tác (P-11, P-12, BR-22).
11. **Giao hàng:** người bán chọn đơn vị vận chuyển được chấp nhận, bàn giao trong 3 ngày làm việc (P-13). Tầng A: người bán tự khai, hiển thị rõ "tự khai". Tầng B: trạng thái lấy từ nhà vận chuyển.
12. **Kiểm tra hàng và hoàn tất:** 7 ngày lịch sau giao được xác minh (P-15). Không có tranh chấp thì hoàn tất.
13. **Tranh chấp (nếu có):** mở trong 7 ngày lịch, người bán phản hồi trong 3 ngày làm việc, vận hành quyết định trong mục tiêu 5 ngày làm việc (P-16, P-17).
14. **Đánh giá:** mỗi bên đánh giá đối tác một lần trong 30 ngày (P-18).

## 7. Tiêu chí vào và ra cho từng bước

### 7.1. Tiêu chí để bắt đầu thử nghiệm tầng A

Tất cả phải đạt:
- PO đã duyệt file này và các quyết định M-D1, M-D2, M-S1.
- Danh mục hàng cho thử nghiệm đã chốt, kèm danh sách hàng cấm tối thiểu.
- Quy chế hoạt động, điều khoản giao dịch và chính sách bảo vệ dữ liệu cá nhân đã được soạn. Chưa cần rà pháp lý sâu hơn cho tầng A, nhưng phải có văn bản.
- Có ít nhất 20 kịch bản kiểm thử cho luồng đấu giá, trong đó có các kịch bản đặt giá đồng thời và đặt giá sát giờ (mục 9).
- Có người phụ trách vận hành duyệt tin và xử lý tranh chấp trong giờ làm việc.

### 7.2. Tiêu chí để mở tầng B

Tất cả phải đạt, và đây là cổng phát hành:
- Đối tác giữ tiền đã ký hợp đồng, hỗ trợ nhiều người bán, có đối soát, giải ngân, hoàn tiền và xử lý chargeback (BR-24, D-04).
- Đã có kết quả rà soát pháp lý về việc giữ tiền, phân loại mô hình đấu giá theo Luật Đấu giá tài sản và Luật TMĐT 2025 (BR-32).
- Đã thử thành công việc xác nhận và hủy giữ chỗ mua ngay với đối tác (P-10).
- Đã thử xác nhận thanh toán trùng lặp và phản hồi đến muộn (FR-23).

Nếu không đạt, không tự chuyển sang thu tiền vào tài khoản cá nhân hoặc trả thẳng người bán (file 02, mục 9.3).

## 8. Số liệu và chỉ số đánh giá MVP

Các chỉ số dưới đây khớp với file 01 mục 8. Ngưỡng mục tiêu chưa chốt, và cần PO quyết định cùng quy mô thử nghiệm (D-07).

| Chỉ số | Định nghĩa thao tác | Ghi chú |
|---|---|---|
| Phiên có lượt giá hợp lệ | Số phiên kết thúc có ít nhất một giá hợp lệ / tổng phiên kết thúc | Mẫu số là phiên đã kết thúc |
| Phiên có người thắng | Số phiên có người thắng / phiên có lượt giá hợp lệ | |
| Thắng dẫn đến thanh toán | Giao dịch có nguồn đối soát đáng tin cậy / giao dịch có người thắng. Ở tầng A, người thắng tự khai không được tính | Tách riêng tầng A và B; tầng A có thể không có số này nếu không có đối soát |
| Tranh chấp | Số tranh chấp mở / giao dịch đã giao | |
| Tính đúng đắn | Số kết quả khớp quy tắc / tổng kết quả kiểm tra | Kiểm tra lại bằng nhật ký |
| Giờ hỗ trợ thủ công | Tổng giờ vận hành / số giao dịch | |

## 9. Điều kiện nghiệm thu MVP

MVP được coi là đạt để mở rộng khi:

1. Toàn bộ kịch bản kiểm thử ở mục 7 của file 02 (11 kịch bản) đều đạt.
2. Kiểm thử đồng thời: ít nhất 50 yêu cầu đặt giá gửi cùng một phiên trong cùng một giây; chỉ một thứ tự chính thức, không có hai người thắng. (Con số này là đề xuất BA, chờ D-07.)
3. Kiểm thử gia hạn sát giờ: nhiều lượt hợp lệ liên tiếp trong 2 phút cuối, giờ đóng mới đúng công thức.
4. Không có lỗi mất dữ liệu lượt giá đã được xác nhận trong thử nghiệm.
5. Mọi thay đổi trọng yếu (giá, kết quả, trạng thái thanh toán, vận chuyển, tranh chấp, kiểm duyệt) có nhật ký (FR-36).
6. Thời gian xử lý tranh chấp trung bình nằm trong mục tiêu 5 ngày làm việc, hoặc có lý do ghi nhận.

## 10. Rủi ro riêng của MVP

| Rủi ro | Mức | Cách giảm |
|---|---|---|
| Đấu giá có thể thuộc diện đấu giá tài sản cần tổ chức được cấp phép | Cao | Rà pháp lý trước khi mở tầng A cho người dùng ngoài vòng kín |
| Người dùng hiểu nhầm nền tảng bảo vệ tiền ở tầng A | Cao | Cảnh báo rõ trên trang phiên và trang thanh toán |
| Người thắng bỏ thanh toán, đặc biệt khi không đặt cọc (P-07) | Cao | Tầng A đo tỷ lệ bỏ; chọn cách kiểm soát ở D-08 (file 02, mục 9.5) trước khi mở tầng B |
| Ít người mua, phiên không có lượt giá | Trung bình | Thử nghiệm kín với số lượng phiên giới hạn, đo tỷ lệ có lượt giá |
| Đặt giá sát giờ làm hệ thống quá tải hoặc sai kết quả | Trung bình | Kiểm thử đồng thời (mục 9) |
| Đặt giá ảo, tài khoản giả | Trung bình | Quy tắc thủ công ở mục 11 |
| Tranh chấp vượt khả năng xử lý thủ công | Thấp đến trung bình | Giới hạn số phiên đồng thời trong thử nghiệm |

## 11. Quy tắc chống đặt giá ảo ở mức thủ công (đề xuất bổ sung)

Vì BR-03 hiện chỉ chặn người bán tự đặt giá, MVP nên bổ sung:
- Vận hành kiểm tra phiên khi có nhiều tài khoản mới đặt giá sát giờ.
- Vận hành kiểm tra khi các tài khoản có cùng thiết bị, cùng địa chỉ giao hàng hoặc cùng số điện thoại đặt giá trên cùng phiên.
- Phiên bị nghi ngờ được tạm dừng và chuyển sang xem xét (FR-35), không tự động hủy kết quả.

Đây là đề xuất mới, cần PO duyệt và cần được thêm thành BR khi duyệt.

## 12. Các việc cần làm để đưa file này vào hiệu lực

1. PO duyệt hoặc chỉnh M-D1, M-D2, M-D3, M-S1 và mục 11.
2. Cập nhật mục 9.2 của file 01 để trỏ sang file này.
3. Cập nhật trạng thái P-02 đến P-10 trong file 02 khi PO duyệt.
4. Chốt danh mục hàng thử nghiệm và danh mục cấm tối thiểu.
5. Bắt đầu rà pháp lý về đấu giá tài sản và trung gian thanh toán, không chờ đến khi viết xong tầng B.
6. Liên hệ ít nhất hai đối tác giữ tiền để hỏi điều kiện hợp tác và thời gian tích hợp.
7. PO quyết định D-08 (cách kiểm soát người thắng bỏ thanh toán) trước khi chốt thiết kế luồng thanh toán tầng B.

## 13. Câu hỏi mở

1. Thời lượng thử nghiệm kín bao lâu, bao nhiêu phiên và bao nhiêu người tham gia?
2. Ai là người có quyền duyệt tin và ra quyết định tranh chấp trong thử nghiệm?
3. Có cần xác minh danh tính (CCCD) ngay ở tầng A không, hay chỉ xác minh số điện thoại và email?
4. Cảnh báo "không có bảo vệ tiền" ở tầng A cần nội dung pháp lý như thế nào?
5. Khi tầng A kết thúc, dữ liệu thử nghiệm được chuyển sang tầng B hay bị xóa theo chính sách lưu trữ nào?

## 14. Kịch bản kiểm thử chi tiết

Quy ước: mỗi kịch bản có mã `TC`, trỏ về mã FR/BR, nêu điều kiện đầu vào, thao tác, kết quả mong đợi. Tầng ghi trong ngoặc: `[A]` áp dụng cho thử nghiệm kín, `[B]` chỉ áp dụng khi mở thanh toán bảo đảm, `[A,B]` áp dụng cả hai. Các giá trị số là ví dụ, không phải quy định cố định.

### 14.1. Tài khoản và xác thực (FR-01, FR-02, FR-05, P-01)

| TC | Điều kiện | Thao tác | Kết quả mong đợi |
|---|---|---|---|
| TC-01 `[A,B]` | Email mới chưa xác thực | Đăng ký rồi cố đặt giá | Hệ thống chặn đặt giá, yêu cầu xác thực email |
| TC-02 `[A,B]` | Số điện thoại chưa xác thực | Cố đặt giá | Chặn đặt giá, yêu cầu xác thực số điện thoại |
| TC-03 `[A,B]` | Tài khoản bị khóa | Gửi lượt đặt giá trên phiên đang mở | Từ chối với lý do "tài khoản bị hạn chế", giá dẫn đầu không đổi (BR-02) |
| TC-04 `[A,B]` | Người dùng chưa đồng ý điều khoản | Đăng bán hoặc đặt giá | Chặn, hiển thị điều khoản; sau khi đồng ý, hệ thống lưu phiên bản điều khoản (BR-05) |
| TC-05 `[A,B]` | Người dùng ở trang công khai, chưa đăng nhập | Xem tin, tìm kiếm, bấm đặt giá | Xem được tin; bấm đặt giá chuyển sang đăng nhập; không có quyền đăng bán |
| TC-06 `[A,B]` | Người dùng đổi thông tin hồ sơ sau khi đã có giao dịch | Sửa tên hoặc địa chỉ | Giao dịch cũ giữ thông tin tại thời điểm chốt (FR-02) |
| TC-07 `[A,B]` | Người dùng xem hồ sơ của người bán khác | Mở trang hồ sơ | Chỉ thấy trạng thái xác minh và đánh giá công khai, không thấy giấy tờ hoặc số định danh (FR-05, BR-30) |

### 14.2. Xác minh người bán (FR-03, FR-04, BR-04)

| TC | Điều kiện | Thao tác | Kết quả mong đợi |
|---|---|---|---|
| TC-08 `[A]` | Hồ sơ mới chưa xác minh | Cố đăng bán | Chặn, hiển thị trạng thái `chưa xác minh` và bước cần làm |
| TC-09 `[A]` | Hồ sơ đang xét | Cố đăng bán | Chặn, hiển thị `đang xét` và thời gian dự kiến |
| TC-10 `[A]` | Vận hành duyệt hồ sơ | Chuyển sang `đạt` | Được đăng bán; trạng thái hiển thị với người mua |
| TC-11 `[A]` | Hồ sơ bị từ chối | Cố đăng bán | Chặn, hiển thị lý do và cách nộp lại |
| TC-12 `[A]` | Hồ sơ đã đạt nhưng hết hiệu lực | Cố đăng bán | Chuyển sang `cần xác minh lại` và chặn đăng bán mới |
| TC-13 `[A]` | Người dùng chọn loại doanh nghiệp hoặc nhà phân phối | Nộp hồ sơ | Hệ thống từ chối hoặc đưa vào hàng chờ, vì M-S1 chưa mở các loại này |

### 14.3. Đăng hàng và duyệt tin (FR-06 đến FR-11, P-02 đến P-04)

| TC | Điều kiện | Thao tác | Kết quả mong đợi |
|---|---|---|---|
| TC-14 `[A,B]` | Bản nháp thiếu tiêu đề | Gửi duyệt | Báo lỗi đúng trường, tin không vào `chờ duyệt` (BR-06) |
| TC-15 `[A,B]` | Bản nháp đủ trường bắt buộc | Gửi duyệt | Tin vào `chờ duyệt`; không mở phiên khi chưa duyệt |
| TC-16 `[A,B]` | Danh mục bị cấm | Chọn danh mục đó | Chặn hoặc hiển thị thông báo không được đăng |
| TC-17 `[A,B]` | Tin thứ nhất của người bán mới | Gửi duyệt | Vào hàng duyệt thủ công bắt buộc (P-04) |
| TC-18 `[A,B]` | Tin bị gắn cờ | Gửi duyệt | Vào hàng duyệt thủ công |
| TC-19 `[A,B]` | Vận hành yêu cầu sửa | Duyệt tin | Tin ở `cần sửa` kèm lý do; người bán nhận thông báo (FR-08, FR-09) |
| TC-20 `[A,B]` | Tin chưa có giá | Người bán sửa mô tả, không ảnh hưởng giá | Lưu được, có phiên bản mới (P-04) |
| TC-21 `[A,B]` | Tin đã có lượt giá hợp lệ đầu tiên | Người bán sửa giá khởi điểm hoặc mô tả trọng yếu | Hệ thống khóa trường đó; sai sót trọng yếu chỉ được sửa qua vận hành (FR-11, BR-09) |
| TC-22 `[A,B]` | Người bán xem trang xác nhận trước khi gửi | Mở bước tổng hợp | Thấy giá, phí vận chuyển dự kiến, chính sách trả hàng và điều kiện giao dịch (FR-07) |
| TC-23 `[A,B]` | Người mua xem tin | Mở trang tin | Thấy mô tả, người bán, giá, mốc thời gian, chi phí bổ sung và quy tắc phiên (FR-10) |
| TC-24 `[A,B]` | Người bán cố tự đặt giá trên phiên của mình | Gửi lượt đặt giá | Từ chối (BR-03) |

### 14.4. Tìm kiếm cơ bản (FR-10)

| TC | Điều kiện | Thao tác | Kết quả mong đợi |
|---|---|---|---|
| TC-25 `[A,B]` | Có tin đã duyệt | Tìm theo từ khóa | Trả về tin khớp, không trả tin chưa duyệt hoặc đã gỡ |
| TC-26 `[A,B]` | Có tin ở nhiều danh mục | Lọc theo danh mục | Chỉ hiện tin thuộc danh mục đã chọn |
| TC-27 `[A,B]` | Có tin đang mở và đã kết thúc | Lọc theo trạng thái | Đúng trạng thái được chọn |
| TC-28 `[A,B]` | Từ khóa không có kết quả | Tìm kiếm | Hiển thị trạng thái rỗng, không lỗi |

### 14.5. Đấu giá và đặt giá (FR-12 đến FR-19, BR-12 đến BR-19, P-05, P-06, P-08)

Đây là nhóm quan trọng nhất. Giá khởi điểm dùng làm ví dụ là 100.000 VND, bước giá 10.000 VND (bậc 100.000 đến dưới 1.000.000).

| TC | Điều kiện | Thao tác | Kết quả mong đợi |
|---|---|---|---|
| TC-29 `[A,B]` | Phiên mở, chưa có giá | Đặt 100.000 VND | Chấp nhận (lượt đầu bằng giá khởi điểm) |
| TC-30 `[A,B]` | Phiên mở, chưa có giá | Đặt 95.000 VND | Từ chối, lý do dưới giá khởi điểm |
| TC-31 `[A,B]` | Giá dẫn đầu 100.000 VND | Đặt 109.000 VND | Từ chối, lý do dưới giá tối thiểu 110.000 VND (P-06) |
| TC-32 `[A,B]` | Giá dẫn đầu 100.000 VND | Đặt 110.000 VND | Chấp nhận; lịch sử ghi đúng một lần; người dẫn đầu mới là người này |
| TC-33 `[A,B]` | Người đang dẫn đầu | Đặt tiếp | Từ chối; không tự nâng giá của mình |
| TC-34 `[A,B]` | Giá dẫn đầu 110.000 VND | Hai người cùng đặt 120.000 VND gần nhau | Chỉ lượt được ghi nhận trước được chấp nhận; lượt sau bị từ chối vì không còn đạt giá tối thiểu (BR-13, BR-14) |
| TC-35 `[A,B]` | Phiên đã đóng | Đặt giá | Từ chối, giá dẫn đầu không đổi (FR-15) |
| TC-36 `[A,B]` | Tài khoản bị khóa | Đặt giá | Từ chối (BR-02) |
| TC-37 `[A,B]` | Đặt giá trong 2 phút cuối, giờ đóng 20:00:00 | Giá hợp lệ lúc 19:59:30 | Giờ đóng mới 20:01:30; hiển thị cho người tham gia (BR-17) |
| TC-38 `[A,B]` | Giờ đóng 20:01:30 | Giá hợp lệ lúc 20:00:45 | Giờ đóng mới 20:02:45 |
| TC-39 `[A,B]` | Giờ đóng 20:00:00 | Giá đến lúc 20:00:01 | Từ chối, không gia hạn |
| TC-40 `[A,B]` | Giá bị từ chối vì quá thấp, trong 2 phút cuối | Gửi giá đó | Không gia hạn (giá không hợp lệ) |
| TC-41 `[A,B]` | Hai yêu cầu đặt giá gửi cùng lúc | Gửi đồng thời | Một thứ tự chính thức; không có hai người thắng; cả hai nhận kết quả rõ ràng (NFR-01, mục 6 file 02) |
| TC-42 `[A,B]` | Đóng phiên có người dẫn đầu | Hệ thống đóng phiên | Có đúng một người thắng và một giao dịch |
| TC-43 `[A,B]` | Đóng phiên không có giá hợp lệ | Hệ thống đóng phiên | Không tạo người thắng hay giao dịch; thông báo người bán (BR-18) |
| TC-44 `[A,B]` | Tiến trình đóng phiên chạy lặp | Chạy đóng phiên hai lần | Vẫn chỉ có một người thắng và một giao dịch (BR-19) |
| TC-45 `[A,B]` | Vận hành hủy một lượt giá vì nhập nhầm | Hủy có lý do | Lượt bị hủy có nhật ký; giá dẫn đầu được tính lại từ lịch sử hợp lệ (P-08) |
| TC-46 `[A,B]` | Người mua muốn rút giá | Gửi yêu cầu rút | Hệ thống không tự rút; chuyển cho vận hành (P-08) |
| TC-47 `[A,B]` | Người bán dừng tin trước lượt giá đầu tiên | Bấm dừng | Tin dừng, không mở phiên (P-09) |
| TC-48 `[A,B]` | Người bán cố dừng sau lượt giá đầu tiên | Bấm dừng | Không cho phép; chỉ vận hành được dừng có căn cứ (BR-10) |
| TC-49 `[A,B]` | Phiên bị dừng bởi vận hành | Xem trang phiên | Có lý do công bố, lượt giá cũ không tự chuyển thành giao dịch (FR-19) |

### 14.6. Mua ngay (FR-38 đến FR-40, BR-35 đến BR-37, P-10)

Chỉ chạy kịch bản này khi PO bật mua ngay trong MVP. Nếu tắt, bỏ qua nhóm này.

| TC | Điều kiện | Thao tác | Kết quả mong đợi |
|---|---|---|---|
| TC-50 `[A,B]` | Người bán bật mua ngay, chưa có giá | Xem trang phiên | Hiển thị giá mua ngay, tổng chi phí dự kiến và điều kiện thanh toán bên cạnh đặt giá (FR-38) |
| TC-51 `[A,B]` | Giá mua ngay 105.000 VND, chưa có giá | Xác nhận mua ngay | Giữ chỗ 10 phút; tạm dừng đồng hồ phiên; người khác không đặt giá được |
| TC-52 `[A,B]` | Đang giữ chỗ mua ngay | Thanh toán được đối tác xác nhận trong 10 phút | Tạo đúng một giao dịch ở giá mua ngay (P-10) |
| TC-53 `[A,B]` | Đang giữ chỗ mua ngay | Hết 10 phút, không thanh toán | Trả trạng thái chưa có giá; mở lại với ít nhất 2 phút còn lại; không có người thắng giả |
| TC-54 `[A,B]` | Đã có lượt giá hợp lệ đầu tiên | Thử mua ngay | Lựa chọn mua ngay không hiển thị; yêu cầu gửi lên bị từ chối (BR-37) |
| TC-55 `[A,B]` | Giữ chỗ mua ngay và lượt giá đến gần cùng lúc | Gửi đồng thời | Chỉ một kết quả bán chính thức; giờ trên thiết bị không được dùng để phân xử (BR-36) |
| TC-56 `[A,B]` | Đã có một lần giữ chỗ thất bại trên phiên | Thử giữ chỗ lần nữa | Từ chối (P-10: mỗi tài khoản một lần thất bại cho một phiên) |

### 14.7. Tạo giao dịch và thanh toán (FR-20 đến FR-25, BR-21 đến BR-24)

| TC | Điều kiện | Thao tác | Kết quả mong đợi |
|---|---|---|---|
| TC-57 `[A,B]` | Phiên có người thắng | Hệ thống tạo giao dịch | Giao dịch gắn đúng phiên, người thắng, người bán, giá chốt và phiên bản điều kiện (FR-20) |
| TC-58 `[A,B]` | Giao dịch vừa tạo | Xem thông tin người thắng | Thấy số tiền, phí vận chuyển nếu có và hạn thanh toán (FR-21) |
| TC-59 `[A]` | Người thắng bấm "đã chuyển khoản ngoài nền tảng" | Xác nhận | Ghi nhận `người thắng khai, chưa đối soát`; không ghi `đã thanh toán`; không chuyển sang `đã giải ngân`; không tính vào chỉ số thanh toán (BR-22, M-D2) |
| TC-60 `[A]` | Người thắng tải trang thành công | Không có xác nhận từ nguồn | Không đổi trạng thái thanh toán (BR-22) |
| TC-61 `[B]` | Đối tác báo thanh toán thành công | Nhận sự kiện | Ghi `đã trả`, lưu mã tham chiếu đối soát (FR-22) |
| TC-62 `[B]` | Đối tác gửi cùng một sự kiện hai lần | Nhận sự kiện trùng | Chỉ một bản ghi, không tạo thêm giao dịch (FR-23) |
| TC-63 `[B]` | Sự kiện thanh toán đến muộn, sau khi giao dịch đã quá hạn | Nhận sự kiện | Ghi nhận để đối soát thủ công; không tự chuyển trạng thái sai (FR-23, FR-24) |
| TC-64 `[B]` | Người thắng không thanh toán sau 48 giờ | Quá hạn | Hủy giao dịch có lý do; thông báo người bán; không tự trao quyền cho người đặt giá thứ hai (P-11, FR-24) |
| TC-65 `[B]` | 24 giờ chưa thanh toán | Đến mốc nhắc | Người thắng nhận nhắc nhở (P-11) |
| TC-66 `[B]` | Tiền đã vào tài khoản bảo đảm | Hệ thống cập nhật | Ghi `đang giữ`; người bán thấy khoản dự kiến nhận và lý do chưa giải ngân (FR-41) |
| TC-67 `[B]` | Lệnh giải ngân gửi hai lần | Gửi lặp | Chỉ một khoản chi trả (FR-42, BR-38) |

### 14.8. Giao hàng (FR-26 đến FR-29, P-13, P-14)

| TC | Điều kiện | Thao tác | Kết quả mong đợi |
|---|---|---|---|
| TC-68 `[A,B]` | Giao dịch đã thanh toán (hoặc đã xác nhận thử nghiệm ở tầng A) | Người bán xem trang giao hàng | Thấy địa chỉ giao hàng và hạn bàn giao 3 ngày làm việc (FR-26) |
| TC-69 `[A,B]` | Người bán nhập mã vận đơn | Lưu | Trạng thái `đã bàn giao`, nguồn ghi là "người bán khai" (FR-28) |
| TC-70 `[A,B]` | Không có mã vận đơn quá 3 ngày làm việc | Đến hạn | Chuyển sang trạng thái ngoại lệ; người mua được mở yêu cầu (P-13, FR-32) |
| TC-71 `[B]` | Nhà vận chuyển cập nhật giao thành công | Nhận cập nhật | Trạng thái `đã giao` ghi nguồn "nhà vận chuyển xác nhận" (BR-25) |
| TC-72 `[A]` | Người bán tự đánh dấu đã giao | Bấm xác nhận | Ghi nguồn "tự khai, chưa đối soát"; không bắt đầu tính 7 ngày như giao đã xác minh (BR-25) |
| TC-73 `[A,B]` | Giao hàng xác minh xong | Đủ 7 ngày lịch không tranh chấp | Giao dịch chuyển `hoàn tất` (P-15, FR-29) |
| TC-74 `[A,B]` | Người mua bấm "đã nhận" sớm | Xác nhận | Không rút ngắn 7 ngày (P-15) |
| TC-75 `[A,B]` | Giao thành công về vận chuyển nhưng người mua mở tranh chấp trong 7 ngày | Mở tranh chấp | Không hoàn tất tự động (FR-29) |

### 14.9. Tranh chấp (FR-30 đến FR-32, P-16, P-17, BR-27, BR-28, BR-39)

| TC | Điều kiện | Thao tác | Kết quả mong đợi |
|---|---|---|---|
| TC-76 `[A,B]` | Giao dịch đã giao, trong 7 ngày | Người mua mở tranh chấp, kèm lý do và ảnh | Cấp mã theo dõi, khóa bằng chứng, thông báo người bán (FR-30) |
| TC-77 `[A,B]` | Tranh chấp đang mở | Người bán không phản hồi trong 3 ngày làm việc | Vụ chuyển sang trạng thái ưu tiên cho vận hành; giải ngân vẫn bị chặn (P-16) |
| TC-78 `[A,B]` | Tranh chấp đang mở | Thử giải ngân | Bị chặn; lý do hiển thị |
| TC-79 `[A,B]` | Vận hành yêu cầu thêm chứng cứ | Gửi yêu cầu | Các bên nhận thông báo; hạn phản hồi hiển thị (FR-31) |
| TC-80 `[A,B]` | Vận hành quyết định hoàn một phần | Xác nhận quyết định | Ghi lý do, căn cứ, người quyết định; hoàn đúng số tiền; không hoàn lặp (FR-31, BR-38) |
| TC-81 `[A,B]` | Một bên kháng nghị trong 48 giờ | Gửi kháng nghị kèm chứng cứ mới | Tiền vẫn bị chặn; kháng nghị được xem xét (P-16) |
| TC-82 `[A,B]` | Kháng nghị gửi sau 48 giờ | Gửi | Từ chối với lý do hết hạn |
| TC-83 `[B]` | Giao dịch đã hoàn tất và đã giải ngân | Người mua mở tranh chấp | Đi theo quy trình riêng; không hứa thu hồi ngay (P-17) |
| TC-84 `[A,B]` | Tranh chấp và giải ngân đến gần như cùng lúc | Gửi đồng thời | Không chi trả trái chính sách; có lịch sử xử lý để đối soát |

### 14.10. Đánh giá, báo cáo và vận hành (FR-33 đến FR-37, P-18, P-20)

| TC | Điều kiện | Thao tác | Kết quả mong đợi |
|---|---|---|---|
| TC-85 `[A,B]` | Giao dịch đã hoàn tất | Người mua đánh giá người bán 5 sao | Lưu; không sửa được sau khi gửi (P-18) |
| TC-86 `[A,B]` | Đã đánh giá một lần | Thử đánh giá lại | Từ chối |
| TC-87 `[A,B]` | Giao dịch đang tranh chấp | Đánh giá | Đánh giá được giữ ẩn đến khi vụ việc đóng (P-18) |
| TC-88 `[A,B]` | Quá 30 ngày kể từ hoàn tất | Đánh giá | Từ chối |
| TC-89 `[A,B]` | Người dùng báo cáo tin | Gửi báo cáo | Vận hành nhận hồ sơ kèm trạng thái xử lý (FR-34) |
| TC-90 `[A,B]` | Vận hành tạm ẩn tin | Thực hiện với lý do | Tin ẩn; người bán được thông báo; có nhật ký (FR-09, FR-36) |
| TC-91 `[A,B]` | Vận hành khóa quyền đặt giá của một tài khoản đang có lượt giá trong phiên | Thực hiện | Không tự sửa lượt giá cũ; tác động lên phiên được xem xét riêng (P-20, FR-35) |
| TC-92 `[A,B]` | Bất kỳ thay đổi trọng yếu nào | Thực hiện | Nhật ký ghi tác nhân, thời điểm, trước và sau, lý do (FR-36) |
| TC-93 `[A,B]` | Cuối ngày | Mở báo cáo vận hành | Có số phiên mở, kết thúc, có giá, có người thắng, thanh toán, hoàn tất, hủy, tranh chấp (FR-37) |

### 14.11. Chống đặt giá ảo ở mức thủ công (mục 11 của file này)

| TC | Điều kiện | Thao tác | Kết quả mong đợi |
|---|---|---|---|
| TC-94 `[A,B]` | Ba tài khoản mới cùng đặt giá trong 2 phút cuối | Vận hành xem báo cáo | Báo cáo đánh dấu cụm bất thường để kiểm tra |
| TC-95 `[A,B]` | Hai tài khoản cùng số điện thoại hoặc cùng địa chỉ giao hàng | Đặt giá trên cùng phiên | Đánh dấu cho vận hành; không tự hủy kết quả (FR-35) |

### 14.12. Ngoài phạm vi tầng A và giới hạn kiểm thử

- Các kịch bản `[B]` không chạy ở tầng A.
- Kịch bản tải (50 yêu cầu đồng thời ở mục 9) là đề xuất của BA, chờ D-07. Nếu PO chọn quy mô khác, sửa lại con số trong mục 9 và TC-41.
- Kịch bản mua ngay (nhóm 14.6) chỉ chạy khi PO bật mua ngay trong MVP.
- Kịch bản pháp lý và đối soát với đối tác không nằm trong bảng này, mà thuộc kế hoạch thử nghiệm riêng ở file 05.

**Tổng số:** 95 kịch bản. Có 9 kịch bản chỉ dành cho tầng B (TC-61 đến TC-67, TC-71, TC-83), nên tầng A chạy 86 kịch bản. Nếu PO không bật mua ngay, bỏ thêm 7 kịch bản ở nhóm 14.6 (TC-50 đến TC-56).
