# Name: count-number-of-distinct-integers-after-reverse-operations
# URL: https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/


class Solution:
    @staticmethod
    def reverse(n: int) -> int:
        s = ""
        while n > 9:
            s += str(n % 10)
            n //= 10
        s += str(n)

        r = 0
        sign = 1
        length = len(s)

        i = 0
        while i < length and s[i] == ' ':
            i += 1

        if i < length and s[i] == '-':
            sign = -1
            i += 1

        while i < length:
            r = r * 10 + int(s[i])
            i += 1

        return r * sign

    def countDistinctIntegers(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            nums.append(Solution.reverse(nums[i]))
        return len(list(set(nums)))


nums = [1,13,10,12,31]
x = Solution.countDistinctIntegers(
    None,
    nums=nums
)
print(f"{x}: {nums}")
