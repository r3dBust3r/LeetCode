# Name: letter-combinations-of-a-phone-number
# URL: https://leetcode.com/problems/letter-combinations-of-a-phone-number/


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        letters = {
            2: "abc", 3: "def",
            4: "ghi", 5: "jkl",
            6: "mno", 7: "pqrs",
            8: "tuv", 9: "wxyz",
        }
        result = list()

        if len(digits) == 1:
            lttrs = letters[int(digits[0])]
            for a in lttrs:
                result.append(a)

        elif len(digits) == 2:
            lttrs1 = letters[int(digits[0])]
            lttrs2 = letters[int(digits[1])]
            for a in lttrs1:
                for b in lttrs2:
                    result.append(f"{a}{b}")

        elif len(digits) == 3:
            lttrs1 = letters[int(digits[0])]
            lttrs2 = letters[int(digits[1])]
            lttrs3 = letters[int(digits[2])]
            for a in lttrs1:
                for b in lttrs2:
                    for c in lttrs3:
                        result.append(f"{a}{b}{c}")

        elif len(digits) == 4:
            lttrs1 = letters[int(digits[0])]
            lttrs2 = letters[int(digits[1])]
            lttrs3 = letters[int(digits[2])]
            lttrs4 = letters[int(digits[3])]
            for a in lttrs1:
                for b in lttrs2:
                    for c in lttrs3:
                        for d in lttrs4:
                            result.append(f"{a}{b}{c}{d}")

        return result


print(
    Solution.letterCombinations(
        None,
        "2345"
    )
)
