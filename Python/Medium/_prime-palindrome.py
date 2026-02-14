# Name: prime-palindrome
# URL: https://leetcode.com/problems/prime-palindrome/
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
    
    @staticmethod
    def isPalindrome(n: int) -> bool:
        n = str(n)
        for i in range(int(len(n) / 2 + 1)):
            if n[i] == n[len(n) - 1 - i]:
                continue
            return False
        return True

    def primePalindrome(self, n: int) -> int:
        while True:
            if Solution.isPalindrome(n):
                if Solution.isPrime(n):
                    return n
            n += 1


print(
    Solution.primePalindrome(
        None,
        9889990
    )
)
