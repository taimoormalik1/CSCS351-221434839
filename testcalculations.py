import unittest
import calculations

class testcalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculations.add(10, 5), 15)
        self.assertEqual(calculations.add(1, 1), 2)
        self.assertEqual(calculations.add(3,5), 8)

    def test_subtract(self):
        self.assertEqual(calculations.subtract(10, 5), 5)
        self.assertEqual(calculations.subtract(3, 1), 2)
        self.assertEqual(calculations.subtract(13,5), 8)

    def test_square(self):
        self.assertEqual(calculations.square(2, 3), 8)
        self.assertEqual(calculations.square(1, 1), 1)
        self.assertEqual(calculations.square(3,5), 243)
    def test_mod(self):
        self.assertEqual(calculations.mod(10, 5), 0)
        self.assertEqual(calculations.mod(2, 1), 0)
        self.assertEqual(calculations.mod(8,3), 2)

    def test_multiply(self):
        self.assertEqual(calculations.multiply(10, 5), 50)
        self.assertEqual(calculations.multiply(2, 1), 2)
        self.assertEqual(calculations.multiply(8,3), 24)

if __name__ == '__main__':
     unittest.main()
