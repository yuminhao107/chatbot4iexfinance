import unittest
from iexfinance import Stock

class TestIexfinance(unittest.TestCase):

    def test_link(self):
        tsla=Stock('TSLA')
        self.assertTrue(tsla.get_open()>0)
