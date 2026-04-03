from bisect import bisect_left, bisect_right

class Solution:
    def maxWalls(self, robots, distance, walls):
        n = len(robots)

        # combine robot position and distance
        roboDist = [(robots[i], distance[i]) for i in range(n)]
        roboDist.sort()
        walls.sort()

        # helper: count walls in [l, r]
        def countWalls(l, r):
            left = bisect_left(walls, l)
            right = bisect_right(walls, r)
            return right - left

        # build range array
        range_ = []
        for i in range(n):
            pos, d = roboDist[i]

            leftLimit  = 1 if i == 0 else roboDist[i-1][0] + 1
            rightLimit = int(1e9) if i == n-1 else roboDist[i+1][0] - 1

            L = max(pos - d, leftLimit)
            R = min(pos + d, rightLimit)

            range_.append((L, R))

        # DP table
        t = [[-1]*2 for _ in range(n+1)]

        def solve(i, prevDir):
            if i == n:
                return 0

            if t[i][prevDir] != -1:
                return t[i][prevDir]

            leftStart = range_[i][0]

            if prevDir == 1:  # previous fired right
                leftStart = max(leftStart, range_[i-1][1] + 1)

            # fire left
            leftTake = countWalls(leftStart, roboDist[i][0]) + solve(i+1, 0)

            # fire right
            rightTake = countWalls(roboDist[i][0], range_[i][1]) + solve(i+1, 1)

            t[i][prevDir] = max(leftTake, rightTake)
            return t[i][prevDir]

        return solve(0, 0)
