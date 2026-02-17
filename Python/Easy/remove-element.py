# Name: remove-element
# URL: https://leetcode.com/problems/remove-element/


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        try:
            while True:
                if nums[i] == val:
                    nums.pop(i)
                    continue
                i += 1
        except IndexError:
            pass

        return len(nums)


nums = [0,1,2,2,3,0,4,2]
r = Solution.removeElement(
    None,
    nums=nums,
    val=2
)
print(r, nums)