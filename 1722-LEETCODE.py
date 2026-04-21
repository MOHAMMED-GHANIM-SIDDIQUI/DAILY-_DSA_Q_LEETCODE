class Solution:
    def minimumHammingDistance(self, source, target, allowedSwaps):
        n = len(source)

        parent = list(range(n))
        rank = [0] * n

        # Find with path compression
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        # Union by rank
        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX == rootY:
                return

            if rank[rootX] < rank[rootY]:
                rootX, rootY = rootY, rootX

            parent[rootY] = rootX

            if rank[rootX] == rank[rootY]:
                rank[rootX] += 1

        # Step 1: Build components
        for x, y in allowedSwaps:
            union(x, y)

        # Step 2: Count frequency per group
        from collections import defaultdict

        groupFreq = defaultdict(lambda: defaultdict(int))

        for i in range(n):
            p = find(i)
            groupFreq[p][source[i]] += 1

        # Step 3: Calculate Hamming distance
        hamming = 0

        for i in range(n):
            p = find(i)
            if groupFreq[p][target[i]] > 0:
                groupFreq[p][target[i]] -= 1
            else:
                hamming += 1

        return hamming
