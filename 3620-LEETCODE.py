from typing import List
from collections import deque
import math

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)

        graph = [[] for _ in range(n)]
        indegree = [0] * n
        costs = set()

        for u, v, w in edges:
            graph[u].append((v, w))
            indegree[v] += 1
            costs.add(w)

        # topological sort
        q = deque([i for i in range(n) if indegree[i] == 0])
        topo = []

        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        costs = sorted(costs)

        def can(min_edge):
            dist = [math.inf] * n
            dist[0] = 0

            for u in topo:
                if dist[u] == math.inf:
                    continue

                if u != 0 and u != n - 1 and not online[u]:
                    continue

                for v, w in graph[u]:
                    if w < min_edge:
                        continue
                    if v != n - 1 and not online[v]:
                        continue
                    dist[v] = min(dist[v], dist[u] + w)

            return dist[n - 1] <= k

        left, right = 0, len(costs) - 1
        ans = -1

        while left <= right:
            mid = (left + right) // 2
            if can(costs[mid]):
                ans = costs[mid]
                left = mid + 1
            else:
                right = mid - 1

        return ans
        
