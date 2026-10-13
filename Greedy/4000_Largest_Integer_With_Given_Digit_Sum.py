class Solution:
    def largestInteger(self, n: int, sum: int) -> str:
        if sum == 0:
            return "0" if n == 1 else "-1"
        if sum > 9 * n:
            return "-1"

        digits = []
        for _ in range(n):
            digit = min(9, sum)
            digits.append(str(digit))
            sum -= digit

        if sum != 0:
            return "-1"
        return "".join(digits)
