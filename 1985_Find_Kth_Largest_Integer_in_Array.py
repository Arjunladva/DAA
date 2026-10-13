class Solution:
    def kthLargestNumber(self, nums: list[str], k: int) -> str:
        nums.sort(key=lambda value: (len(value), value), reverse=True)
        return nums[k - 1]
