import unittest
import pycritic
from PlatformType import PlatformType


class MyTestCase(unittest.TestCase):
    botw = "the legend of zelda breath of the wild"

    def test_get_developer(self):
        self.assertEqual(pycritic.get_developer(MyTestCase.botw, PlatformType.NS), "Nintendo")

    def test_get_rating(self):
        self.assertEqual(pycritic.get_rating(MyTestCase.botw, PlatformType.NS), "E10+")


if __name__ == '__main__':
    unittest.main()
