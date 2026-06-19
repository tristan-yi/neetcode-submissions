class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = range(len(matrix))
        cols = range(len(matrix[0]))

        for r in rows:
            for c in cols:
                if matrix[r][c] == target:
                    return True
        return False