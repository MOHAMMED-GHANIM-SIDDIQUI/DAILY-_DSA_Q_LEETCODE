class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        
        # memo table
        dp = [[[-1]*2 for _ in range(201)] for __ in range(201)]

        def solve(onesLeft, zerosLeft, lastWasOne):
            if onesLeft == 0 and zerosLeft == 0:
                return 1

            if dp[onesLeft][zerosLeft][lastWasOne] != -1:
                return dp[onesLeft][zerosLeft][lastWasOne]

            result = 0

            if lastWasOne:  # explore 0s
                for length in range(1, min(zerosLeft, limit) + 1):
                    result = (result + solve(onesLeft, zerosLeft - length, 0)) % MOD
            else:  # explore 1s
                for length in range(1, min(onesLeft, limit) + 1):
                    result = (result + solve(onesLeft - length, zerosLeft, 1)) % MOD

            dp[onesLeft][zerosLeft][lastWasOne] = result
            return result

        startWithOne = solve(one, zero, 0)
        startWithZero = solve(one, zero, 1)

        return (startWithOne + startWithZero) % MOD
