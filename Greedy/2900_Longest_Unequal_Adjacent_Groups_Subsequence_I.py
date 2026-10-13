class Solution:
    def getLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        answer = []
        last_group = None
        for word, group in zip(words, groups):
            if group != last_group:
                answer.append(word)
                last_group = group
        return answer
