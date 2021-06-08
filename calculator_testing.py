import unittest
from main import Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        add_object = Calculator()
        self.assertEqual(add_object.add(1, 1), 2), "Incorrect addition. Answer should be two."