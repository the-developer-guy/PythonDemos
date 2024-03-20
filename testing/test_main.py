import unittest
from main_code import is_even

class EvenTest(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_when_even_expect_true(self):
        result = is_even(2)
        self.assertTrue(result)
    
    def test_when_odd_expect_false(self):
        result = is_even(1)
        self.assertFalse(result)

    def test_when_negative_even_expect_true(self):
        result = is_even(-2)
        self.assertTrue(result)
    
    def test_when_negative_odd_expect_false(self):
        result = is_even(-1)
        self.assertFalse(result)

    def test_when_zero_expect_true(self):
        result = is_even(0)
        self.assertTrue(result)
    
    def test_when_string_expect_exception(self):
        with self.assertRaises(TypeError):
            is_even("text")

    def test_when_float_expect_exception(self):
        with self.assertRaises(TypeError):
            is_even(3.14)
