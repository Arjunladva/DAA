class Solution:
    def minimumOperations(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        operations = 0
        for col in range(cols):
            for row in range(1, rows):
                if grid[row][col] <= grid[row - 1][col]:
                    new_value = grid[row - 1][col] + 1
                    operations += new_value - grid[row][col]
                    grid[row][col] = new_value
        return operations
