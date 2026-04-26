class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n, m = len(grid), len(grid[0])
        seen = set()
        def dfs(i, j, pi, pj, char):
            if (i, j) in seen:
                return True
            seen.add((i, j))
            for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= ni < n and 0 <= nj < m:
                    if (ni, nj) == (pi, pj):
                        continue
                    if grid[ni][nj] == char:
                        if dfs(ni, nj, i, j, char):
                            return True
            return False
        for i in range(n):
            for j in range(m):
                if (i, j) not in seen:
                    if dfs(i, j, -1, -1, grid[i][j]):
                        return True
        return False
