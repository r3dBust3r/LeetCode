# Name: add-digits
# URL: https://leetcode.com/problems/add-digits/


class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            num = (num % 10) + (num // 10)
        return num


print(
    Solution.addDigits(
        None,
        12345
    )
)
