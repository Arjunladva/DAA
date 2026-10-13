class Solution:
    def kthLargestValue(self, matrix: list[list[int]], k: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        values = []
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                prefix[r][c] = (matrix[r - 1][c - 1] ^
                                 prefix[r - 1][c] ^
                                 prefix[r][c - 1] ^
                                 prefix[r - 1][c - 1])
                values.append(prefix[r][c])
        values.sort(reverse=True)
        return values[k - 1]
