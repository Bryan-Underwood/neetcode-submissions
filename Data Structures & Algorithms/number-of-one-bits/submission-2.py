class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return 0

        count = 0

        while n:
            n &= n-1
            count += 1

        return count