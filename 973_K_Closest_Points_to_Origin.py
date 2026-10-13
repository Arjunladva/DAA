class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        points.sort(key=lambda point: point[0] ** 2 + point[1] ** 2)
        return points[:k]
