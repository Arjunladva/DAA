class Solution:
    def distMoney(self, money: int, children: int) -> int:
        money -= children
        if money < 0:
            return -1
        answer = min(money // 7, children)
        money -= answer * 7
        children -= answer

        if children == 0 and money > 0:
            answer -= 1
        elif children == 1 and money == 3:
            answer -= 1
        return answer
