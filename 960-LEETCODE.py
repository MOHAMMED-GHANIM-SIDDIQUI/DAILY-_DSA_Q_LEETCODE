class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        k = len(strs[0])
        # dp[i]: length of LIS ending at column i
        dp = [1] * k

        for i in range(1, k):
            for j in range(i):
                # check if column j <= column i for all rows
                if all(s[j] <= s[i] for s in strs):
                    dp[i] = max(dp[i], dp[j] + 1)

        return k - max(dp)
