import numpy as np
class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        min_col = min_row = 0
        max_col = max_row = n
        direction = 0
        """
        0 - RIGHT -> LEFT
        1 - UP -> DOWN
        2 - RIGHT -> LEFT
        3 - DOWN - > UP
        """
        elem = 1
        col = row = 0
        matrix = [[0] * n for _ in range(n)]

        while True:
            try:
                ts = matrix[row][col]
            except IndexError:
                break
            else:
                if ts != 0:
                    break
            matrix[row][col] = elem
            elem += 1
            if direction % 4 == 0:
                if col < max_col - 1:
                    col += 1
                else:
                    row += 1
                    direction += 1
                    min_row += 1

            elif direction % 4 == 1:
                if row < max_row - 1:
                    row += 1
                else:
                    direction += 1
                    max_col -= 1
                    col -= 1

            elif direction % 4 == 2:
                if col > min_col:
                    col -= 1
                else:
                    direction += 1
                    max_row -= 1
                    row -= 1

            elif direction % 4 == 3:
                if row > min_row:
                    row -= 1
                else:
                    direction += 1
                    min_col += 1
                    col += 1
        return matrix
sol = Solution()
n = 20
print(np.matrix(sol.generateMatrix(n)))