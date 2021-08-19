import random
import unittest
import mycalc


class MyCalcTestIncrease(unittest.TestCase):
    def test_add(self):
        """Описание теста"""
        self.assertEqual(mycalc.add(1, 2), 3)
        print('shortDescription:', self.shortDescription())

        self.id()

    def test_mul(self):
        self.assertEqual(mycalc.mul(3, 7), 21)


class MyCalcTestDecrease(unittest.TestCase):
    def test_sub(self):
        self.assertEqual(mycalc.sub(4, 2), 2)

    # @unittest.skipIf(random.random() < .5, 'Ретроградный меркурий мешает')
    def test_div(self):
        self.assertEqual(mycalc.div(16, 8), 2)
        with self.assertRaises(ZeroDivisionError):
            mycalc.div(1, 0)


# @unittest.skip('Корни не нужны.')
# class MyCalcTestDecrease(unittest.TestCase):
#     def test_sqrt(self):
#         self.assertAlmostEqual(
#             mycalc.sqrt(9),
#             3,
#             delta=.000000001
#         )


if __name__ == "__main__":
    unittest.main()
