# LeetCode provides Node.
class Solution:
    def construct(self, grid: list[list[int]]):
        def build(r, c, size):
            first = grid[r][c]
            same = True
            for i in range(r, r + size):
                for j in range(c, c + size):
                    if grid[i][j] != first:
                        same = False
                        break
                if not same:
                    break
            if same:
                return Node(first == 1, True, None, None, None, None)

            half = size // 2
            return Node(False, False,
                        build(r, c, half),
                        build(r, c + half, half),
                        build(r + half, c, half),
                        build(r + half, c + half, half))
        return build(0, 0, len(grid))
