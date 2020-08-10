import unittest
from galton_v2 import solve
import random
import time


class MyTestCase(unittest.TestCase):
    # def test_gen_trig(self):
    #     # self.assertEqual(
    #     #     gen_triangle(3),
    #     #     [1, 2, 1]
    #     # )
    #     self.assertEqual(
    #         gen_triangle(4),
    #         [1, 3,3, 1]
    #     )
    def test_small(self):
        for (x, h, ans) in [
            ([[1], [2, 3]], 2, "7 2"),
            ([[-2], [-2, -2], [-2, -2, -2]], 3, "-6 1"),
            ([[5], [-2, 3], [0, -7, 1]], 3, "9 4"),
            ([[1], [2,3],[4,5,6],[7,8,9,10]], 4, "17 1")
        ]:
            self.assertEqual(
                solve(x),
                ans
            )
    def test_large(self):
        h = 30
        l = [[random.randint(-100, 100) for x in range(i)] for i in range(1, h+1)]
        t0 = time.time()

        solve(l)
        t1 = time.time()
        print('Passed:', int(t1 - t0) % 60)


if __name__ == '__main__':
    unittest.main()
