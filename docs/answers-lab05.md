# Lab 05 – Trả lời câu hỏi thảo luận

## 1. Ưu, nhược điểm của **upstream first** so với **release first**

**Upstream first** (Release Flow của Microsoft): sửa lỗi trên dòng phát triển chính (`main`) trước, rồi lan truyền xuống các nhánh `release/*` bằng cherry-pick.

- **Ưu:** `main` không bao giờ thiếu bản sửa ⇒ bản phát hành *sau* mặc định đã sạch lỗi, không phụ thuộc việc nhớ lan truyền; bản sửa được review/kiểm thử trong môi trường mã mới nhất; chỉ có một nguồn sự thật về mã nguồn.
- **Nhược:** vẫn phải cherry-pick thủ công xuống từng nhánh release cũ (vẫn quên được); nếu bản sửa dựa trên mã chỉ có ở `main` thì cherry-pick xuống release cũ sẽ xung đột hoặc không áp dụng được; khó xử lý lỗi *chỉ tồn tại* trên bản đã phát hành (ví dụ lỗi do cấu hình/phiên bản thư viện của bản cũ) vì không được phép sửa trực tiếp trên release.

**Release first** (cách học phần chọn): sửa trực tiếp trên nhánh release đã phát hành → phát hành bản vá (`v1.0.1`) → lan truyền về `main` (và các release khác) bằng cherry-pick.

- **Ưu:** người dùng đang dùng bản đã phát hành được sửa ngay, đúng dòng phiên bản họ đang chạy; bản sửa nằm đúng ngữ cảnh mã của bản cũ nên áp dụng sạch, không cần "hạ cấp" mã từ `main`; phù hợp mô hình nộp/phát hành theo tuần với nhiều bản song song (mỗi tuần một `release/labXX`).
- **Nhược:** **phụ thuộc kỷ luật lan truyền** — quên cherry-pick về `main` thì bản phát hành sau tái phát lỗi; phải kiểm toán định kỳ (`git log --grep "cherry picked from"`, `git cherry -v`, `git tag --contains`) để biết bản sửa đã có ở mọi dòng chưa; mỗi bản sửa có thể phải lặp lại ở nhiều dòng phiên bản.

**Kết luận:** upstream first giảm rủi ro "main thiếu bản sửa" nhưng đòi hỏi `main` luôn phải ổn định và cherry-pick luôn chạy được; release first ưu tiên bản đang chạy thật, đổi lại phải kiểm toán việc lan truyền. Học phần chọn release first vì mục tiêu bài học là **bảo trì nhiều dòng phiên bản song song** và chứng minh được bằng `cherry-pick -x` + `git tag --contains`.

## 2. Nếu quên lan truyền bản sửa sang `release/lab05`, lệnh nào phát hiện?

Hai lệnh ở Phần F phát hiện được, không cần đọc mã:

1. **Vòng lặp kiểm tra hành vi** — `v1.1.0` in ra **`0`** thay vì `1`:
   ```bash
   for ref in v1.0.1 v1.1.0 main; do git switch --detach -q $ref; printf "%-8s " $ref; ... done
   ```
   Vì `release/lab05` được tạo từ `main` trước khi có bản sửa, nên nếu không cherry-pick thì `search_by_title('lion')` trên `v1.1.0` vẫn trả về `[]`.
2. **`git log --all --oneline --grep "cherry picked from commit <FIX_SHA>"`** — chỉ ra **1** kết quả (bản trên `main`) thay vì **2** (thêm bản trên `release/lab05`).

**Lưu ý phân biệt:** `git cherry -v origin/main origin/release/lab05` chỉ hữu ích khi bản sửa *đã* được cherry-pick nhưng nội dung bị lệch (khi đó hiện dấu `+` = "chưa có bản tương đương"); còn khi **quên hẳn** thì commit đó không tồn tại trên nhánh nên `git cherry` không liệt kê gì. Còn `git tag --contains <FIX_SHA>` chỉ ra `v1.0.1` — đúng cả khi đã lan truyền, vì bản trên các dòng khác là **bản sao** (SHA khác), nên lệnh này **không** dùng để phát hiện thiếu lan truyền.
