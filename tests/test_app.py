import unittest

from app import farewell, greet, murmur, shout, whisper, yell


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


class MurmurTest(unittest.TestCase):
    def test_lowercases_text(self):
        self.assertEqual(murmur("Hello World"), "hello world")

    def test_leaves_non_letters_unchanged(self):
        self.assertEqual(murmur("ALREADY LOUD!"), "already loud!")

    def test_leaves_lowercase_text_unchanged(self):
        self.assertEqual(murmur("already quiet"), "already quiet")

    def test_empty_string(self):
        self.assertEqual(murmur(""), "")


class YellTest(unittest.TestCase):
    def test_upper_cases_with_exclamation_mark(self):
        self.assertEqual(yell("hi"), "HI!")


if __name__ == "__main__":
    unittest.main()
