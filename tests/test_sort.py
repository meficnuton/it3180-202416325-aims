import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestCartSort(unittest.TestCase):
    def test_sort_by_title_ascending(self):
        """sort_by_title sắp xếp theo tiêu đề A → Z."""
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("Star Wars", "Science Fiction", 24.95))
        cart.add_dvd(DigitalVideoDisc("Aladdin", "Animation", 18.99))
        cart.add_dvd(DigitalVideoDisc("The Lion King", "Animation", 19.95))

        self.assertEqual(
            [dvd.title for dvd in cart.sort_by_title()],
            ["Aladdin", "Star Wars", "The Lion King"],
        )

    def test_sort_by_cost_ascending(self):
        """sort_by_cost sắp xếp theo giá tăng dần."""
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("Star Wars", "Science Fiction", 24.95))
        cart.add_dvd(DigitalVideoDisc("Aladdin", "Animation", 18.99))
        cart.add_dvd(DigitalVideoDisc("The Lion King", "Animation", 19.95))

        self.assertEqual(
            [dvd.title for dvd in cart.sort_by_cost()],
            ["Aladdin", "The Lion King", "Star Wars"],
        )


if __name__ == "__main__":
    unittest.main()
