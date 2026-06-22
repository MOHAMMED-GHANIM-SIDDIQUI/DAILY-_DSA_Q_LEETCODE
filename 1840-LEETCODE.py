class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.append([n, n - 1])

        restrictions.sort()

        # Forward pass
        for i in range(1, len(restrictions)):
            d = restrictions[i][0] - restrictions[i - 1][0]
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i - 1][1] + d
            )

        # Backward pass
        for i in range(len(restrictions) - 2, -1, -1):
            d = restrictions[i + 1][0] - restrictions[i][0]
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i + 1][1] + d
            )

        ans = 0

        # Maximum possible peak between adjacent restrictions
        for i in range(1, len(restrictions)):
            x1, h1 = restrictions[i - 1]
            x2, h2 = restrictions[i]

            d = x2 - x1
            peak = (h1 + h2 + d) // 2
            ans = max(ans, peak)

        return ans
