class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        answer = 0
        for i in range(len(colors)):
            for j in range(len(colors)):
                if colors[i] != colors[j]:
                    answer = max(answer, abs(i - j))
        return answer
