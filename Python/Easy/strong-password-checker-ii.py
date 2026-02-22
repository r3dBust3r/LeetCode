# Name: strong-password-checker-ii
# URL: https://leetcode.com/problems/strong-password-checker-ii/


class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False

        lc = False
        uc = False
        dg = False
        sp = False

        for i in range(len(password)):
            if password[i].islower(): lc = True
            if password[i].isupper(): uc = True
            if password[i].isdigit(): dg = True
            if password[i] in "!@#$%^&*()-+": sp = True
            if i != 0 and password[i] == password[i - 1]:
                return False

        if lc and uc and dg and sp:
            return True

        return False


print(
    Solution.strongPasswordCheckerII(
        None,
        "sUCJE32&Kl"
    )
)
