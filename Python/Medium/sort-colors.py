# Name: sort-colors
# URL: https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp


colors = [2,0,2,1,1,0]
Solution.sortColors(
    None,
    colors
)
print(colors)
