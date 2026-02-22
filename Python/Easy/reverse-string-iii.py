# Name: reverse-string-iii
# URL: https://leetcode.com/problems/reverse-words-in-a-string-iii/


class Solution:
    def reverseWords(self, s: str) -> str:
        new_s = ""
        for w in s.split(' '):
            new_s += f"{w[::-1]} "
        return new_s.strip()


print(
    Solution.reverseWords(
        None,
        "Let's take LeetCode contest"
    )
)
