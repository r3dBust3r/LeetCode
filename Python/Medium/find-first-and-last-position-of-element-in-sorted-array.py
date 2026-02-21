# Name: find-first-and-last-position-of-element-in-sorted-array
# URL: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        result = [-1, -1]
        for i in range(len(nums)):
            if nums[i] == target:
                if result[0] == -1:
                    result = [i, i]
                else:
                    result[1] = i
        return result


print(
    Solution.searchRange(
        None,
        [5,7,7,8,8,10], 8
    )
)
