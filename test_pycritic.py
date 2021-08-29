import unittest
import pycritic
from PlatformType import PlatformType


class MyTestCase(unittest.TestCase):
    botw = "the legend of zelda breath of the wild"

    def test_get_metascore(self):
        self.assertEqual(pycritic.get_metascore(MyTestCase.botw, PlatformType.SWITCH), 97)

    def test_get_user_score(self):
        self.assertEqual(pycritic.get_user_score(MyTestCase.botw, PlatformType.SWITCH), 8.7)

    def test_get_developer(self):
        self.assertEqual(pycritic.get_developer(MyTestCase.botw, PlatformType.SWITCH), "Nintendo")

    def test_get_rating(self):
        self.assertEqual(pycritic.get_rating(MyTestCase.botw, PlatformType.SWITCH), "E10+")

    def test_get_genres(self):
        answer = ['Action Adventure', 'Open-World']
        self.assertEqual(pycritic.get_genre(MyTestCase.botw, PlatformType.SWITCH), answer)


if __name__ == '__main__':
    unittest.main()
