# 3691. Maximum Total Subarray Value II

## 🔗 Problem Link
https://leetcode.com/problems/maximum-total-subarray-value-ii/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Heap (Priority Queue), Sparse Table

---

## 🧩 Problem Summary

You are given `nums` and an integer `k`. You must choose **exactly `k` distinct subarrays** `(l, r)`. The value of a subarray is `max(nums[l..r]) - min(nums[l..r])`. You want to maximize the sum of the values of the chosen subarrays.

Unlike version I (which allowed reusing the single best subarray), here the `k` subarrays must be **distinct** `(l, r)` pairs. So we need the **`k` largest distinct subarray values** and their sum.

### 📌 Constraints
- `1 <= nums.length <= 5 * 10^4`
- `1 <= nums[i] <= 10^9`
- `1 <= k <= min(n*(n+1)/2, ...)` (k never exceeds the number of distinct subarrays)
- A subarray is identified by its `(l, r)` index pair; each may be used at most once.

---

## 💭 Intuition

👉 For a **fixed left endpoint `l`**, as the right endpoint `r` shrinks from `n-1` down to `l`, the window only loses elements, so `max` can only decrease and `min` can only increase. Therefore `value(l, r) = max - min` is **monotonically non-increasing as `r` decreases**. The widest window `(l, n-1)` gives the largest value for that `l`.

This means: among all subarrays starting at `l`, the best is `(l, n-1)`, the next-best is `(l, n-2)`, and so on. This is exactly the setup for a **k-way merge with a max-heap**: seed the heap with each `l`'s best window, repeatedly pop the global maximum, and push the next-widest window for that same `l`.

To make `value(l, r)` an `O(1)` query, we precompute **sparse tables** for range max and range min.

---

## ⚡ Approach — Sparse Table + Max-Heap k-way merge

### 🧠 Idea
- Build sparse tables `mx` and `mn` so any `value(l, r) = rangeMax(l,r) - rangeMin(l,r)` is answered in `O(1)`.
- For every left endpoint `l`, the widest (and thus most valuable) window is `(l, n-1)`. Push `(-value(l, n-1), l, n-1)` into a max-heap (negated for Python's min-heap).
- Repeat `k` times:
  - Pop the largest value `(l, r)`, add it to the answer.
  - If `r > l`, the next candidate sharing the same `l` is `(l, r-1)` — push it. This is the next-largest value for that `l`, and it has never been pushed before, so no duplicate `(l, r)` is ever counted.
- Because each `l` produces values in strictly decreasing order of `r`, popping the heap `k` times yields the `k` largest distinct subarray values.

---

## 💻 Code

```python
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)

        LOG = n.bit_length()

        mx = [nums[:]]
        mn = [nums[:]]

        j = 1
        while (1 << j) <= n:
            prev_mx = mx[j - 1]
            prev_mn = mn[j - 1]
            half = 1 << (j - 1)

            cur_mx = [
                max(prev_mx[i], prev_mx[i + half])
                for i in range(n - (1 << j) + 1)
            ]
            cur_mn = [
                min(prev_mn[i], prev_mn[i + half])
                for i in range(n - (1 << j) + 1)
            ]

            mx.append(cur_mx)
            mn.append(cur_mn)
            j += 1

        def value(l: int, r: int) -> int:
            length = r - l + 1
            p = length.bit_length() - 1
            mxv = max(mx[p][l], mx[p][r - (1 << p) + 1])
            mnv = min(mn[p][l], mn[p][r - (1 << p) + 1])
            return mxv - mnv

        heap = []

        for l in range(n):
            heapq.heappush(heap, (-value(l, n - 1), l, n - 1))

        ans = 0

        for _ in range(k):
            neg_v, l, r = heapq.heappop(heap)
            ans += -neg_v

            if r > l:
                heapq.heappush(heap, (-value(l, r - 1), l, r - 1))

        return ans
```

---

## 🧠 Dry Run

### Input
```
nums = [4, 2, 5], k = 3
```

### Steps
```
Build sparse tables for range max / range min.

value(l, r) = max(l..r) - min(l..r):
  value(0,2) = max(4,2,5) - min(4,2,5) = 5 - 2 = 3
  value(1,2) = max(2,5) - min(2,5)     = 5 - 2 = 3
  value(2,2) = 5 - 5                    = 0
  value(0,1) = 4 - 2                    = 2
  value(1,1) = 0

Seed heap with widest window per l:
  l=0 -> (-3, 0, 2)
  l=1 -> (-3, 1, 2)
  l=2 -> ( 0, 2, 2)

Pop 1: (-3, 0, 2) -> ans = 3. r>l, push (l=0, r=1): value(0,1)=2 -> (-2,0,1)
Pop 2: (-3, 1, 2) -> ans = 6. r>l, push (l=1, r=1): value(1,1)=0 -> ( 0,1,1)
Pop 3: (-2, 0, 1) -> ans = 8. r>l, push (l=0, r=0): value(0,0)=0 -> ( 0,0,0)

k = 3 pops done. Answer = 8
```

---

## ⏱️ Time Complexity
```
O(n log n + k log n)
```
Building the sparse tables takes `O(n log n)`. Seeding the heap is `O(n log n)`. Each of the `k` pops does `O(1)` value queries plus `O(log n)` heap work, for `O(k log n)`.

---

## 💾 Space Complexity
```
O(n log n)
```
The two sparse tables dominate, each storing `O(n log n)` precomputed values. The heap holds at most `n` entries at any time.

---

## ⚠️ Edge Cases
- All elements equal: every subarray has value `0`, answer is `0`.
- `n == 1`: only `value(0,0) = 0`; heap seeded once; any `k` (must be 1) yields `0`.
- Large `k` approaching the total number of subarrays: the heap mechanism still enumerates them in decreasing order without duplicates because each `(l, r)` is pushed exactly once.
- Strictly increasing/decreasing arrays: widest window always has the largest spread.

---

## 🎯 Interview Takeaways
- Monotonicity of `max - min` as a window shrinks turns "k largest subarray values" into a clean k-way merge.
- Sparse tables give `O(1)` static range min/max after `O(n log n)` preprocessing — the right tool when there are no updates.
- A negated tuple `(-value, l, r)` adapts Python's min-heap into a max-heap.

---

## 📌 Key Pattern
👉 **"For a fixed left endpoint, value(l, r) is monotonic in r — so use a max-heap k-way merge over per-left 'best window' candidates."**

---

## 🔁 Related Problems
- Maximum Total Subarray Value I
- 373. Find K Pairs with Smallest Sums
- 378. Kth Smallest Element in a Sorted Matrix
- 2386. Find the K-Sum of an Array

---

## 🚀 Final Thoughts
The whole problem hinges on one observation: shrinking a window can only reduce its `max - min`. Once you see that values are sorted per-left-endpoint, the `k`-largest selection becomes a textbook heap merge, and the sparse table just makes each value lookup free. The distinctness requirement (vs. version I) is exactly what forces the "push the next window for that l" step instead of re-counting one global best.

---

✨ **Rule to remember:**
> "When a quantity is monotonic along one axis of your candidate space, a heap that advances one step per pop extracts the top-k in sorted order."
