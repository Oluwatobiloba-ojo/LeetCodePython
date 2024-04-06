import unittest

from code.anagram import isAnagram


class MyTestCase(unittest.TestCase):

    def testThatThisIsNotAnagram(self):
        first = "anagram"
        second = "nagarams"
        self.assertFalse(isAnagram(first, second))

    def testThatThisIsAnagram(self):
        first = "anagram"
        second = "nagaram"
        self.assertTrue(isAnagram(first, second))

    def testThatThisIsNotAnAnagramEvenWhenSameLength(self):
        first = "cat"
        second = "rat"
        self.assertFalse(isAnagram(first, second))

    def testThatWordCatAndActAreAnagram(self):
        first = "cat"
        second = "act"
        self.assertTrue(first, second)

    def testThatPlayersAndParsleyAreAnagram(self):
        first = "players"
        second = "parsley"
        self.assertTrue(first, second)

    def testThatCiderAndCriedAreAnagram(self):
        first = "cider"
        second = "cried"
        self.assertTrue(first, second)


if __name__ == '__main__':
    unittest.main()
