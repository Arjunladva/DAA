from collections import Counter

class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        counts = sorted(Counter(s).values(), reverse=True)
        return sum(counts[k:])
