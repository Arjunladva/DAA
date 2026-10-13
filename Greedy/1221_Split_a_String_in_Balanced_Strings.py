class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = answer = 0
        for char in s:
            balance += 1 if char == "R" else -1
            if balance == 0:
                answer += 1
        return answer
