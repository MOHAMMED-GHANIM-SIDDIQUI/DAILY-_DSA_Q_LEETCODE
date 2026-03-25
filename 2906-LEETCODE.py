class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        n, m = len(grid), len(grid[0])
        p = [[0] * m for _ in range(n)]

        # Step 1: prefix
        prefix = 1
        for i in range(n):
            for j in range(m):
                p[i][j] = prefix
                prefix = (prefix * grid[i][j]) % MOD

        # Step 2: suffix
        suffix = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                p[i][j] = (p[i][j] * suffix) % MOD
                suffix = (suffix * grid[i][j]) % MOD

        return p
