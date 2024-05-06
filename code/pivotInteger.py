class Solution:

    def pivotInteger(self, n: int) -> int:
        for count in range(0, n+1):
            sums = sum([i for i in range(1, count+1)])
            if sums == sum([i for i in range(count, n+1)]):
                return count
        return -1
