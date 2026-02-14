# Name: count-primes
# URL: https://leetcode.com/problems/count-primes/
# ISSUE: TIME LIMIT EXCEEDE

from math import isqrt

class Solution:
    @staticmethod
    def isPrime(n: int) -> bool:
        if n < 2:
            return False
        if n % 2 == 0:
            return n == 2
        for i in range(3, int(isqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def countPrimes(self, n: int) -> int:
        c = 0
        for i in range(2, n):
            if Solution.isPrime(i):
                c += 1
        return c


print(
    Solution.countPrimes(
        None,
        999999
    )
)
