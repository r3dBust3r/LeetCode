# Name: find-maximum-number-of-string-pairs
# URL: https://leetcode.com/problems/find-maximum-number-of-string-pairs/


class Solution:
    def maximumNumberOfStringPairs(self, words: list[str]) -> int:
        paired = dict()
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if i in paired: continue
                if words[i] == words[j][::-1]:
                    paired[i] = j
        return len(paired)

print(
    Solution.maximumNumberOfStringPairs(
        None,
        ["cd","ac","dc","ca","zz"]
    )
)
