# Name: string-to-integer-atoi
# URL: https://leetcode.com/problems/string-to-integer-atoi


class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        r = 0
        i = 0

        try:
            while 1:
                if s[i] != ' ':
                    break
                i += 1

            if s[i] == '-' or s[i] == '+':
                if s[i] == '-':
                    sign = -1
                i += 1

            while '0' <= s[i] <= '9':
                r = r * 10 + ord(s[i]) - ord('0')
                i += 1

        except IndexError:
            pass

        r *= sign

        if r <= -2147483648:
            return -2147483648

        if r >= 2147483647:
            return 2147483647

        return r


print(
    Solution.myAtoi(
        None,
        "   -1337coding8888"
    )
)
