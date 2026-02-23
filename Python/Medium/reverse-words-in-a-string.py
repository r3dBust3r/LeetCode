# Name: reverse-words-in-a-string
# URL: https://leetcode.com/problems/reverse-words-in-a-string/


class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        for w in s.split(' '):
            if len(w.strip()):
                words.append(w)

        for i in range(len(words) // 2):
            (
                words[i],
                words[len(words) - 1 - i]
            ) = (
                words[len(words) - 1 - i],
                words[i]
            )

        return ' '.join(words)


print(
    Solution.reverseWords(
        None,
        "the sky is blue"
    )
)
