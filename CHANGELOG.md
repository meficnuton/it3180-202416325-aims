# Changelog

Mọi thay đổi đáng chú ý của **AIMS-mini** được ghi lại trong tệp này.

Định dạng theo [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
phiên bản theo [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.0] - 2026-11-07

### Added

- `Cart.print_cart()`: in chi tiết giỏ hàng, kèm nhánh xử lý giỏ trống
- `search_by_title()`: tìm đĩa theo tiêu đề
- `Cart.total_cost_with_discount(percent)`: tổng tiền sau giảm giá, kiểm tra `percent` trong khoảng 0–100
- `docs/use-case.md`: danh sách use case của AIMS-mini
- `.github/pull_request_template.md`: mẫu mô tả Pull Request
- `docs/answers-lab02.md`, `docs/answers-lab03.md`: trả lời câu hỏi thảo luận

### Fixed

- Giỏ hàng từ chối đĩa thứ 21 (`MAX_NUMBERS_ORDERED = 20`) — #8
- `total_cost_with_discount()` trả về số tiền **sau** giảm và chặn `percent` không hợp lệ

[Unreleased]: https://github.com/meficnuton/it3180-202416325-aims/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/meficnuton/it3180-202416325-aims/releases/tag/v1.0.0
