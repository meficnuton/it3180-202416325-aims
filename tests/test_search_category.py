import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category


class TestSearchByCategory(unittest.TestCase):
    def test_search_by_category_is_case_insensitive(self):
        """Tim theo the loai, khong phan biet hoa/thuong."""
        items = [
            DigitalVideoDisc("The Lion King", "Animation", 19.95),
            DigitalVideoDisc("Star Wars", "Science Fiction", 24.95),
            DigitalVideoDisc("Aladdin", "Animation", 18.99),
        ]

        self.assertEqual(
            [dvd.title for dvd in search_by_category(items, "animation")],
            ["The Lion King", "Aladdin"],
        )
        self.assertEqual(search_by_category(items, "horror"), [])


if __name__ == "__main__":
    unittest.main()
