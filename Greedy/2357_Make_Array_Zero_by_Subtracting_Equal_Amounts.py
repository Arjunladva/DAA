class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        return len(set(num for num in nums if num > 0))
