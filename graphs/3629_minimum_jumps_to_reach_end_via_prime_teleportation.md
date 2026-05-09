# 3629. Minimum Jumps to Reach End via Prime Teleportation

## 🔗 Problem Link
https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Hash Table, Math, Breadth-First Search, Number Theory

---

## 🧩 Problem Summary
You are given an integer array `nums` indexed from `0` to `n-1`. You start at index `0` and want to reach index `n-1` in the **minimum** number of jumps. From index `i` you may:

1. Move to `i - 1` or `i + 1` (if in bounds), **or**
2. **Teleport** — if `nums[i]` is a prime `p`, jump to *any* index `j` where `p` divides `nums[j]`.

Return the minimum number of jumps to reach index `n - 1`. If it is unreachable, return `-1`.

### 📌 Constraints
- `1 <= n <= 10^5`
- `1 <= nums[i] <= 10^6`

---

## 💭 Intuition
Every jump (adjacent or teleport) costs **1**. Every cost is uniform → this is a **shortest path on an unweighted graph** → **BFS**.

The naive graph has too many edges: each prime index `i` can teleport to *every* index sharing one of its prime factors. We can't materialize all those edges. Two key observations make BFS cheap:

1. **Teleportation is keyed by primes.** Group indices by every prime factor in their value. From a prime-valued index `i` (`nums[i] = p`), the teleport set is exactly `factor_to_indices[p]`.
2. **Each prime bucket is "used" at most once.** Once you've drained bucket `p` into the BFS frontier, every index in it is either already visited or just enqueued — you never gain anything by reopening that bucket later. Marking a prime as *used* turns the total teleport work across the whole BFS into `O(sum of bucket sizes) = O(n · #factors)` instead of `O(n²)`.

That single "spent prime" trick is what makes the BFS linear-ish.

---

## ⚡ Approach — BFS with prime-factor buckets, each bucket consumed once

### 🧠 Idea
1. Build a **smallest-prime-factor (SPF) sieve** up to `max(nums)`. With it, factoring any value is `O(log v)`.
2. For every index `i`, take the *unique* prime factors of `nums[i]` and append `i` to `factor_to_indices[p]` for each such `p`.
3. BFS from index `0`:
   - Standard adjacent moves to `i-1`, `i+1`.
   - **Teleport only if `nums[i]` itself is prime** (otherwise the problem doesn't allow teleporting from `i`). The teleport bucket is `factor_to_indices[nums[i]]`.
   - After draining bucket `p`, add `p` to a `used_prime` set so we never reopen it.
4. Return the BFS depth at which `n-1` is dequeued; otherwise `-1`.

The "used bucket" guarantee is what keeps the total work near `O(n · α + Σ|bucket_p|)` rather than blowing up to a quadratic edge set.

---

## 💻 Code

```python
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
```

---

## 🧠 Dry Run
### Input
```
nums = [2, 4, 6, 5, 9, 10]   (n = 6, target = index 5)
```

### Buckets (prime → indices whose value is divisible by that prime)
```
2 → [0, 1, 2, 5]      (2, 4, 6, 10 are even)
3 → [2, 4]            (6, 9)
5 → [3, 5]            (5, 10)
```

### BFS
```
queue            visited                     used_prime
[(0,0)]          {0}                         {}
pop (0,0)        nums[0]=2 is prime
  adj: enqueue (1,1)
  teleport p=2: enqueue 2, 5 with steps=1
queue: [(1,1),(2,1),(5,1)]   visited={0,1,2,5}   used_prime={2}

pop (1,1)        not target; nums[1]=4 (not prime, skip teleport)
  adj: 0 visited, 2 visited
pop (2,1)        not target; nums[2]=6 (not prime, skip teleport)
  adj: 1 visited, 3 unseen → enqueue (3,2)
pop (5,1)        i == n-1 → return 1 ✅
```

So the answer is `1` — we teleport directly from index `0` (value `2`) to index `5` (value `10`, divisible by `2`).

### Why "used_prime" matters
If later we revisited a prime-2 index, scanning `factor_to_indices[2]` again would be wasted — every index there was already enqueued (or visited) at the first scan. Skipping the bucket keeps total teleport work bounded by `Σ |bucket_p|`, not by `(visits) × |bucket|`.

---

## ⏱️ Time Complexity
```
Sieve:              O(M log log M)        where M = max(nums)
Factorization:      O(n · log M)          per-index unique prime factors via SPF
BFS, adj edges:     O(n)
BFS, teleport work: O(Σ_p |bucket_p|) = O(n · ω(M))   ω = #distinct prime factors

Overall: O(M log log M + n · log M)
```

## 💾 Space Complexity
```
O(M)  for the SPF sieve
O(n · ω(M))  for factor_to_indices
O(n)  for visited / queue
```

---

## ⚠️ Edge Cases
- `n == 1` → start is already the target → BFS returns `0` immediately.
- `nums[0] == 1` → no prime factors, no teleport possible from index 0; answer is whatever pure ±1 walking achieves (`n - 1`).
- All `nums[i] == 1` → only adjacent moves work → answer is `n - 1`.
- Prime values with empty buckets cannot happen (the index itself is in its own bucket), so teleport from a prime always reaches at least itself.
- Large primes near `10^6`: sieve must size to `max(nums) + 1` exactly, not a hardcoded bound.
- The teleport guard `len(get_factors(val)) == 1 and val in get_factors(val)` is the primality test — it correctly rejects composites and `1`.

---

## 🎯 Interview Takeaways
- **Uniform-cost shortest path → BFS.** Don't reach for Dijkstra when every edge weighs the same.
- **Don't materialize big edge sets.** Group nodes by the *property* that connects them (here: shared prime factor). Walk the bucket lazily during BFS.
- **"Spent bucket" optimization.** When the *first* time a bucket is opened it enqueues every still-unvisited member, no later visit gains anything — mark the bucket consumed. This collapses `O(visits × bucket_size)` to `O(bucket_size)`.
- **SPF sieve** is the workhorse for fast unique-prime-factorization across many values up to `10^6`.

---

## 📌 Key Pattern
👉 **"BFS over implicit buckets — group by the relation, drain each bucket once, never rebuild the edge set."**

---

## 🔁 Related Problems
- 1345. Jump Game IV (BFS with value-buckets, each bucket consumed once)
- 752. Open the Lock
- 127. Word Ladder
- 854. K-Similar Strings
- 815. Bus Routes (BFS over "routes" rather than stops)

---

## 🚀 Final Thoughts
This problem looks heavy because of the teleport rule, but it collapses cleanly: BFS for the uniform cost, prime-factor buckets for the implicit edges, and a *used-prime* set so each bucket is opened at most once. That last detail is the line between TLE and AC.

---

✨ **Rule to remember:**
> When edges in a BFS are defined by a shared key (prime, letter, color, route…), don't enumerate them — bucket the nodes by key and drain each bucket exactly once.
