class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def to_minutes(value):
            hours, minutes = map(int, value.split(":"))
            return hours * 60 + minutes

        difference = to_minutes(correct) - to_minutes(current)
        operations = 0
        for step in [60, 15, 5, 1]:
            operations += difference // step
            difference %= step
        return operations
