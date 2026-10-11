import json
import unittest

from functions.refunds.handler import eligible, handler


class RefundsTest(unittest.TestCase):
    def test_window(self) -> None:
        self.assertTrue(eligible(30, used=False))
        self.assertFalse(eligible(31, used=False))
        self.assertFalse(eligible(1, used=True))

    def test_handler(self) -> None:
        out = handler({"body": json.dumps({"days": 3})}, None)
        self.assertEqual(json.loads(out["body"]), {"eligible": True})


if __name__ == "__main__":
    unittest.main()
