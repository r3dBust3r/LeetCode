# Name: validate-ip-address


class Solution:
    @staticmethod
    def atoiBase(s: str, base: int) -> int:
        if not 2 <= base <= 16: return 0

        n = len(s)

        i = 0
        while i < n and s[i].isspace(): i += 1

        sign = 1
        if i < n and s[i] in ['-', '+']:
            if s[i] == '-': sign = -1
            i += 1

        chrs = "0123456789ABCDEF"
        r = 0

        while i < n:
            if chrs.find(s[i]) == -1: break

            if chrs.index(s[i]) >= base: break

            r = r * base + int(chrs.index(s[i]))
            i += 1

        return r * sign


print(
    Solution.atoiBase(
        "2058", 16
    )
)
