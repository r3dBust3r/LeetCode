# Name: most-common-word
# URL: https://leetcode.com/problems/most-common-word/


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        paragraph = paragraph.replace('.', ' ').replace(',', ' ')
        banned = [_.lower() for _ in banned]
        words = paragraph.lower().split(' ')
        words = [''.join(c for c in w if c.isalnum()) for w in words]
        counter = dict()
        for w in words:
            if w in banned or not w:
                continue
            if w not in counter:
                counter[w] = 1
            else:
                counter[w] += 1

        return max(counter, key=counter.get)


print(
    Solution.mostCommonWord(
        None,
        "a, a, a, a, b,b,b,c, c.k.k.k",
        ["a"]
    )
)
