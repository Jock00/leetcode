class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        aboveRow = [1] * n

        for _ in range(m - 1):
            currentRow = [1] * n
            for i in range(1, n):
                currentRow[i] = currentRow[i - 1] + aboveRow[i]
            aboveRow = currentRow

        return aboveRow[-1]

sol = Solution()
n = 3
m = 3
o = sol.uniquePaths(m, n)
print(o)