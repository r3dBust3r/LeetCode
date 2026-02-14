# Name: remove-duplicates-from-sorted-array
# URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        temp_nums = []
        for n in nums:
            if n not in temp_nums:
                temp_nums.append(n)

        nums[:] = temp_nums
        return len(nums)


arr = [0,0,1,1,1,2,2,3,3,4]
n = Solution.removeDuplicates(
    None,
    arr
)
print(f"{n}: {arr}")
