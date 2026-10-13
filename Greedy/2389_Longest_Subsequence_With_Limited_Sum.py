class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        nums.sort()
        prefix = []
        total = 0
        for num in nums:
            total += num
            prefix.append(total)

        answers = []
        for query in queries:
            count = 0
            for value in prefix:
                if value <= query:
                    count += 1
                else:
                    break
            answers.append(count)
        return answers
