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
- `minimum_i` is the energy you must already have to **start** task `i`.

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

Two ways to convert that intuition into code:
- **Approach 1** — don't trust the sort key, *binary-search* the answer and let a greedy validator confirm feasibility. Slower but bulletproof.
- **Approach 2** — trust the sort key, do a single greedy pass. Faster, but requires the exchange argument.

---

## ⚡ Approach 1 — Binary Search on the Answer + Greedy Validator

### 🧠 Idea
1. Define `is_valid(tasks, energy)`: starting with `energy`, can we finish all tasks in **some** order?
   - Sort tasks by `minimum_i - actual_i` descending (largest "slack requirement" first).
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

## ⚡ Approach 2 — Sorted Greedy Simulation

### 🧠 Idea
Skip the binary search. Sort once by `minimum_i - actual_i` descending and simulate:

- Track `current` (energy left after the tasks already finished) and `energy` (the running answer — total starting energy committed so far).
- For each `[actual, minimum]`:
  - If `current < minimum`, we don't have enough to start. Top up by exactly the deficit: `energy += (minimum - current); current = minimum`.
  - Subtract `actual` to do the task: `current -= actual`.

Total of top-ups is the answer. `O(n log n)` for the sort, `O(n)` for the walk — strictly faster than Approach 1.

```python
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:

        # Sort by (minimum - actual) descending
        tasks.sort(key=lambda x: (x[1] - x[0]), reverse=True)

        energy = 0
        current = 0

        for actual, minimum in tasks:

            # If current energy is less than required minimum
            if current < minimum:
                energy += (minimum - current)
                current = minimum

            # Do the task
            current -= actual

        return energy
```

---

## 🧠 Dry Run

### Input
```
tasks = [[1, 3], [2, 4], [10, 11], [10, 12], [8, 9]]
```

### Sort key — `minimum - actual` descending
slacks: `[1,3]→2, [2,4]→2, [10,12]→2, [8,9]→1, [10,11]→1`

One stable ordering (Python keeps insertion order on ties):
```
[1, 3], [2, 4], [10, 12], [8, 9], [10, 11]
```

### Steps (Approach 2 — direct simulation)
```
start:  current = 0, energy = 0

[1, 3]:  current(0) < 3  → energy += 3,  current = 3
         do task:  current = 3 - 1 = 2

[2, 4]:  current(2) < 4  → energy += 2,  current = 4
         do task:  current = 4 - 2 = 2

[10,12]: current(2) < 12 → energy += 10, current = 12
         do task:  current = 12 - 10 = 2

[8, 9]:  current(2) < 9  → energy += 7,  current = 9
         do task:  current = 9 - 8 = 1

[10,11]: current(1) < 11 → energy += 10, current = 11
         do task:  current = 11 - 10 = 1
```
Return `energy = 32`.

### Steps (Approach 1 — binary search collapses to the same value)
```
low = 0, high = 10^9
... binary search narrows around 32 ...
  E = 32: 32≥3→31; 31≥4→29; 29≥12→17; 17≥9→9; 9≥11? ✗   (order varies by tie-break)
          using the [1,3],[2,4],[10,12],[10,11],[8,9] order:
          32≥3→31; 31≥4→29; 29≥12→19; 19≥11→9; 9≥9→1.  ✓
  E = 31: same walk fails on the last step.
Smallest passing E = 32.
```
Both approaches return `32`. ✅

---

## ⏱️ Time Complexity
```
Approach 1: O(n log n · log V) — validator sort × log of the energy range V ≈ 10^9
Approach 2: O(n log n)         — one sort plus a linear pass
```

## 💾 Space Complexity
```
Approach 1: O(n) — sorted copy inside the validator (does not mutate caller's list)
Approach 2: O(1) extra — in-place sort; use `sorted(...)` if you need to preserve input
```

---

## ⚠️ Edge Cases
- **Single task `[a, m]`**: answer is `m` — you need at least the minimum to start, and you finish with `m - a` left over.
- **`actual_i == minimum_i` for all tasks**: no slack anywhere. Answer is `sum(actual_i)`.
- **All tasks identical `[a, m]`** (`n` copies): answer is `(n-1) * a + m`. You need `m` to start the last one, having spent `(n-1) * a` before it.
- **Tie-breaking on `minimum - actual`**: any tie order works. Swapping two adjacent tasks with equal slack doesn't change the peak requirement (the exchange argument).
- **Mutation**: Approach 1 deliberately uses `sorted(...)` (no mutation) because the validator is called many times. Approach 2 uses `tasks.sort(...)` in place — fine for LeetCode, but switch to `sorted(...)` if the caller reuses the list.
- **Upper bound `10^9`** for the binary search: `sum(actual_i) ≤ 10^5 · 10^4 = 10^9`, plus `max(minimum_i) ≤ 10^4`, so `10^9` safely upper-bounds the answer. `n * max(minimum)` is tighter.
- **Overflow** (C++/Java): cast to `long long`. In Python, irrelevant.

---

## 🎯 Interview Takeaways
- **Binary search on the answer** is the right reflex any time the feasibility predicate is monotonic and easier to verify than to optimize. Use Approach 1 if you can't justify the sort key under pressure.
- **The sort key is `minimum - actual`, descending** — the "buffer" required beyond the cost. Sorting by `minimum` alone or `actual` alone both fail on small adversarial cases.
- The pure-greedy approach (Approach 2) is justified by an **exchange argument**: swapping two adjacent tasks with the sort key flipped never decreases the required initial energy.
- Don't mutate caller-provided lists inside a repeatedly-invoked helper. Approach 1's `sorted(...)` is intentional.

---

## 📌 Key Pattern
👉 **"To minimize the peak resource ever needed, schedule items by `requirement − cost` descending. If the sort key isn't obvious, binary-search the answer and let the greedy validator decide."**

---

## 🔁 Related Problems
- 1326. Minimum Number of Taps to Open to Water a Garden
- 2071. Maximum Number of Tasks You Can Assign
- 630. Course Schedule III
- 871. Minimum Number of Refueling Stops
- 1383. Maximum Performance of a Team
- 502. IPO

---

## 🚀 Final Thoughts
Two clean approaches: binary-search-the-answer (discoverable but `log V` slower) and pure greedy (fast but requires you to trust the exchange argument). Code Approach 1 first under interview pressure; refactor to Approach 2 if time permits or the interviewer pushes for the optimal complexity.

---

✨ **Rule to remember:**
> Greedy beats binary search when you can prove the sort key. The proof is an exchange argument; the key is `requirement − cost`, descending.
