# Name: reverse-string
# URL: https://leetcode.com/problems/reverse-string/


class Solution:
    def reverseString(self, s: list[str]) -> None:
        for i in range(len(s) // 2):
            tmp = s[i]
            s[i] = s[len(s) - 1 - i]
            s[len(s) - 1 - i] = tmp


string = ["h","e","l","l","o"]
Solution.reverseString(
    None,
    string
)
print(string)
