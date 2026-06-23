class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7

        m = r - l + 1

        # dp[v] = number of ways ending with value v
        dp = [1] * m

        for i in range(1, n):
            ndp = [0] * m

            if i % 2 == 1:
                # previous value must be smaller
                pref = 0
                for v in range(m):
                    ndp[v] = pref
                    pref = (pref + dp[v]) % MOD
            else:
                # previous value must be larger
                suff = 0
                for v in range(m - 1, -1, -1):
                    ndp[v] = suff
                    suff = (suff + dp[v]) % MOD

            dp = ndp

        return (2 * sum(dp)) % MOD
