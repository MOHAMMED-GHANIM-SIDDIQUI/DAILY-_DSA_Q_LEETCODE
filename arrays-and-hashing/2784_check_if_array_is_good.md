# 2784. Check if Array Is Good

## 🔗 Problem Link
https://leetcode.com/problems/check-if-array-is-good/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Hash Table, Sorting

---

## 🧩 Problem Summary
You are given an integer array `nums`. The array is called **good** if it is a permutation of `base[n] = [1, 2, ..., n - 1, n, n]` for some `n >= 1` — i.e. an array of length `n + 1` that contains each of `1..n-1` exactly once and the value `n` exactly twice. Return `True` if `nums` is good, otherwise `False`.

### 📌 Constraints
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 200`

---

## 💭 Intuition
If `nums` is a permutation of `base[n]`, then `len(nums) = n + 1`, so `n = len(nums) - 1` is forced. With `n` pinned, "good" reduces to two structural facts:

1. The **set of values** in `nums` is exactly `{1, 2, ..., n}` — no extras, no missing.
2. The largest value `n` appears **exactly twice** (everything else once).

Together those two checks pin the multiset down to `base[n]` without sorting. The set comparison handles uniqueness and range; the count check handles the one duplicate that's allowed.

---

## ⚡ Approach — Set Match + Duplicate Count

### 🧠 Idea
1. Let `n = len(nums) - 1`.
2. Build `set(nums)` and compare against `{1, 2, ..., n}`. If they differ, return `False`.
3. Check that `n` occurs exactly twice in `nums`. If not, return `False`.
4. Otherwise return `True`.

The set check rules out values outside `1..n` and missing values inside; the count check rules out the wrong element being duplicated.

---

## 💻 Code

```python
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        set_num = set(nums)
        real_set = set([i for i in range(1, len(nums))])
        if set_num == real_set and nums.count(len(nums) - 1) == 2:
            return True
        return False
```

---

## 🧠 Dry Run
### Input
```
nums = [2, 1, 3, 3]
```

### Steps
```
n = len(nums) - 1 = 3
set_num  = {1, 2, 3}
real_set = set(range(1, 4)) = {1, 2, 3}
set_num == real_set  →  True
nums.count(3) == 2   →  True
return True ✅
```

### Counter-example
```
nums = [1, 3, 3, 2]      → set_num={1,2,3}, count(3)=2  ✅ good
nums = [3, 4, 4, 1, 2, 1] → set_num={1,2,3,4}, real_set={1,2,3,4,5}  → False
nums = [1, 1]            → n=1, set_num={1}, real_set={1}, count(1)=2 → True
```

---

## ⏱️ Time Complexity
```
O(N)   one pass to build the set, one pass for .count, one to build real_set.
```

## 💾 Space Complexity
```
O(N)   set_num and real_set each hold up to n distinct integers.
```

---

## ⚠️ Edge Cases
- **`nums = [1, 1]`** → `n = 1`, `real_set = set(range(1,2)) = {1}`, `count(1) == 2`. Returns `True`. The smallest good array.
- **Value out of range** (e.g. `nums = [1, 2, 4, 4]` of length 4): `real_set = {1,2,3}` but `set_num = {1,2,4}` → mismatch → `False`.
- **Wrong element duplicated** (e.g. `nums = [1, 1, 2, 3]`): `set_num = real_set = {1,2,3}` but `count(3) = 1`, not 2 → `False`.
- **All identical** (e.g. `nums = [2, 2, 2]`): `set_num = {2}`, `real_set = {1, 2}` → mismatch → `False`.

---

## 🎯 Interview Takeaways
- For "is this a permutation of a known shape" problems, pin down the implied parameter (`n` here) from the length first — it collapses the question to a structural check.
- A **set equality** check is a clean way to assert "exactly this collection of distinct values, nothing more, nothing missing" in one line.
- Set equality alone isn't enough when duplicates carry meaning — pair it with a targeted `count` for the one value that's allowed to repeat.
- Equivalent one-pass alternative using `Counter`: build the expected counter `{i: 1 for i in 1..n-1} | {n: 2}` and compare to `Counter(nums)`. Same idea, slightly less arithmetic juggling.

---

## 📌 Key Pattern
👉 **"Permutation-of-a-known-shape → derive `n` from length, then check set + targeted duplicate count."**

---

## 🔁 Related Problems
- 1. Two Sum
- 268. Missing Number
- 287. Find the Duplicate Number
- 442. Find All Duplicates in an Array
- 448. Find All Numbers Disappeared in an Array

---

## 🚀 Final Thoughts
A short hashing problem with a small twist: the "good" shape allows exactly one duplicate at a known position. Once you notice that `n` is fully determined by the length, the rest is just two independent integrity checks — set membership and a single count. Don't sort; sorting trades `O(N)` for `O(N log N)` with no gain.

---

✨ **Rule to remember:**
> When the answer depends on "is this a permutation of X?", derive the parameter of X from the input's length first, then verify with a set comparison plus targeted counts. Hashing beats sorting here.
