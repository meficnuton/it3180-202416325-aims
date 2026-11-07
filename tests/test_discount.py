import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestDiscount(unittest.TestCase):
    def test_discounted_total_and_validation(self):
        """Giảm 20% trên giỏ 100$ -> 80$; percent ngoài [0, 100] -> ValueError."""
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("DVD 100$", "Test", 100.0))

        self.assertEqual(cart.total_cost_with_discount(20), 80.0)
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)


if __name__ == "__main__":
    unittest.main()
