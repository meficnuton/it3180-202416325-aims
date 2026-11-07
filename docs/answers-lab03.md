# Lab 03 – Trả lời câu hỏi thảo luận

## 1. Merge base là gì?

**Merge base** của hai nhánh là **commit tổ tiên chung gần nhất** mà cả hai nhánh đều kế thừa (best common ancestor). Khi merge, Git dùng ba điểm: **base**, **nhánh A**, **nhánh B** — lấy `diff(base → A)` và `diff(base → B)` rồi hợp nhất hai tập thay đổi (3-way merge).

- Nếu chỉ **một phía** đổi một vùng dòng → Git tự lấy thay đổi đó (auto-merge).
- Nếu **cả hai phía** đổi **cùng vùng dòng** theo hai cách khác nhau → Git không tự quyết định được → **xung đột**, ta phải chọn/gộp ý đồ.
- Nếu merge base **chính là** tip của nhánh kia (nhánh ta đang đứng là hậu duệ trực tiếp) → Git **fast-forward**, không sinh merge commit.

Lệnh xem merge base:

```bash
git merge-base main feature/show-added-title
git log --oneline $(git merge-base main feature/show-added-title)..feature/show-added-title
```

**Liên hệ với lab:** merge base của `feature/show-added-title` và `origin/main` là commit `main` tại thời điểm Dev 2 tạo nhánh. Vì sau đó Dev 1 đã merge `feature/vietnamese-messages` (đổi **cùng dòng** trong `aims/cart.py::add_dvd`), hai phía lệch nhau đúng một dòng → xung đột. Merge base càng **cũ** thì hai diff càng lớn → càng dễ xung đột; vì vậy quy tắc là **đồng bộ `main` sớm** (`git merge origin/main`) hoặc **rebase** để dời nhánh mình lên sát base mới trước khi nhờ review.

## 2. Vì sao `main` / `release/*` phải dùng `revert` chứ không `reset`?

Vì đó là **lịch sử đã chia sẻ**: commit đã push, người khác đã fetch về, PR/tag/release đã trỏ vào các SHA đó.

- `git reset` (và `rebase`, `commit --amend`) **viết lại lịch sử** — dời con trỏ nhánh và tạo SHA mới. Trên nhánh chung, người khác `git pull` về sẽ lệch lịch sử, buộc phải `--force` đè lên công việc của họ → mất commit, mất dấu vết kiểm toán (audit trail). Tag/GitHub Release đã phát hành vẫn trỏ vào SHA cũ ⇒ baseline đã công bố bị "vô hiệu".
- `git revert` **không viết lại lịch sử**: nó tạo một **commit mới đảo ngược** thay đổi đã có. SHA cũ giữ nguyên, mọi người chỉ cần `git pull` là có bản sửa — đúng nguyên tắc *"viết lại lịch sử chỉ trên commit chưa chia sẻ"*.
- Với **merge commit**, revert đặc biệt rẻ: `git revert -m 1 <sha>` là **một lệnh** hoàn tác cả một tính năng đã merge (trong khi revert từng commit của nhánh đã rebase/squash sẽ tốn nhiều lệnh).
- `release/*` là **baseline đã đóng băng** và được branch protection bảo vệ (cấm force push, cấm xoá) ⇒ `revert` là cách sửa duy nhất hợp lệ về mặt quy trình.
- `revert` còn **đảo ngược được** (`git revert` chính commit revert đó) để khôi phục nếu quyết định sai — `reset --hard` thì thay đổi đã biến mất khỏi lịch sử nhánh.

Tóm lại: **commit chưa push → `reset`** cho gọn lịch sử; **`main` / `release/*` → `revert`** qua nhánh `bugfix/*` + PR để giữ lịch sử chung và dấu vết kiểm toán.

## Bảng tóm tắt (dùng cho ảnh chụp nếu cần)

| | `git reset` | `git revert` |
|---|---|---|
| Cơ chế | Dời con trỏ nhánh | Tạo commit đảo ngược |
| Viết lại lịch sử | Có | Không |
| Dùng cho | Commit **chưa push** (nhánh nháp) | `main`, `release/*` — lịch sử chung |
| Có dấu vết để hoàn tác lại | Không (phải nhờ `reflog`) | Có (revert của revert) |
