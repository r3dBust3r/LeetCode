# Name: transformed-array
# URL: https://leetcode.com/problems/transformed-array/


class Solution:
    def constructTransformedArray(self, nums: list[int]) -> list[int]:
        transformed = list()

        for i in range(len(nums)):
            if nums[i] == 0:
                transformed.append(0)
                
            else:
                new_index = (i + nums[i]) % len(nums)
                transformed.append(nums[new_index])

        return transformed


print(
    Solution.constructTransformedArray(
        None,
        [3,-2,1,1]
    )
)
