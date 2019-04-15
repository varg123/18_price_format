import unittest
from format_price import format_price


class TestPriceMethod(unittest.TestCase):
    def test_format_price_none(self):
        self.assertIsNone(format_price(''))

    def test_format_price_not_valid_str(self):
        self.assertIsNone(format_price('test'))

    def test_format_price_valid_str(self):
        self.assertEqual(format_price('3245.000000'), '3 245')

    def test_format_price_valid_str_with_point(self):
        self.assertEqual(format_price('3245.123'), '3 245,12')

    def test_format_price_valid_str_null(self):
        self.assertEqual(format_price('0'), '0')

    def test_format_price_valid_str_nulls(self):
        self.assertEqual(format_price('0000'), '0')

    def test_format_price_valid(self):
        self.assertIsInstance(format_price('0000'), str)

if __name__ == '__main__':
    unittest.main()
