class Solution:
    def splitNum(self, num: int) -> int:
        digits = sorted(str(num))
        first = digits[::2]
        second = digits[1::2]
        return int("".join(first)) + int("".join(second))
