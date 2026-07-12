class Solution:
    def pathsWithMaxScore(self, board):
        MOD = 10**9 + 7
        n = len(board)

        # dp[i][j] = [max_score_from_here_to_S, ways]
        dp = [[[-1, 0] for _ in range(n)] for _ in range(n)]
        dp[n-1][n-1] = [0, 1]   # Start from S

        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if board[i][j] == 'X':
                    continue
                if i == n-1 and j == n-1:
                    continue

                best = -1
                ways = 0

                # Can come from down, right, diagonal down-right
                for x, y in [(i+1, j), (i, j+1), (i+1, j+1)]:
                    if x < n and y < n and dp[x][y][0] != -1:
                        if dp[x][y][0] > best:
                            best = dp[x][y][0]
                            ways = dp[x][y][1]
                        elif dp[x][y][0] == best:
                            ways = (ways + dp[x][y][1]) % MOD

                if best == -1:
                    continue

                val = 0 if board[i][j] in 'SE' else int(board[i][j])
                dp[i][j] = [best + val, ways]

        if dp[0][0][0] == -1:
            return [0, 0]
        return [dp[0][0][0] % MOD, dp[0][0][1] % MOD]
