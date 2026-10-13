class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        nums.sort(reverse=True)
        total = sum(nums)
        chosen = []
        current = 0
        for num in nums:
            chosen.append(num)
            current += num
            if current > total - current:
                return chosen
        return chosen
