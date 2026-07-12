class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # Step 1: Distance of every cell from nearest thief
        dist = [[-1] * n for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
        # Step 2: Maximum bottleneck path using max heap
        pq = [(-dist[0][0], 0, 0)]
        seen = [[False] * n for _ in range(n)]
        seen[0][0] = True

        while pq:
            safe, x, y = heappop(pq)
            safe = -safe

            if x == n - 1 and y == n - 1:
                return safe

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not seen[nx][ny]:
                    seen[nx][ny] = True
                    heappush(pq, (-min(safe, dist[nx][ny]), nx, ny))

        return 0
