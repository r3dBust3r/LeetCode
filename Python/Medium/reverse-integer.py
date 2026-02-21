# Name: reverse-integer
# URL: https://leetcode.com/problems/reverse-integer/


class Solution:
    def reverse(self, x: int) -> int:
        s = ""
        if x < 0:
            x = -x
            s += "-"

        while x > 9:
            s += str(x % 10)
            x //= 10
        s += str(x)

        r = 0
        sign = 1
        length = len(s)

        i = 0
        while i < length and s[i] == ' ':
            i += 1

        if i < length and s[i] == '-':
            sign = -1
            i += 1

        while i < length:
            r = r * 10 + int(s[i])
            i += 1

        r *= sign

        if -2147483648 <= r <= 2147483647:
            return r

        return 0


print(
    Solution.reverse(
        None,
        -12345678
    )
)
