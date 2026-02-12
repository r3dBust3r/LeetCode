# Name: palindrome-number
# URL: https://leetcode.com/problems/palindrome-number/


class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        for i in range(len(x)):
            if x[i] == x[len(x) - 1 - i]:
                continue
            return False
        return True


print(
    Solution.isPalindrome(
        None,
        1237321
    )
)
