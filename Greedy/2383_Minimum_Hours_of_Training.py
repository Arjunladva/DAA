class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int,
                         energy: list[int], experience: list[int]) -> int:
        hours = max(0, sum(energy) + 1 - initialEnergy)
        current = initialExperience
        for opponent in experience:
            if current <= opponent:
                extra = opponent + 1 - current
                hours += extra
                current += extra
            current += opponent
        return hours
