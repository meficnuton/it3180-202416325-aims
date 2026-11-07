import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class TestSearchByTitle(unittest.TestCase):
    def test_search_is_case_insensitive(self):
        """Tim 'lion' phai ra 'The Lion King' (khong phan biet hoa/thuong)."""
        items = [DigitalVideoDisc("The Lion King", "Animation", 19.95)]

        self.assertEqual(
            [dvd.title for dvd in search_by_title(items, "lion")],
            ["The Lion King"],
        )
        self.assertEqual(
            [dvd.title for dvd in search_by_title(items, "LION")],
            ["The Lion King"],
        )


if __name__ == "__main__":
    unittest.main()
