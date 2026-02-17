# Name: length-of-last-word
# URL: https://leetcode.com/problems/length-of-last-word/


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lw = s.strip().split(' ')[-1]
        return len(lw)


print(
    Solution.lengthOfLastWord(
        None,
        "Hello World!"
    )
)
