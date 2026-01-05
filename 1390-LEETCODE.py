class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:
        ans = 0
        memory = {}

        for n in nums:
            if n in memory:
                ans += memory[n]
                continue

            divisior = 2  # 1 and n
            cnt = {1, n}

            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    j = n // i
                    if i == j:
                        divisior += 1
                        cnt.add(i)
                    else:
                        divisior += 2
                        cnt.add(i)
                        cnt.add(j)

                if divisior > 4:
                    break

            if divisior == 4:
                memory[n] = sum(cnt)
                ans += memory[n]

        return ans
