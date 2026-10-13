class Solution:
    def countSubarrays(self, nums: list[int], target: int) -> int:
        answer = 0
        for left in range(len(nums)):
            count = 0
            for right in range(left, len(nums)):
                if nums[right] == target:
                    count += 1
                length = right - left + 1
                if count > length // 2:
                    answer += 1
        return answer
