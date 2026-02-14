# Name: complete-prime-number
# URL: https://leetcode.com/problems/complete-prime-number/

from math import isqrt

class Solution:
    @staticmethod
    def isPrime(n: int) -> bool:
        if n < 2:
            return False
        if n % 2 == 0:
            return n == 2
        for i in range(3, isqrt(n) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    def completePrime(self, num: int) -> bool:
        prefixes = []
        suffexis = []
        s = ""
        for c in str(num):
            s += c
            prefixes.append(s)

        s = ""
        for i in range(len(str(num)) - 1, -1, -1):
            s = list(s)
            s.insert(0, str(num)[i])
            s = ''.join(s)
            suffexis.append(s)

        for i in range(len(prefixes)):
            if not Solution.isPrime(int(prefixes[i])): return False
            if not Solution.isPrime(int(suffexis[i])): return False

        return True


print(
    Solution.completePrime(
        None,
        23
    )
)
