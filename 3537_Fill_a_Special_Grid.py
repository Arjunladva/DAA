class Solution:
    def specialGrid(self, n: int) -> list[list[int]]:
        size = 2 ** n
        grid = [[0] * size for _ in range(size)]

        def fill(r, c, length, start):
            if length == 1:
                grid[r][c] = start
                return
            half = length // 2
            area = half * half
            # Quadrants are filled in this order: top-right, bottom-right,
            # bottom-left, top-left.
            fill(r, c + half, half, start)
            fill(r + half, c + half, half, start + area)
            fill(r + half, c, half, start + 2 * area)
            fill(r, c, half, start + 3 * area)

        fill(0, 0, size, 0)
        return grid
