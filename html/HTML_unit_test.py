import unittest
from HTML import solve


class TestHTML(unittest.TestCase):
    def test_small(self):
        for (x, ans) in [
            # (["<X>", "<Y>", "</Y>", "</X>"], "CORRECT"),
            # (["< HTML >", "< biba >", "</ BIBA >", "</KUKA>", "< / HTML >"], "ALMOST </KUKA>"),
            # (["< HTML >", "< TAG >", "< button >", "</ BUTTON >", "< TAG >", "< / html >"], 'INCORRECT'),
            # (["<br>"], "ALMOST <BR>"),
            # (["<x>", "<y>", "</x>", "</y>"], "INCORRECT"),
            # (["< HTML >", "< TAG >", "< button >", "</ BUTTON >", "< / html >"], 'ALMOST <TAG>'),
            # (["</TAG>"], "ALMOST </TAG>"),
            # (["<TAG>", "</TAG>"], "CORRECT"),
            # (["<x>", "<x>", "</x>", "</x>", "<x>"], "ALMOST <X>"),
            (["</x>", "<x>"], "INCORRECT")
        ]:
            self.assertEqual(
                solve(x),
                ans
            )

if __name__ == '__main__':
    unittest.main()
