# Name: a-number-after-a-double-reversal
# URL: https://leetcode.com/problems/a-number-after-a-double-reversal/


class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        old_num = num
        s = ""
        while num > 9:
            s += str(num % 10)
            num //= 10
        s += str(num)

        r = 0
        length = len(s)
        i = 0
        while i < length and (s[i] == '0' or s[i] == ' '):
            i += 1

        while i < length:
            r = r * 10 + int(s[i])
            i += 1

        r = int(str(r)[::-1])
        return True if old_num == r else False


print(
    Solution.isSameAfterReversals(
        None,
        123
    )
)
