class Solution:
    def maxSum(self, nums: list[int]) -> int:
        positive = set(num for num in nums if num > 0)
        if positive:
            return sum(positive)
        return max(nums)
