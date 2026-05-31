from sortedcontainers import SortedList

class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, i, val):
        while i <= self.n:
            self.bit[i] = max(self.bit[i], val)
            i += i & -i

    def query(self, i):
        res = 0
        while i > 0:
            res = max(res, self.bit[i])
            i -= i & -i
        return res


class Solution:
    def getResults(self, queries):
        MX = min(50000, len(queries) * 3)

        obstacles = SortedList([0, MX])
        for q in queries:
            if q[0] == 1:
                obstacles.add(q[1])

        bit = BIT(MX + 2)

        arr = list(obstacles)
        for i in range(1, len(arr)):
            bit.update(arr[i], arr[i] - arr[i - 1])

        ans = []

        for q in reversed(queries):
            if q[0] == 1:
                x = q[1]

                idx = obstacles.index(x)
                left = obstacles[idx - 1]
                right = obstacles[idx + 1]

                bit.update(right, right - left)
                obstacles.remove(x)

            else:
                _, x, sz = q

                idx = obstacles.bisect_right(x)
                prev_obs = obstacles[idx - 1]

                ans.append(
                    bit.query(prev_obs) >= sz or
                    x - prev_obs >= sz
                )

        return ans[::-1]
