# Name: ransom-note
# URL: https://leetcode.com/problems/ransom-note/


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_counter = {}
        for i in range(len(ransomNote)):
            if ransomNote[i] not in ransom_counter:
                ransom_counter[ransomNote[i]] = 1
            else:
                ransom_counter[ransomNote[i]] += 1

        magazine_counter = {}
        for i in range(len(magazine)):
            if magazine[i] not in magazine_counter:
                magazine_counter[magazine[i]] = 1
            else:
                magazine_counter[magazine[i]] += 1
        try:
            for l, c in ransom_counter.items():
                if c > magazine_counter[l]:
                    return False
        except KeyError:
            return False

        return True


print(
    Solution.canConstruct(
        None,
        "aabccac", "asabclcmmaactcakcc"
    )
)
