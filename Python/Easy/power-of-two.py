# Name: power-of-two
# URL: https://leetcode.com/problems/power-of-two/


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i = 0
        while 2 ** i < n:
            i += 1

        if 2 ** i == n:
            return True
        return False


print(
    Solution.isPowerOfTwo(
        None,
        128
    )
)
