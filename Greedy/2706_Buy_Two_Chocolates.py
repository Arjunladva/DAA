class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        prices.sort()
        remaining = money - prices[0] - prices[1]
        return remaining if remaining >= 0 else money
