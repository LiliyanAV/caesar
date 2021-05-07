import unittest
from main import Caesar


class TestCaesaer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.p = Caesar()

    def test_crypt(self):
        self.assertEqual(self.p.crypt("aha"), "nun")
        self.assertEqual(self.p.crypt("balk"), "onyx")
        self.assertEqual(self.p.crypt("barf"), "ones")
        self.assertEqual(self.p.crypt("bin"), "ova")
        self.assertEqual(self.p.crypt("envy"), "rail")
        self.assertEqual(self.p.crypt("errs"), "reef")
        self.assertEqual(self.p.crypt("fur"), "she")
        self.assertEqual(self.p.crypt("gnat"), "tang")
        self.assertEqual(self.p.crypt("clerk"), "pyrex")
        self.assertEqual(self.p.crypt("furby"), "sheol")
        self.assertEqual(self.p.crypt("ant"), "nag")

    def test_encrypt(self):
        self.assertEqual(self.p.encrypt("aha"), "nun")
        self.assertEqual(self.p.encrypt("balk"), "onyx")
        self.assertEqual(self.p.encrypt("barf"), "ones")
        self.assertEqual(self.p.encrypt("bin"), "ova")
        self.assertEqual(self.p.encrypt("envy"), "rail")
        self.assertEqual(self.p.encrypt("errs"), "reef")
        self.assertEqual(self.p.encrypt("fur"), "she")
        self.assertEqual(self.p.encrypt("gnat"), "tang")
        self.assertEqual(self.p.encrypt("clerk"), "pyrex")
        self.assertEqual(self.p.encrypt("furby"), "sheol")
        self.assertEqual(self.p.encrypt("ant"), "nag")


if __name__ == '__main__':
    unittest.main()
