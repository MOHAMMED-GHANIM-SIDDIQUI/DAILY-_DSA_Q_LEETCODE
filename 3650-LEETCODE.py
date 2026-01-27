class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        # Build graph
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, 2 * w))

        # Dijkstra setup
        dist = [float('inf')] * n
        dist[0] = 0
        visited = [False] * n
        heap = [(0, 0)]  # (distance, node)

        while heap:
            d, u = heapq.heappop(heap)

            if u == n - 1:
                return d

            if visited[u]:
                continue

            visited[u] = True

            for v, weight in g[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    heapq.heappush(heap, (dist[v], v))

        return -1
