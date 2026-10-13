class Solution:
    def countElements(self, nums: list[int], k: int) -> int:
        if k == 0:
            return len(nums)
        ordered = sorted(nums, reverse=True)
        answer = 0
        for value in nums:
            greater = sum(1 for other in nums if other > value)
            if greater >= k:
                answer += 1
        return answer
