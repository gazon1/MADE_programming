import unittest
from rect import preprocess, solve

class MyTestCase(unittest.TestCase):
    def test_something(self):
        l = \
            [
                "1 7",
                "4 7",
                "6 7",
                "1 5",
                "4 5",
                "6 5",
                "3 3",
                "1 1",
                "4 1"
            ]
        dots = preprocess(l)
        self.assertEqual(
            solve(dots),
            5
        )


if __name__ == '__main__':
    unittest.main()
