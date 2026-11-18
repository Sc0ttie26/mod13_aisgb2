from datetime import datetime
import unittest

def is_valid_symbol(symbol):
    return symbol.isalpha() and symbol.isupper() and 1 <= len(symbol) <= 7


def is_valid_chart_type(chart_type):
    return chart_type in ["1", "2"]


def is_valid_time_series(time_series):
    return time_series in ["1", "2", "3", "4"]


def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

    
class TestStockInputs(unittest.TestCase):

    def test_symbol(self):
        self.assertTrue(is_valid_symbol("AAPL"))
        self.assertTrue(is_valid_symbol("A"))
        self.assertFalse(is_valid_symbol("aapl"))  
        self.assertFalse(is_valid_symbol("TOOLONG1"))  
        self.assertFalse(is_valid_symbol(""))

    def test_chart_type(self):
        self.assertTrue(is_valid_chart_type("1"))
        self.assertTrue(is_valid_chart_type("2"))
        self.assertFalse(is_valid_chart_type("3"))
        self.assertFalse(is_valid_chart_type("a"))


    def test_time_series(self):
        self.assertTrue(is_valid_time_series("1"))
        self.assertTrue(is_valid_time_series("4"))
        self.assertFalse(is_valid_time_series("5"))
        self.assertFalse(is_valid_time_series("0"))

    def test_start_date(self):
        self.assertTrue(is_valid_date("2023-05-01"))
        self.assertFalse(is_valid_date("05-01-2023"))  
        self.assertFalse(is_valid_date("2023-13-01"))

    def test_end_date(self):
        self.assertTrue(is_valid_date("2023-12-31"))
        self.assertFalse(is_valid_date("2023/12/31"))  
        self.assertFalse(is_valid_date("2023-02-30"))







if __name__ == "__main__":
    unittest.main()
