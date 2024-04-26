from unittest import TestCase

from code.valid_palindrome import isPalindrome


class TestSomething(TestCase):
    def testSomethingPalindrome(self):
        value = 'A man a plan, a canal: Panama'
        self.assertTrue(isPalindrome(value))

    def testThatWordIsNotPalindrome(self):
        value = 'race a car'
        self.assertFalse(isPalindrome(value))


    def testThatWordIsPalindrome(self):
        value = " "
        self.assertTrue(isPalindrome(value))
