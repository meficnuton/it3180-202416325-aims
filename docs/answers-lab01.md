# Lab 01 – Trả lời câu hỏi thảo luận

## Câu hỏi nhanh: Cấu hình `--global` được lưu ở đâu? Khác gì so với `--local`?

- `--global`: lưu trong `~/.gitconfig` (trên Windows: `C:\Users\<tên-user>\.gitconfig`) — áp dụng cho **mọi repo** của user.
- `--local`: lưu trong `.git/config` của **từng repo** — chỉ có hiệu lực với repo đó.
- Khi trùng khóa, thứ tự ưu tiên là `system` < `global` < `local` (cấu hình cụ thể hơn ghi đè cái chung hơn). Kiểm tra nguồn của từng cấu hình bằng `git config --list --show-origin`.

## 1. Vì sao dùng `git mv`?

`git mv` thực hiện việc đổi tên/di chuyển tệp **và** đưa thay đổi vào staging chỉ trong một lệnh. Git nhận diện đây là *rename* (chữ R trong `git status`) chứ không phải một cặp xóa + thêm, nhờ đó:

- Trên Pull Request, tab *Files changed* hiển thị "renamed" — người review thấy đúng ý đồ thay đổi, dễ review hơn;
- Lịch sử tệp không bị "đứt": `git log --follow -- aims/cart.py` vẫn lần theo được các commit từ trước khi đổi tên.

Về bản chất `git mv` tương đương `mv` + `git rm` + `git add`, nhưng tường minh và khó quên bước staging hơn.

## 2. `release/lab01` có phải baseline không?

Có. Theo định nghĩa của học phần, baseline là "phiên bản đã thống nhất, chỉ đổi qua quy trình" — được thực hiện bằng **tag hoặc nhánh release**. `release/lab01` được tạo từ master ngay khi kết thúc Lab 01, giữ nguyên và không sửa tiếp (mọi sửa đổi sau này phải theo quy trình hotfix — Lab 05), và chính là phiên bản dùng để nộp bài. Ở Lab 04, baseline này sẽ được "chính thức hoá" bằng tag annotated `v0.1.0`. Việc `git rev-parse origin/master origin/release/lab01` trả về hai mã băm giống nhau chứng minh `release/lab01` đúng là mốc chụp của master tại thời điểm nộp.

## 3. Vì sao không commit thẳng master dù làm một mình?

- **Quy trình không phụ thuộc số người:** master là nhánh phát hành; mọi thay đổi nên đi qua change control (nhánh → PR → review → merge) để có lịch sử truy vết, kiểm toán được và hoàn tác dễ dàng (revert một PR thay vì truy lùng commit lẻ).
- **Chất lượng:** PR là điểm dừng để có "người thứ hai" soi xét (partner, CI, công cụ); commit thẳng master không có review nào cả.
- **Chuẩn bị cho môi trường thật:** từ Lab 02, master bật branch protection — push thẳng sẽ bị chặn; làm đúng nếp ngay từ đầu sẽ không bị động.
- **Điểm chấm:** rubric đánh giá phần "tuân thủ branching policy" (20%) dựa trên việc các thay đổi có đi qua nhánh + PR hay không.
