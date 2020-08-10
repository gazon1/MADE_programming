import unittest
from N_bit import solve


class TestNBit(unittest.TestCase):
    # def test_small(self):
    #     for (x, ans) in [
    #         (1, 3),
    #         (2, 5),
    #         (7, 17),
    #     ]:
    #         self.assertEqual(
    #             solve(x),
    #             ans
    #         )

    def test_large(self):
        for (x, ans) in [
            (103, 18432),
            (10000, 13733871088263)
        ]:
            self.assertEqual(
                solve(x),
                ans
            )


if __name__ == '__main__':
    unittest.main()
