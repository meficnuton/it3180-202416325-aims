import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestCartLimit(unittest.TestCase):
    def test_add_dvd_until_full(self):
        """Giỏ chỉ nhận tối đa 20 đĩa; đĩa thứ 21 phải bị từ chối."""
        cart = Cart()
        for index in range(20):
            self.assertTrue(cart.add_dvd(DigitalVideoDisc(f"DVD {index + 1}")))
        self.assertEqual(len(cart.items), 20)

        self.assertFalse(cart.add_dvd(DigitalVideoDisc("DVD 21")))
        self.assertEqual(len(cart.items), 20)


if __name__ == "__main__":
    unittest.main()
