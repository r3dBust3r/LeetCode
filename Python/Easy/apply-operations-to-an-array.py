# Name: apply-operations-to-an-array
# URL: https://leetcode.com/problems/apply-operations-to-an-array/


class Solution:
    @staticmethod
    def moveZeroes(nums: list[int]) -> None:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == 0:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp

    def applyOperations(self, nums: list[int]) -> list[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        Solution.moveZeroes(nums)
        return nums


print(
    Solution.applyOperations(
        None,
        [1,2,2,1,1,0]
    )
)
