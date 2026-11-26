import unittest

from app import farewell, greet, shout, whisper


class GreetTest(unittest.TestCase):
    def test_greets_by_name(self):
        self.assertEqual(greet("Ada"), "Hello, Ada!")


class FarewellTest(unittest.TestCase):
    def test_says_goodbye_by_name(self):
        self.assertEqual(farewell("Ada"), "Goodbye, Ada!")


class ShoutTest(unittest.TestCase):
    def test_upper_cases_with_exclamation_mark(self):
        self.assertEqual(shout("hello"), "HELLO!")


class WhisperTest(unittest.TestCase):
    def test_lowercases_and_appends_ellipsis(self):
        self.assertEqual(whisper("HELLO"), "hello...")


if __name__ == "__main__":
    unittest.main()
