class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        largest = max(nums)
        return k * largest + (k * (k - 1)) // 2
