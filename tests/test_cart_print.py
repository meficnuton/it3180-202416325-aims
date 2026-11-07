import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestCartPrint(unittest.TestCase):
    def test_print_cart_empty(self):
        import io
        from contextlib import redirect_stdout

        cart = Cart()
        buf = io.StringIO()
        with redirect_stdout(buf):
            cart.print_cart()
        self.assertEqual(buf.getvalue().strip(), "The cart is empty")

    def test_print_cart_lists_items(self):
        import io
        from contextlib import redirect_stdout

        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("The Lion King", "Animation", 19.95))
        buf = io.StringIO()
        with redirect_stdout(buf):
            cart.print_cart()
        output = buf.getvalue()
        self.assertIn("The Lion King", output)
        self.assertIn("1", output)


if __name__ == "__main__":
    unittest.main()
