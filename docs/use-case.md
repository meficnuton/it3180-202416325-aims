# AIMS-mini – Use case

## Tác nhân (Actors)

- **Khách hàng (Customer):** người mua đĩa, tương tác với giỏ hàng.
- **Quản trị viên (Admin):** người quản lý danh mục đĩa trong cửa hàng (phạm vi mở rộng).

## Danh sách use case

| Mã | Use case | Tác nhân | Mô tả ngắn |
|---|---|---|---|
| UC01 | Xem danh mục đĩa | Khách hàng | Duyệt các đĩa đang bán trong cửa hàng |
| UC02 | Tìm đĩa theo tiêu đề | Khách hàng | Nhập từ khóa, nhận danh sách đĩa khớp tiêu đề |
| UC03 | Thêm đĩa vào giỏ | Khách hàng | Chọn một đĩa; giỏ chấp nhận tối đa 20 đĩa |
| UC04 | Xem giỏ hàng | Khách hàng | In chi tiết các đĩa trong giỏ, hoặc thông báo giỏ trống |
| UC05 | Tính tổng tiền | Khách hàng | Xem tổng giá trị các đĩa trong giỏ |
| UC06 | Cập nhật danh mục đĩa | Quản trị viên | Thêm/sửa đĩa trong cửa hàng (mở rộng) |

## Luồng chính – UC03: Thêm đĩa vào giỏ

1. Khách hàng chọn một đĩa từ danh mục.
2. Hệ thống kiểm tra số lượng đĩa hiện có trong giỏ.
3. Nếu giỏ chưa đạt 20 đĩa: hệ thống thêm đĩa, thông báo thành công.
4. Nếu giỏ đã đủ 20 đĩa: hệ thống từ chối, thông báo giỏ đầy.

## Quan hệ giữa các use case

- UC04 và UC05 là các use case độc lập nhưng thường được dùng sau UC03.
- UC02 hỗ trợ UC01 (tìm kiếm là một cách duyệt danh mục).
