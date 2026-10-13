class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        low, high = 0, len(s)
        answer = []
        for char in s:
            if char == "I":
                answer.append(low)
                low += 1
            else:
                answer.append(high)
                high -= 1
        answer.append(low)
        return answer
