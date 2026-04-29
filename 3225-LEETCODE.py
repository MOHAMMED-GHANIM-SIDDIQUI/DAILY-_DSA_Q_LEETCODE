class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        if n == 1: return 0

        dp = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n)]
        prev_max = [[0] * (n + 1) for _ in range(n + 1)]
        prev_suffix_max = [[0] * (n + 1) for _ in range(n + 1)]
        col_sum = [[0] * (n + 1) for _ in range(n)]

        for c in range(n):
            for r in range(1, n + 1):
                col_sum[c][r] = col_sum[c][r - 1] + grid[r - 1][c]

        for i in range(1, n):
            for curr_h in range(n + 1):
                for prev_h in range(n + 1):
                    if curr_h <= prev_h:
                        extra_score = col_sum[i][prev_h] - col_sum[i][curr_h]
                        dp[i][curr_h][prev_h] = max(
                            dp[i][curr_h][prev_h],
                            prev_suffix_max[prev_h][0] + extra_score,
                        )
                    else:
                        extra_score = col_sum[i - 1][curr_h] - col_sum[i - 1][prev_h]
                        dp[i][curr_h][prev_h] = max(
                            dp[i][curr_h][prev_h],
                            prev_max[prev_h][curr_h] + extra_score,
                            prev_suffix_max[prev_h][curr_h]
                        )

            for curr_h in range(n + 1):
                cur_max = 0
                for next_h in range(n + 1):
                    cur_max = max(cur_max, dp[i][next_h][curr_h])
                    prev_max[curr_h][next_h] = cur_max

                cur_suffix_max = 0
                for next_h in range(n, -1, -1):
                    cur_suffix_max = max(cur_suffix_max, dp[i][next_h][curr_h])
                    prev_suffix_max[curr_h][next_h] = cur_suffix_max

        ans = 0
        for prev_h in range(n + 1):
            ans = max(ans, prev_suffix_max[prev_h][0])

        return ans
