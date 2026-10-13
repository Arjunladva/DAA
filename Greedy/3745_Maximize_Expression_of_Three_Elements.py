class Solution:
    def maximizeExpressionOfThree(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        return nums[0] + nums[1] - nums[-1]
