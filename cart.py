MAX_NUMBERS_ORDERED = 20


class Cart:
    """Giỏ hàng chứa tối đa MAX_NUMBERS_ORDERED đĩa DVD."""

    def __init__(self):
        self.items = []

    def add_dvd(self, dvd) -> bool:
        """Thêm một DVD vào giỏ; trả về False nếu giỏ đã đầy."""
        if len(self.items) > MAX_NUMBERS_ORDERED:
            return False
        self.items.append(dvd)
        return True

    def total_cost(self) -> float:
        """Tổng tiền của các DVD trong giỏ."""
        return round(sum(dvd.cost for dvd in self.items), 2)
