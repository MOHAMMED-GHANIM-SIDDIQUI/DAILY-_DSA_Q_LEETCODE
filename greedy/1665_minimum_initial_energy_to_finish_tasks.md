# 1665. Minimum Initial Energy to Finish Tasks

## 🔗 Problem Link
https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Greedy, Sorting

---

## 🧩 Problem Summary
You are given a 2D array `tasks` where `tasks[i] = [actual_i, minimum_i]`:
- `actual_i` is the energy spent to finish task `i`.
- `minimum_i` is the energy you must **already have** to start task `i`.

You may finish the tasks in any order. Return the **minimum initial energy** required to finish all tasks.

### 📌 Constraints
- `1 <= tasks.length <= 10^5`
- `1 <= actual_i <= minimum_i <= 10^4`

---

## 💭 Intuition
Two observations decide the whole problem:

1. The total energy actually **spent** is `sum(actual_i)` — independent of order.
2. What changes with order is the **peak start-requirement**. Some task may demand a high `minimum_i` long after you've drained your reserve on cheap tasks, and you'd be stuck.

So we want to schedule tasks so that the **buffer** (`minimum_i - actual_i`) is consumed in the right order. The cleanest framing: do the tasks that demand the **largest buffer first**, i.e. sort by `minimum_i - actual_i` descending.

But proving "this order is optimal" by hand is fiddly. A robust alternative is **binary search on the answer**: the predicate *"can I finish all tasks starting with `E` energy?"* is monotonic (more energy is always at least as good), so we binary-search the smallest `E` that works. The validator itself uses the same greedy sort. That's the approach below.

---

## ⚡ Approach — Binary Search on the Answer + Greedy Validator

### 🧠 Idea
1. Define `is_valid(tasks, energy)`: starting with `energy`, can we finish all tasks in **some** order?
   - Sort tasks by `minimum_i - actual_i` descending (highest "slack requirement" first).
   - Walk through; if `energy < minimum_i` at any step, fail. Else subtract `actual_i` and continue.
2. The predicate is monotonic in `energy`: if `E` works then `E+1` works. So binary-search `low = 0`, `high = 10^9` (safely above `sum(actual_i)`) for the smallest passing value.

The validator sort is `O(n log n)`; binary search does `O(log V)` validator calls where `V` is the energy range.

---

## 💻 Code

```python
class Solution:

    def is_valid(self, tasks, energy):

        # DO NOT mutate original list
        arr = sorted(tasks, key=lambda x: (x[1] - x[0]), reverse=True)

        for actual, minimum in arr:
            if energy < minimum:
                return False

            energy -= actual

        return True

    def minimumEffort(self, tasks: List[List[int]]) -> int:

        low, high = 0, 10**9
        ans = high

        while low <= high:

            mid = low + (high - low) // 2

            if self.is_valid(tasks, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
```

---

## 🧠 Dry Run

### Input
```
tasks = [[1, 3], [2, 4], [10, 11], [10, 12], [8, 9]]
```

### Sorted by (minimum - actual) descending
```
[1, 3]   → slack 2
[2, 4]   → slack 2
[8, 9]   → slack 1
[10, 11] → slack 1
[10, 12] → slack 2     ← actually slack 2 too; tie-breaking is fine either way
```
Sorted (one valid order):
```
[1, 3], [2, 4], [10, 12], [10, 11], [8, 9]
```

### Binary search for smallest energy that finishes all tasks
```
low = 0, high = 10^9
mid = 5*10^8 → is_valid → True → ans = 5*10^8, high = mid-1
... (collapses quickly to the boundary)
Eventually narrows around 32:
  E = 32: 32≥3, →31; 31≥4, →29; 29≥12, →19; 19≥11, →9; 9≥9, →1.  ✓
  E = 31: 31≥3, →30; 30≥4, →28; 28≥12, →18; 18≥11, →7; 7≥9?  ✗
Smallest passing E = 32.
```
Return `32`. ✅

---

## ⏱️ Time Complexity
```
O(n log n · log V)
```
Where `n = len(tasks)` and `V` is the binary-search range (`10^9`). Each validator call sorts in `O(n log n)`; there are `O(log V)` validator calls.

> The pure-greedy [[1665_minimum_initial_energy_to_finish_tasks_v2]] does it in a single `O(n log n)` pass — strictly faster — but this binary-search framing is the safer template when the optimal ordering isn't obvious.

## 💾 Space Complexity
```
O(n)
```
For the sorted copy inside `is_valid`. We deliberately do not mutate the caller's list.

---

## ⚠️ Edge Cases
- **Single task `[a, m]`**: answer is `m` — you need at least the minimum to start, and you finish with `m - a` left over.
- **`actual_i == minimum_i` for all tasks**: no slack anywhere, every task drains you to exactly the prereq of the next. Answer is `sum(actual_i)`.
- **All tasks identical**: order doesn't matter; answer is `(n-1) * a + m` for `n` copies of `[a, m]` — you need `m` to start the last one, having spent `(n-1)*a` before it.
- **Re-sorting inside the validator**: sorting once outside is faster, but be careful — the function as written is **pure** (no mutation), which is the right default if `tasks` is reused.
- **Upper bound `10^9`**: `sum(actual_i) ≤ 10^5 · 10^4 = 10^9`, plus `max(minimum_i) ≤ 10^4`, so `10^9` safely upper-bounds the answer. Using `10^4 * n` is also fine and tighter.

---

## 🎯 Interview Takeaways
- **Binary search on the answer** is the right reflex any time the predicate "is `X` feasible?" is monotonic and easier to verify than to optimize.
- The key sort key here is `minimum - actual` (the "buffer", how much extra you need *beyond* the cost). Sorting descending lets you spend the largest buffers first, when your energy is highest.
- Don't mutate caller-provided lists inside a helper — it bites you when the helper is invoked repeatedly (as it is here, by the binary search).
- This problem is a sibling of 1326 (Min Taps to Water a Garden) and 2071 (Max Tasks With Energy / Pills) — same flavor of "schedule to minimize an initial-resource requirement."

---

## 📌 Key Pattern
👉 **"When optimal order is unclear, binary-search the answer and let a sorted-greedy validator decide feasibility — sort by `requirement − cost` descending."**

---

## 🔁 Related Problems
- 1326. Minimum Number of Taps to Open to Water a Garden
- 2071. Maximum Number of Tasks You Can Assign
- 630. Course Schedule III
- 871. Minimum Number of Refueling Stops
- 1383. Maximum Performance of a Team

---

## 🚀 Final Thoughts
Two ways to solve this: binary search the answer with a greedy validator (this file), or skip the binary search and prove the greedy ordering directly (see [[1665_minimum_initial_energy_to_finish_tasks_v2]]). The greedy-only version is faster, but binary search is the more **discoverable** approach under interview pressure — you don't have to invent the exchange argument on the fly.

---

✨ **Rule to remember:**
> If the predicate is monotonic, binary-search the answer. The validator only has to be *correct*, not *optimal* — let the search wring out the minimum.
