# Name: closest-prime-numbers-in-range
# URL: https://leetcode.com/problems/closest-prime-numbers-in-range/

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

    def closestPrimes(self, left: int, right: int) -> list[int]:
        prims = []
        options = []
        for i in range(left, right + 1):
            if Solution.isPrime(i):
                prims.append(i)

        try:
            for i in range(len(prims)):
                options.append([prims[i], prims[i + 1]])
        except IndexError:
            pass

        target = []
        min_subs = 9e9
        for i in range(len(options) - 1, -1, -1):
            o = options[i]
            if o[1] - o[0] <= min_subs:
                min_subs = o[1] - o[0]
                target = o

        if not options:
            return [-1, -1]

        return target


print(
    Solution.closestPrimes(
        None,
        12854,
        130337
    )
)
