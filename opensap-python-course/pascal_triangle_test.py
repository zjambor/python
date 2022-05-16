import unittest
import pascal_triangle as pt

class Pascal_trangle_test(unittest.TestCase):
    def test_new_pascal_triangle(self):
        pascal_tr = [[1]]
        n = 10
        line = pt.rec_pascal_triangle(pascal_tr, n)[9]
        expected = [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
        self.assertEqual(line, expected)

if __name__ == '__main__':
    unittest.main()
    