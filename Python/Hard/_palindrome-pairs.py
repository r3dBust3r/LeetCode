# Name: palindrome-pairs
# URL: https://leetcode.com/problems/palindrome-pairs/
# ISSUE: TIME LIMIT EXCEEDE


class Solution:
    @staticmethod
    def isPalindrome(word: str) -> bool:
        if word == word[::-1]:
            return True
        return False

    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        result = list()
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if Solution.isPalindrome(f"{words[i]}{words[j]}"):
                    result.append([i, j])

                if Solution.isPalindrome(f"{words[j]}{words[i]}"):
                    result.append([j, i])

        return result


print(
    Solution.palindromePairs(
        None,
        ["abcd","dcba","lls","s","sssll"]
    )
)
