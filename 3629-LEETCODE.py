class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)

        # Smallest Prime Factor sieve
        MAXV = max(nums) + 1
        spf = list(range(MAXV))

        for i in range(2, int(MAXV ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, MAXV, i):
                    if spf[j] == j:
                        spf[j] = i

        # Get unique prime factors
        def get_factors(x):
            factors = set()
            while x > 1:
                p = spf[x]
                factors.add(p)
                while x % p == 0:
                    x //= p
            return factors

        # prime factor -> indices
        factor_to_indices = defaultdict(list)

        for i, val in enumerate(nums):
            for p in get_factors(val):
                factor_to_indices[p].append(i)

        q = deque([(0, 0)])  # (index, steps)
        visited = {0}

        used_prime = set()

        while q:
            i, steps = q.popleft()

            if i == n - 1:
                return steps

            # adjacent moves
            for nxt in [i - 1, i + 1]:
                if 0 <= nxt < n and nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, steps + 1))

            # teleportation
            val = nums[i]

            # teleport only if val itself is prime
            if len(get_factors(val)) == 1 and val in get_factors(val):

                p = val

                if p not in used_prime:
                    for nxt in factor_to_indices[p]:
                        if nxt not in visited:
                            visited.add(nxt)
                            q.append((nxt, steps + 1))

                    used_prime.add(p)

        return -1
