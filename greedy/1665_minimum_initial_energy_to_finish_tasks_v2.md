# 1665. Minimum Initial Energy to Finish Tasks (v2)

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

Return the **minimum initial energy** required to finish all tasks, in any order.

### 📌 Constraints
- `1 <= tasks.length <= 10^5`
- `1 <= actual_i <= minimum_i <= 10^4`

---

## 💭 Intuition
Instead of binary-searching the answer (see [[1665_minimum_initial_energy_to_finish_tasks]]), simulate directly:

- Process tasks in the order **largest `minimum_i - actual_i` first**.
- Track the current energy you "need to have collected so far." Whenever the next task's `minimum_i` exceeds what you've collected minus what you've spent, top up by exactly the deficit.

That total of top-ups is the answer. The sort key `(minimum - actual)` is the classic exchange argument: tasks with a *large gap* between start-requirement and spend are the ones that bite you if you do them late, when your reserve is thin. Doing them while your reserve is fat costs nothing extra; doing them later may force you to top up *retroactively*.

---

## ⚡ Approach — Sorted Greedy Simulation

### 🧠 Idea
1. Sort tasks by `minimum_i - actual_i` descending.
2. Walk the list with two counters:
   - `current`: the running energy left after finishing the tasks processed so far.
   - `energy`: the total starting energy we've committed to (the answer-in-progress).
3. For each `[actual, minimum]`:
   - If `current < minimum`, we don't have enough to *start*: bump `energy` by `(minimum - current)` and set `current = minimum`.
   - Subtract `actual` from `current` (do the task).
4. Return `energy`.

The sort is `O(n log n)`; the walk is `O(n)`. No binary search needed.

---

## 💻 Code

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

### Sorted by (minimum - actual) descending
slacks: `[1,3]→2, [2,4]→2, [10,12]→2, [8,9]→1, [10,11]→1`

One stable ordering (Python keeps insertion order on ties):
```
[1, 3], [2, 4], [10, 12], [8, 9], [10, 11]
```

### Walk
```
start:  current = 0, energy = 0

[1, 3]:  current(0) < 3 → energy += 3, current = 3
         do task: current = 3 - 1 = 2
         current=2, energy=3

[2, 4]:  current(2) < 4 → energy += 2, current = 4
         do task: current = 4 - 2 = 2
         current=2, energy=5

[10,12]: current(2) < 12 → energy += 10, current = 12
         do task: current = 12 - 10 = 2
         current=2, energy=15

[8, 9]:  current(2) < 9 → energy += 7, current = 9
         do task: current = 9 - 8 = 1
         current=1, energy=22

[10,11]: current(1) < 11 → energy += 10, current = 11
         do task: current = 11 - 10 = 1
         current=1, energy=32
```
Return `32`. ✅ (Matches the binary-search version.)

---

## ⏱️ Time Complexity
```
O(n log n) — one sort plus a linear pass.
```
Strictly faster than the binary-search variant, which does `O(n log n)` *per probe*.

## 💾 Space Complexity
```
O(1) extra
```
The sort is in-place (`tasks.sort(...)`). If you must preserve the caller's list, use `sorted(...)` and pay `O(n)`.

---

## ⚠️ Edge Cases
- **`tasks.sort` mutates the input**. If the grader reuses `tasks` after `minimumEffort`, this changes observable behavior. The v1 file deliberately uses `sorted(...)` for that reason. On LeetCode it's harmless.
- **Tie-breaking on `minimum - actual`**: any tie order works. The proof goes through because swapping two adjacent tasks with equal slack doesn't change the peak requirement.
- **All `actual_i == minimum_i`**: slack 0 everywhere; sort order is whatever Python gives back. Answer collapses to `sum(actual_i)`.
- **One task**: loop runs once; `energy = minimum`, `current = minimum - actual`. Return `minimum`. Correct.
- **Integer overflow**: in Python irrelevant. In C++/Java cast to `long long` — `n * max(minimum)` can be up to `10^9`, still in `int32`, but safer to be explicit.

---

## 🎯 Interview Takeaways
- The greedy here is the **exchange argument**: show that swapping any two out-of-order pairs doesn't decrease the required initial energy. That justifies sorting by `minimum - actual` descending.
- This is a tighter solution than [[1665_minimum_initial_energy_to_finish_tasks]] but requires you to *trust the sort key*. If you don't, fall back to binary search — same answer, slower but bulletproof.
- "Top up only when needed, then subtract" is the same pattern as min-heap scheduling problems (e.g. 871 Refueling Stops with a heap, but here a sort suffices because we don't need to re-pick the next task adaptively).
- A common bug: sorting by `minimum` alone or `actual` alone — both fail on small adversarial cases. The *difference* is what matters.

---

## 📌 Key Pattern
👉 **"To minimize the peak resource you ever need, schedule items by `requirement − cost` descending and simulate."**

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
Same answer as the binary-search version in one pass. The trick is knowing the sort key — `minimum - actual`, descending — which is hard to invent from scratch but easy to remember once you've seen it. When in doubt under pressure, code the binary-search version first; if time permits, refactor to this.

---

✨ **Rule to remember:**
> Greedy beats binary search when you can prove the right sort key. The proof is an exchange argument; the sort key is `requirement − cost`.
