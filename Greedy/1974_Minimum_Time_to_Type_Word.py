class Solution:
    def minTimeToType(self, word: str) -> int:
        time = len(word)
        current = "a"
        for char in word:
            distance = abs(ord(char) - ord(current))
            time += min(distance, 26 - distance)
            current = char
        return time
