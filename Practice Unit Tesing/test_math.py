import unittest
import myMath


class TestMyMath(unittest.TestCase):

    def test_add(self):

        print("Testing Add Function")
        self.assertEqual(myMath.add(10, 5), 15)
        self.assertEqual(myMath.add(10, 20), 30)
        self.assertEqual(myMath.add(30, -20), 10)
        self.assertEqual(myMath.add(-1, -1), -2)
        self.assertEqual(myMath.add(0, 0), 0)
        print("Add Tests Passed\n")

    def test_subtract(self):

        print("Testing Subract Function")
        self.assertEqual(myMath.subtract(10, 5), 5)
        self.assertEqual(myMath.subtract(75, 25), 50)
        self.assertEqual(myMath.subtract(10, -5), 15)
        self.assertEqual(myMath.subtract(-10, 5), -15)
        self.assertEqual(myMath.subtract(10, 15), -5)
        print("Subtract Tests Passed\n")

    def test_multiply(self):

        print("Testing Mulitply Function")
        self.assertEqual(myMath.multiply(10, 5), 50)
        self.assertEqual(myMath.multiply(5, 5), 25)
        self.assertEqual(myMath.multiply(100, 5), 500)
        self.assertEqual(myMath.multiply(7, -5), -35)
        self.assertEqual(myMath.multiply(1, 0), 0)
        print("Multiply Tests Passed\n")

    def test_divide(self):

        print("Testing Divide Function")
        self.assertEqual(myMath.divide(25, 5), 5)
        self.assertEqual(myMath.divide(50, 5), 10)
        self.assertEqual(myMath.divide(5, 5), 1)
        self.assertEqual(myMath.divide(10, 1), 10)
        self.assertEqual(myMath.divide(10, -2), -5)
        with self.assertRaises(ValueError):
            myMath.divide(10, 0)
        print("Divide Tests Passed\n")

if __name__ == '__main__':
    unittest.main()

