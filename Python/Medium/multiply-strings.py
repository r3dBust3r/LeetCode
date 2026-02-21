# Name: multiply-strings
# URL: https://leetcode.com/problems/multiply-strings/


class Solution:
    @staticmethod
    def myAtoi(s: str) -> int:
        sign = 1
        r = i = 0
        try:
            while 1:
                if s[i] != ' ': break
                i += 1

            if s[i] == '-' or s[i] == '+':
                if s[i] == '-': sign = -1
                i += 1

            while '0' <= s[i] <= '9':
                r = r * 10 + ord(s[i]) - ord('0')
                i += 1
        except IndexError: pass
        return r * sign

    def multiply(self, num1: str, num2: str) -> str:
        return str(
            Solution.myAtoi(num1) * Solution.myAtoi(num2)
        )


print(
    Solution.multiply(
        None,
        "123", "456"
    )
)
