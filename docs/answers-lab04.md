# Lab 04 – Trả lời câu hỏi thảo luận

## 1. Vì sao `release/*` không bao giờ merge ngược vào `main`?

- **`release/labXX` là baseline đã đóng băng.** Nó là ảnh chụp (snapshot) của một commit trên `main` tại thời điểm phát hành, dùng để nộp/đối chiếu/tái tạo đúng phiên bản đã giao. Merge ngược sẽ làm nhánh nộp chứa thêm lịch sử mới ⇒ không còn là ảnh chụp bất biến nữa.
- **Thay đổi trên `release/*` không qua kiểm soát.** `release/*` chỉ nhận thay đổi từ `hotfix/*` (có Issue → PR → review). Nếu merge ngược vào `main`, mọi thứ trên nhánh đó chảy thẳng vào dòng phát triển chính mà không có Issue/PR tương ứng — vi phạm nguyên tắc "mọi thay đổi đi qua Pull Request".
- **Hai dòng phát triển khác mục đích.** `main` là nơi *phát triển tiếp*; `release/*` là nơi *bảo trì bản đã phát hành*. Trộn hai chiều sẽ tạo vòng lặp merge (`main` → release do hotfix, release → main do merge ngược) và làm mọi lần so sánh `A..B` sau này mất ý nghĩa.
- **Định danh phiên bản nằm ở tag, không ở nhánh.** `v1.0.0` là tag annotated bất biến; nhánh `release/lab04` có thể nhận hotfix và tiến lên. Vì vậy "giao hàng" được ghi bằng tag + GitHub Release, còn nhánh release chỉ là *dòng bảo trì*. Nếu merge ngược, người đọc lịch sử sẽ khó biết commit nào thuộc bản phát hành nào.
- Nói ngắn: luồng thay đổi là **một chiều** — `feature/*`, `bugfix/*`, `topic/*` → `main` → (đóng băng thành) `release/*`; và `hotfix/*` → `release/*` + cherry-pick về `main`.

## 2. So sánh Release Flow (học phần) với GitFlow

| Tiêu chí | Release Flow (học phần) | GitFlow |
|---|---|---|
| Nhánh dài hạn | Chỉ `main` | `main` + `develop` |
| Nhánh phát hành | `release/labXX` tạo từ `main`, **không** merge ngược | `release/*` tạo từ `develop`, **merge vào cả `main` và `develop`** |
| Nơi phát triển | `main` (mọi tính năng đi qua PR vào `main`) | `develop` (tính năng vào `develop`, `main` chỉ nhận bản phát hành) |
| Sau khi phát hành | `main` tiếp tục đi trước `release/*` | `main` = bản đã phát hành, `develop` đi tiếp |
| Sửa lỗi khẩn | `hotfix/*` tạo **từ `release/*`**, rồi cherry-pick về `main` | `hotfix/*` tạo **từ `main`**, merge vào `main` + `develop` |
| Độ phức tạp | Nhẹ, ít nhánh, phù hợp nhóm nhỏ / nộp bài theo tuần | Nặng, nhiều nhánh, phù hợp sản phẩm lớn, phát hành định kỳ nhiều môi trường |

**Nhận xét:** Release Flow ở học phần là bản rút gọn một nhánh dài hạn của GitFlow: vẫn giữ được baseline + tag + dòng bảo trì (đủ để kiểm toán cấu hình), nhưng bỏ `develop` nên không phải đồng bộ hai nhánh dài hạn. Điểm khác biệt bản chất là **hướng của luồng merge**: GitFlow để bản phát hành chảy về `main`, học phần đóng băng phát hành thành nhánh riêng và không bao giờ merge ngược.

## 3. Vì sao lên `1.0.0` mà không phải `0.4.0`?

- Theo SemVer, `0.y.z` là **giai đoạn đầu, chưa ổn định**: API có thể đổi ở bất kỳ bản nhỏ nào. `1.0.0` là tuyên bố **API đã ổn định** — từ đây chỉ tăng MINOR khi thêm tính năng tương thích, tăng PATCH khi chỉ sửa lỗi, và tăng MAJOR khi phá vỡ tương thích.
- Ba baseline trước (`v0.1.0` Lab 01, `v0.2.0` Lab 02, `v0.3.0` Lab 03) là các cột mốc còn đang thay đổi liên tục: cấu trúc mã nguồn đổi (refactor), tính năng còn thêm, lỗi còn sửa. Sau Lab 03, nhóm tính năng lõi đã đủ và đã sạch lỗi (`print_cart`, `search_by_title`, `total_cost_with_discount`, giới hạn 20 đĩa, 4 test OK) — đây là bản đầu tiên đủ điều kiện giao cho người dùng.
- `0.4.0` chỉ có nghĩa "thêm một cột mốc nữa trong giai đoạn chưa ổn định", **không** đánh dấu cam kết tương thích. Mốc `1.0.0` còn là điểm mốc kỹ thuật cho các bài sau: Lab 05 sẽ tăng `1.1.0` (thêm tính năng tương thích) và `1.0.1` (hotfix) — đúng hai quy tắc MINOR/PATCH mà chỉ phiên bản `1.x` mới có ý nghĩa.
- Đánh số này cũng nói với người dùng: "an toàn để dùng, chúng tôi cam kết không phá vỡ tương thích trong dòng 1.x".

## 4. Vì sao chuẩn bị phiên bản + CHANGELOG trên `main` trước, không sửa trực tiếp trên `release/lab04`?

- **Sửa trên `release/*` là sửa vào ngõ cụt.** Vì `release/*` không merge ngược vào `main`, mọi commit chỉ nằm trên nhánh release sẽ **vĩnh viễn không có trên dòng phát triển chính** — bản phát hành sau đó thiếu nội dung đó, và `git log main..release/lab04` (phải rỗng) sẽ không còn rỗng nữa.
- **Mọi thay đổi phải đi qua PR.** Quy tắc của học phần: không commit trực tiếp lên `main` và `release/*`. Chuẩn bị trên một nhánh `topic/prepare-release-1.0.0` rồi PR vào `main` cho ta review, mô tả thay đổi, và một commit duy nhất mà ai cũng tra được.
- **Baseline phải trỏ tới một commit đã có trên `main`.** Khi đó `release/lab04` chỉ việc tạo từ `main` và tag `v1.0.0` tại đỉnh nhánh; phiên bản 1.0.0 vừa tồn tại trên dòng phát triển, vừa là điểm đóng băng để kiểm toán.
- **CHANGELOG phải khớp mã nguồn.** Nếu viết CHANGELOG trên nhánh release thì tệp đó không có trên `main`, các bản sau sẽ thấy CHANGELOG "nhảy cóc" (mất mục `[1.0.0]`). Viết trên `main` giữ dòng lịch sử phiên bản liên tục.
