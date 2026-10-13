class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1
        for char, count in counts.items():
            if count < k:
                return max(self.longestSubstring(part, k)
                           for part in s.split(char))
        return len(s)
