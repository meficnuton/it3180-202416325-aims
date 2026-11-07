# Lab 02 – Trả lời câu hỏi thảo luận

## 1. Vì sao phải đồng bộ master trước khi gửi PR?

- **PR sạch, dễ review:** nếu nhánh tách từ main cũ, tab *Files changed* sẽ hiện lẫn cả những thay đổi người khác đã merge → reviewer khó phân biệt đâu là thay đổi của mình.
- **Phát hiện xung đột sớm, tại máy mình:** `git merge origin/main` cho mình tự giải quyết conflict trong nhánh riêng, chạy test được, thay vì để PR "This branch has conflicts" rồi phải xử lý vội.
- **Kiểm thử tích hợp (integration test):** merge main vào nhánh rồi chạy `python main.py` / unit test chính là bước xác nhận *tính năng của mình hoạt động cùng mã mới nhất* — thứ mà CI/branch protection sau này sẽ đòi hỏi.
- **Merge sạch = lịch sử gọn:** fast-forward hoặc merge commit rõ ràng, không sinh chuỗi merge rối khiến `git log --graph` khó đọc ở Lab 04–05.
- Nói ngắn: **đồng bộ trước, giải quyết ở local; không để người review làm hộ việc đối chiếu.**

## 2. Khi nào KHÔNG được rebase?

- **Commit/nhánh đã chia sẻ (đã push):** rebase viết lại SHA — mọi người kéo về sẽ lệch lịch sử, phải `--force` đè lên công của người khác. Quy tắc học phần: *viết lại lịch sử (amend, reset, rebase) chỉ trên commit chưa chia sẻ.*
- **Nhánh đang có PR mở mà người khác đã review:** rebase làm mất dấu commit đã review, approval cũ không còn gắn với mã đã duyệt (đúng tinh thần "thứ được duyệt = thứ được tích hợp").
- **Nếu buộc phải rebase nhánh đã push** (ví dụ Phần C của Lab 03) thì dùng `git push --force-with-lease` — không bao giờ `--force` trần.
- Trên `main` và `release/*`: **không bao giờ rebase** — lịch sử ở đó là lịch sử chung; hoàn tác trên nhánh chung dùng `revert` (Lab 03).

## 3. `feature/*` khác `topic/*` ở đâu?

| | `feature/*` | `topic/*` |
|---|---|---|
| Nội dung | Tính năng sản phẩm: thêm/sửa hành vi người dùng thấy được (`feature/cart-print`, `feature/search-by-title`) | Chủ đề kỹ thuật/quy trình: công cụ, tài liệu, cấu hình (`topic/pr-template`, `topic/use-case-diagram`) |
| Ý nghĩa commit | `feat:` | `docs:`, `chore:`, `ci:`… |
| Vòng đời | Thường gắn với Issue/đề xuất tính năng | Việc phụ trợ cho dự án, không đổi hành vi chương trình |

Giống nhau về **quy trình**: đều sống ngắn, tạo từ `main`, merge vào `main` qua PR — trong sơ đồ Release Flow của học phần hai loại này cùng một hàng. Khác nhau chỉ ở **ngữ nghĩa đặt tên**: tên nhánh phải nói lên mục đích, và một nhánh chỉ một mục đích.
