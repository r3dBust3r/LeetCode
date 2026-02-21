# Name: reverse-string-ii
# URL: https://leetcode.com/problems/reverse-string-ii/


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        new_s = ""
        i = 0
        turn = 1
        while i < len(s):
            if i % k == 0:
                if turn:
                    turn = 0
                    new_s += s[i:i + k][::-1]
                else:
                    turn = 1
                    new_s += s[i:i + k]
            i += 1
        return new_s


print(
    Solution.reverseStr(
        None,
        s = "abcdefg",
        k = 2
    )
)
