class Solution:
    def smallestTrimmedNumbers(self, nums: list[str], queries: list[list[int]]) -> list[int]:
        answers = []
        for k, trim in queries:
            indexed = [(value[-trim:], index) for index, value in enumerate(nums)]
            indexed.sort()
            answers.append(indexed[k - 1][1])
        return answers
