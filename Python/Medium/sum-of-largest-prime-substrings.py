# Name: sum-of-largest-prime-substrings
# URL: https://leetcode.com/problems/sum-of-largest-prime-substrings/

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
    
    @staticmethod
    def generatePossibilites(str: str) -> list[str]:
        possibilites = []
        for i in range(len(str)):
            s = str[i]
            if Solution.isPrime(int(s)):
                possibilites.append(int(s))
            for j in range(i + 1, len(str)):
                s += str[j]
                if Solution.isPrime(int(s)):
                    possibilites.append(int(s))
        return list(set(possibilites))

    def sumOfLargestPrimes(self, s: str) -> int:
        return sum(
            sorted(
                Solution.generatePossibilites(s),
                reverse=True
            )[:3]
        )


print(
    Solution.sumOfLargestPrimes(
        None,
        "12234"
    )
)
