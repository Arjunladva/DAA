class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        total = sum(nums)
        max_current = max_sum = nums[0]
        min_current = min_sum = nums[0]

        for num in nums[1:]:
            max_current = max(num, max_current + num)
            max_sum = max(max_sum, max_current)
            min_current = min(num, min_current + num)
            min_sum = min(min_sum, min_current)

        if max_sum < 0:
            return max_sum
        return max(max_sum, total - min_sum)
