import unittest


class TestX(unittest.TestCase):
    def setUp(self):
        self.obj = X()

    def test_multiplication_positive_numbers(self):
        result = self.obj.z(3, 4)
        self.assertEqual(result, 12)

    def test_multiplication_with_zero(self):
        result = self.obj.z(0, 10)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
