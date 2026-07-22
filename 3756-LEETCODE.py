class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        # prefix sum of digits
        pre_sum = [0] * (n + 1)

        # position among non-zero digits
        nz_idx = [0] * (n + 1)

        vals = []
        pref = [0]
        pw = [1]

        for i, ch in enumerate(s):
            d = ord(ch) - ord('0')
            pre_sum[i + 1] = pre_sum[i] + d

            if d:
                vals.append(d)
                pref.append((pref[-1] * 10 + d) % MOD)
                pw.append((pw[-1] * 10) % MOD)

            nz_idx[i + 1] = len(vals)

        ans = []

        for l, r in queries:
            L = nz_idx[l]
            R = nz_idx[r + 1]
            k = R - L

            if k == 0:
                ans.append(0)
                continue

            x = (pref[R] - pref[L] * pw[k]) % MOD
            sm = pre_sum[r + 1] - pre_sum[l]
            ans.append((x * sm) % MOD)

        return ans
