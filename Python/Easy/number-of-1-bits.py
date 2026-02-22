# Name: number-of-1-bits
# URL: https://leetcode.com/problems/number-of-1-bits/


class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0
        for i in range(32):
            if n & 2 ** i:
                bits += 1
        return bits


print(
    Solution.hammingWeight(
        None,
        2147483645
    )
)
