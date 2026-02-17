# Name: move-zeroes
# URL: https://leetcode.com/problems/move-zeroes/


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == 0:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp


nums = [0,1,0,3,12]
Solution.moveZeroes(
    None,
    nums=nums
)
print(nums)
