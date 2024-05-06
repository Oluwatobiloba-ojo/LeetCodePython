from unittest import TestCase
from pivotInteger import Solution


class TestSomething(TestCase):
    def testPivotInteger(self):
        nums: int = 8
        result: int = 6
        solution = Solution()
        output = solution.pivotInteger(nums)
        self.assertEqual(result, output)

    def testPivotInteger2(self):
        nums: int = 1
        result: int = 1
        solution = Solution()
        output = solution.pivotInteger(nums)
        self.assertEqual(result, output)

    def testPivotInteger3(self):
        nums: int = 4
        result: int = -1
        solution = Solution()
        output = solution.pivotInteger(nums)
        self.assertEqual(result, output)
