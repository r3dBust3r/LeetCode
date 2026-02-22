# Name: defanging-an-ip-address
# URL: https://leetcode.com/problems/defanging-an-ip-address/


class Solution:
    def defangIPaddr(self, address: str) -> str:
        defanged = ""
        for c in address:
            if c == '.':
                defanged += "[.]"
            else:
                defanged += c
        return defanged


print(
    Solution.defangIPaddr(
        None,
        "1.1.1.1"
    )
)
