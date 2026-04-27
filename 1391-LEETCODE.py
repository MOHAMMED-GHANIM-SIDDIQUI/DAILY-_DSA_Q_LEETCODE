class Solution:
    def hasValidPath(self, grid):
        self.m = len(grid)
        self.n = len(grid[0])

        self.directions = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(-1, 0), (0, 1)]
        }

        visited = set()
        return self.dfs(grid, 0, 0, visited)

    def dfs(self, grid, i, j, visited):
        if i == self.m - 1 and j == self.n - 1:
            return True

        visited.add((i, j))

        for di, dj in self.directions[grid[i][j]]:
            ni, nj = i + di, j + dj

            if not (0 <= ni < self.m and 0 <= nj < self.n):
                continue
            if (ni, nj) in visited:
                continue

            # check back connection
            for bi, bj in self.directions[grid[ni][nj]]:
                if ni + bi == i and nj + bj == j:
                    if self.dfs(grid, ni, nj, visited):
                        return True

        return False
