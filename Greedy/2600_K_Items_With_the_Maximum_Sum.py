class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int,
                             numNegOnes: int, k: int) -> int:
        take_ones = min(numOnes, k)
        answer = take_ones
        k -= take_ones

        take_zeros = min(numZeros, k)
        k -= take_zeros
        answer -= min(numNegOnes, k)
        return answer
