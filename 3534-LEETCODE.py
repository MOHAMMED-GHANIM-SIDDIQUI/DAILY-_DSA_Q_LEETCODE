from typing import List
import math


class Solution:
    def customUpperBound(self, arr, target):
        n = len(arr)
        l, r = 0, n - 1
        result = 0

        while l <= r:
            mid = l + (r - l) // 2

            if arr[mid][0] <= target:
                result = mid
                l = mid + 1
            else:
                r = mid - 1

        return result

    def pathExistenceQueries(
        self,
        n: int,
        nums: List[int],
        maxDiff: int,
        queries: List[List[int]]
    ) -> List[int]:

        # arr = [value, originalIndex]
        arr = [[nums[i], i] for i in range(n)]
        arr.sort()

        nodeToIdx = [0] * n
        for i in range(n):
            nodeToIdx[arr[i][1]] = i

        rows = n
        cols = math.floor(math.log2(n)) + 1 if n > 1 else 1

        ancestorTable = [[0] * cols for _ in range(rows)]

        # Fill 0th column
        for node in range(n):
            farthestIdxOneHop = self.customUpperBound(
                arr, arr[node][0] + maxDiff
            )
            ancestorTable[node][0] = farthestIdxOneHop

        # Fill remaining columns
        for j in range(1, cols):
            for node in range(n):
                ancestorTable[node][j] = ancestorTable[
                    ancestorTable[node][j - 1]
                ][j - 1]

        result = []

        for u, v in queries:
            a = nodeToIdx[u]
            b = nodeToIdx[v]

            if a == b:
                result.append(0)
                continue

            if a > b:
                a, b = b, a

            curr = a
            jumps = 0

            for j in range(cols - 1, -1, -1):
                if ancestorTable[curr][j] < b:
                    curr = ancestorTable[curr][j]
                    jumps += 1 << j

            if ancestorTable[curr][0] >= b:
                result.append(jumps + 1)
            else:
                result.append(-1)

        return result
