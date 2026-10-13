class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        values = sorted(nums)
        half = (len(nums) + 1) // 2
        small = values[:half][::-1]
        large = values[half:][::-1]
        nums[::2] = small
        nums[1::2] = large
