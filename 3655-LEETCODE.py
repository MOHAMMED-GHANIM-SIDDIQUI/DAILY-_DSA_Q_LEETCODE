import math
from collections import defaultdict

class Solution:
    def __init__(self):
        self.M = 10**9 + 7

    # Binary Exponentiation (Fermat's Little Theorem)
    def power(self, a, b):
        if b == 0:
            return 1
        half = self.power(a, b // 2)
        result = (half * half) % self.M
        if b % 2 == 1:
            result = (result * a) % self.M
        return result

    def xorAfterQueries(self, nums, queries):
        n = len(nums)
        blockSize = math.ceil(math.sqrt(n))

        smallKMap = defaultdict(list)

        for query in queries:
            L, R, K, V = query

            if K >= blockSize:
                for i in range(L, R + 1, K):
                    nums[i] = (nums[i] * V) % self.M
            else:
                smallKMap[K].append(query)

        for K, allQueries in smallKMap.items():
            diff = [1] * n

            for query in allQueries:
                L, R, _, V = query

                diff[L] = (diff[L] * V) % self.M

                steps = (R - L) // K
                next_idx = L + (steps + 1) * K

                if next_idx < n:
                    diff[next_idx] = (diff[next_idx] * self.power(V, self.M - 2)) % self.M

            # Cumulative product
            for i in range(n):
                if i - K >= 0:
                    diff[i] = (diff[i] * diff[i - K]) % self.M

            # Apply diff to nums
            for i in range(n):
                nums[i] = (nums[i] * diff[i]) % self.M

        result = 0
        for num in nums:
            result ^= num

        return result
