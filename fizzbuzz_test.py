import unittest
import fizzbuzz

class TestStringMethods(unittest.TestCase):

    def test_good(self):
        expected = "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FizzBuzz"
        result = fizzbuzz.multi(15, {3: 'Fizz', 5: 'Buzz'}, "")
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
