class Solution:
    def minimumPushes(self, word: str) -> int:
        length = len(word)
        answer = 0
        for i in range(length):
            answer += i // 8 + 1
        return answer
