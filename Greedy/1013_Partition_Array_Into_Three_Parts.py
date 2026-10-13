class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0:
            return False

        target = total // 3
        current = parts = 0
        for num in arr:
            current += num
            if current == target:
                parts += 1
                current = 0
        return parts >= 3
