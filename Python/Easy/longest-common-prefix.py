# Name: longest-common-prefix
# URL: https://leetcode.com/problems/longest-common-prefix


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        smallest_str = min(strs, key=len)
        common = smallest_str

        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                for k in range(len(smallest_str)):
                    if strs[i][k] == strs[j][k]:
                        continue
                    common = common[:k]
                    break

        return common


print(
    Solution.longestCommonPrefix(
        None,
        ["flower","flow","flight"]
    )
)
