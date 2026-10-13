class Solution:
    def xorAfterQueries(self, nums: list[int], queries: list[list[int]]) -> int:
        mod = 10 ** 9 + 7
        for l, r, k, v in queries:
            for index in range(l, r + 1, k):
                nums[index] = (nums[index] * v) % mod
        result = 0
        for num in nums:
            result ^= num
        return result
