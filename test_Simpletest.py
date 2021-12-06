import unittest
import inc_dec    # The code to test

def add_together(a, b):
    return a + b

a = 3
b = 2
print(add_together(a, b))

def divide(a, b):
    return a // b

class Simpletest(unittest.TestCase):

    def test_equal(self):
        self.assertEqual('sa' + 'me', 'same')

    def test_true(self):
        self.assertTrue(True)

    def test_addition(self):
        a = 3
        b = 2
        expected = 5
        self.assertEqual(add_together(a, b), expected)

    def test_divide(self):
        a = 1
        b = 0
        self.assertRaises(ZeroDivisionError, divide, a, b)


class Test_TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(inc_dec.increment(3), 4)

    def test_decrement(self):
        self.assertEqual(inc_dec.decrement(3), 2)

if __name__ == '__main__':
    unittest.main()