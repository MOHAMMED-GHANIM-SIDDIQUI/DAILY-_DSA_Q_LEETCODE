# 3660. Jump Game IX

## 🔗 Problem Link
https://leetcode.com/problems/jump-game-ix/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Greedy

---

## 🧩 Problem Summary
You are given an integer array `nums`. From an index `i` you may jump to an index `j` if either:
- `j > i` and `nums[j] < nums[i]`, or
- `j < i` and `nums[j] > nums[i]`.

For every index `i`, return the **maximum value** in `nums` reachable starting from `i` (including `nums[i]` itself) after any number of jumps.

### 📌 Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`

---

## 💭 Intuition
👉 Think of reachability as flowing through a *frontier*:

- From index `i`, the best forward jump value we can ever pick up is the **maximum on the prefix `[0..i]`**, because we can always step back-and-forth between positions to absorb every prefix maximum into our reachable set (going left to a larger value, then forward to a smaller value, etc.).
- Call `pre_max[i] = max(nums[0..i])`. If there exists *any* index `j > i` with `nums[j] < pre_max[i]`, then standing at `i` we can reach index `j` — and from `j` we can reach everything `j` reaches.
- Whether such a `j` exists is exactly the test `pre_max[i] > min(nums[i+1..n-1])`. So we sweep right-to-left maintaining a running suffix minimum and chain answers.

Two simple invariants do all the work:
1. `pre_max[i]` — best value we can pick up by moving over the left side.
2. `suf_min` — smallest value strictly to the right; if `pre_max[i]` exceeds it, we can hop forward and inherit `ans[i+1]`.

---

## ⚡ Approach — Prefix Max + Suffix Min Chain

### 🧠 Idea
- Build `pre_max` left-to-right: `pre_max[i] = max(pre_max[i-1], nums[i])`.
- Sweep `i` from `n-1` down to `0` keeping `suf_min = min(nums[i+1..n-1])`:
  - If `pre_max[i] > suf_min`, a forward jump is possible → `ans[i] = ans[i+1]` (inherit the chain).
  - Otherwise, no forward jump beats us; the best we can do is `pre_max[i]` itself.
- Update `suf_min = min(suf_min, nums[i])` *after* the comparison.

---

## 💻 Code

```python
class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)

        pre_max = [0] * n
        pre_max[0] = nums[0]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], nums[i])

        ans = [0] * n
        suf_min = float("inf")

        for i in range(n - 1, -1, -1):
            if pre_max[i] > suf_min:
                ans[i] = ans[i + 1]
            else:
                ans[i] = pre_max[i]
            suf_min = min(suf_min, nums[i])

        return ans
```

---

## 🧠 Dry Run
### Input
```
nums = [2, 1, 3]
```
### Steps
```
pre_max = [2, 2, 3]

i = 2: suf_min = inf  → pre_max[2]=3 not > inf → ans[2] = 3
       suf_min = min(inf, 3) = 3
i = 1: pre_max[1]=2, suf_min=3 → 2 > 3? no → ans[1] = pre_max[1] = 2
       suf_min = min(3, 1) = 1
i = 0: pre_max[0]=2, suf_min=1 → 2 > 1? yes → ans[0] = ans[1] = 2
       suf_min = min(1, 2) = 1

ans = [2, 2, 3]
```
- From index 0 (value 2): can jump forward to index 1 (1 < 2). pre_max along the way is 2 → max reachable = 2 ✅
- From index 1 (value 1): no forward jump (next is 3 > 1) and no backward jump (0 has 2 < 1? no, 2 > 1 so we *can* go to 0). Wait — going to 0 requires `nums[0] > nums[1]`, i.e. 2 > 1 ✅. So from 1 we reach 0 (value 2). Max = 2 ✅
- From index 2 (value 3): nothing larger to the left, no forward indices. Max = 3 ✅

---

## ⏱️ Time Complexity
```
O(n) — one left-to-right sweep for pre_max, one right-to-left sweep for ans.
```

## 💾 Space Complexity
```
O(n) — for pre_max and ans. The suf_min is a single scalar.
       (pre_max can be removed by computing it inline if you want O(1) extra space beyond the output.)
```

---

## ⚠️ Edge Cases
- `n == 1` → no jumps possible, `ans = [nums[0]]`.
- All equal values → no jump satisfies the strict `<` / `>` condition, `ans[i] = nums[i]` for all `i`.
- Strictly increasing → from any `i`, no `j > i` has `nums[j] < nums[i]`; backward jumps to larger values *do* work, so `ans[i]` reaches `pre_max[i]` (which equals `nums[i]` at every position) — meaning `ans = nums`.
- Strictly decreasing → every `j > i` satisfies `nums[j] < nums[i]`, so chaining covers the whole array; `ans[i]` falls through to `ans[n-1] = nums[0]` (the largest), which gives `ans = [nums[0]] * n`.
- Duplicates → strict inequality means duplicates do **not** create jumps; only the surrounding distinct values matter.

---

## 🎯 Interview Takeaways
- The "can I reach ahead?" test reduces to a single inequality: `pre_max[i] > min(nums[i+1..])`. Don't simulate jumps.
- Whenever a problem allows zig-zagging between indices subject to value comparisons, the *attainable set* often collapses to "everything below your prefix maximum that lies to the right" — a classic monotone-frontier observation.
- Sweeping right-to-left while updating `suf_min` *after* the comparison is the standard idiom for "is there anything strictly to my right that satisfies P?". Don't include the current index in the running min until after the check.
- Chaining via `ans[i] = ans[i+1]` is union-find-by-pointer in disguise; once you can hop one step forward, you inherit the entire downstream component.

---

## 📌 Key Pattern
👉 **"Reachability = prefix-max meets suffix-min — when prefix-max strictly exceeds the suffix-min, the chain extends."**

---

## 🔁 Related Problems
- 55. Jump Game
- 45. Jump Game II
- 1306. Jump Game III
- 1345. Jump Game IV
- 1340. Jump Game V

---

## 🚀 Final Thoughts
The whole problem hinges on noticing that the *set* of reachable indices from `i` is determined by `pre_max[i]` and the suffix below it — not by the order of jumps. Once that's clear, an `O(n)` two-sweep solution drops out and the rest is bookkeeping.

---

✨ **Rule to remember:**
> When jumps obey value comparisons, ask what your *attainable maximum* and the *minimum ahead* are — the answer usually lives in their interaction, not in any particular jump sequence.
