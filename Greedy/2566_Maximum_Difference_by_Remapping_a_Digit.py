class Solution:
    def minMaxDifference(self, num: int) -> int:
        text = str(num)
        max_text = text
        for digit in text:
            if digit != "9":
                max_text = text.replace(digit, "9")
                break
        min_text = text
        min_text = text.replace(text[0], "0")
        return int(max_text) - int(min_text)
