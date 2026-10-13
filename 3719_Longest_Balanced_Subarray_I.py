class Solution:
    def longestBalanced(self, nums: list[int]) -> int:
        best = 0
        for left in range(len(nums)):
            evens = set()
            odds = set()
            for right in range(left, len(nums)):
                if nums[right] % 2 == 0:
                    evens.add(nums[right])
                else:
                    odds.add(nums[right])
                if len(evens) == len(odds):
                    best = max(best, right - left + 1)
        return best
