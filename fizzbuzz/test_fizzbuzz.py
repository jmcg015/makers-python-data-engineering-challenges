import unittest

from fizzbuzz import fizzbuzz

class TestFizzbuzz(unittest.TestCase):
    def test_lists_value_of_1_initially(self):
        self.assertEqual(fizzbuzz(1), "1")

    def test_lists_value_of_up_to_2(self):
        self.assertEqual(fizzbuzz(2), "1, 2")

    def test_lists_value_of_up_to_3(self):
        self.assertEqual(fizzbuzz(3), "1, 2, Fizz")

    def test_lists_value_of_up_to_5(self):
        self.assertEqual(fizzbuzz(5), "1, 2, Fizz, 4, Buzz")

    def test_lists_value_of_up_to_6(self):
        self.assertEqual(fizzbuzz(6), "1, 2, Fizz, 4, Buzz, Fizz")

    def test_lists_value_of_up_to_10(self):
        self.assertEqual(fizzbuzz(10), "1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz")
    
    def test_lists_value_of_up_to_15(self):
        self.assertEqual(fizzbuzz(15), "1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz")

if __name__ == '__main__':
    unittest.main()