import unittest
from prompt_router import route


class RouterTests(unittest.TestCase):
    def test_support(self):
        self.assertEqual(route("Where is my order?").task, "support")

    def test_extract(self):
        self.assertEqual(route("extract the email as json").task, "extract")

    def test_fallback_and_empty(self):
        self.assertEqual(route("hello").task, "general")
        with self.assertRaises(ValueError):
            route(" ")


if __name__ == "__main__":
    unittest.main()
