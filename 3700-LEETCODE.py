class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7

        m = r - l + 1

        # State:
        # up[x]   = arrays ending at value x, last move was up
        # down[x] = arrays ending at value x, last move was down
        #
        # Total states = 2 * m

        sz = 2 * m

        T = [[0] * sz for _ in range(sz)]

        # up -> down
        for a in range(m):
            for b in range(a):
                T[m + b][a] = 1

        # down -> up
        for a in range(m):
            for b in range(a + 1, m):
                T[b][m + a] = 1

        def mat_mul(A, B):
            n = len(A)
            C = [[0] * n for _ in range(n)]

            for i in range(n):
                for k in range(n):
                    if A[i][k] == 0:
                        continue
                    aik = A[i][k]
                    for j in range(n):
                        if B[k][j]:
                            C[i][j] = (C[i][j] + aik * B[k][j]) % MOD
            return C

        def mat_pow(M, p):
            n = len(M)
            R = [[0] * n for _ in range(n)]
            for i in range(n):
                R[i][i] = 1

            while p:
                if p & 1:
                    R = mat_mul(R, M)
                M = mat_mul(M, M)
                p >>= 1

            return R

        # length = 2 initialization
        vec = [0] * sz

        for a in range(m):
            for b in range(m):
                if a == b:
                    continue
                if a < b:
                    vec[b] += 1      # last move up
                else:
                    vec[m + b] += 1  # last move down

        if n == 2:
            return sum(vec) % MOD

        P = mat_pow(T, n - 2)

        ans = 0
        for i in range(sz):
            cur = 0
            for j in range(sz):
                cur = (cur + P[i][j] * vec[j]) % MOD
            ans = (ans + cur) % MOD

        return ans
