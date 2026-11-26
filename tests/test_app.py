import unittest

from app import farewell, greet


class GreetTest(unittest.TestCase):
    def test_greets_by_name(self):
        self.assertEqual(greet("Ada"), "Hello, Ada!")


class FarewellTest(unittest.TestCase):
    def test_says_goodbye_by_name(self):
        self.assertEqual(farewell("Ada"), "Goodbye, Ada!")


if __name__ == "__main__":
    unittest.main()
