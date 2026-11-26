import os
import unittest

from app import farewell, greet


class GreetTest(unittest.TestCase):
    def test_greets_by_name(self):
        self.assertEqual(greet("Ada"), "Hello, Ada!")


class FarewellTest(unittest.TestCase):
    def test_says_goodbye_by_name(self):
        self.assertEqual(farewell("Ada"), "Goodbye, Ada!")


class BreakMainTest(unittest.TestCase):
    def test_break_main_is_an_empty_file_at_the_repo_root(self):
        path = os.path.join(os.path.dirname(__file__), "..", "BREAK_MAIN")
        self.assertTrue(os.path.isfile(path))
        self.assertEqual(os.path.getsize(path), 0)


if __name__ == "__main__":
    unittest.main()
