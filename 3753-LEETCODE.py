from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve(n: int) -> int:
            if n <= 0:
                return 0

            s = str(n)

            @lru_cache(None)
            def dfs(pos, tight, started, prev1, prev2):
                # returns (count_numbers, total_waviness)
                if pos == len(s):
                    return (1, 0)

                limit = int(s[pos]) if tight else 9
                total_cnt = 0
                total_wav = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)

                    if not started and d == 0:
                        cnt, wav = dfs(pos + 1, ntight, False, 10, 10)
                        total_cnt += cnt
                        total_wav += wav
                    else:
                        if not started:
                            cnt, wav = dfs(pos + 1, ntight, True, d, 10)
                            total_cnt += cnt
                            total_wav += wav
                        elif prev2 == 10:
                            cnt, wav = dfs(pos + 1, ntight, True, d, prev1)
                            total_cnt += cnt
                            total_wav += wav
                        else:
                            add = int(
                                (prev1 > prev2 and prev1 > d) or
                                (prev1 < prev2 and prev1 < d)
                            )

                            cnt, wav = dfs(pos + 1, ntight, True, d, prev1)

                            total_cnt += cnt
                            total_wav += wav + add * cnt

                return total_cnt, total_wav

            # subtract the "all-leading-zero" number
            return dfs(0, True, False, 10, 10)[1]

        return solve(num2) - solve(num1 - 1)
