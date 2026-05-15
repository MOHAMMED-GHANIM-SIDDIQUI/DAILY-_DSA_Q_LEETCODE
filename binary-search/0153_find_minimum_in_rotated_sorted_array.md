# 153. Find Minimum in Rotated Sorted Array

## 🔗 Problem Link
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Binary Search

---

## 🧩 Problem Summary
A sorted array of **unique** integers has been rotated between `1` and `n` times (a full `n` rotations is also allowed). Given that rotated array `nums`, return the **minimum** element. The algorithm must run in `O(log n)` time.

### 📌 Constraints
- `n == nums.length`
- `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
- All integers in `nums` are **unique**.
- `nums` is sorted and rotated between 1 and `n` times.

---

## 💭 Intuition
A linear scan trivially solves this in `O(n)`, but the `O(log n)` requirement rules that out — we have to binary-search.

The trick is that a rotated sorted array of unique values has a single "drop" point — the minimum — and on either side of that point the values are sorted. The minimum is the **only** element smaller than its predecessor (or the first element if no rotation happened).

We can locate the drop using one anchor: compare `nums[mid]` to `nums[high]`.

- If `nums[mid] > nums[high]`, the minimum **cannot** be at `mid` or to its left — the right half contains values smaller than `nums[mid]`, so the drop is somewhere in `(mid, high]`. Move `low = mid + 1`.
- Otherwise (`nums[mid] <= nums[high]`), the segment from `mid` to `high` is already sorted, so the minimum lives at `mid` or to its left. Move `high = mid` (don't drop `mid`, it may *be* the answer).

Comparing against `nums[high]` (not `nums[low]`) is the cleaner pivot because in the unrotated case `nums[mid] <= nums[high]` is always true, so the loop naturally collapses leftward to index 0 — the correct answer when there's no rotation.

---

## ⚡ Approach — Binary Search Against the Right Anchor

### 🧠 Idea
1. Maintain `low = 0`, `high = len(nums) - 1`.
2. While `low < high`:
   - `mid = low + (high - low) // 2`
   - If `nums[mid] > nums[high]` → minimum is strictly right of `mid` → `low = mid + 1`.
   - Else → minimum is at `mid` or left of it → `high = mid`.
3. Loop terminates with `low == high` pointing at the minimum. Return `nums[low]`.

### 🔑 Why `high = mid` not `high = mid - 1`
`mid` could itself be the minimum (when `nums[mid] <= nums[high]` and `mid` is the drop). Excluding it loses the answer.

### 🔑 Why `low < high` not `low <= high`
We want the window to **converge** to a single index, not iterate past it. Strict inequality gives us a natural single-survivor loop and avoids an off-by-one when `low + 1 == high` and `mid == low`.

---

## 💻 Code

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2

            # Minimum is in right half
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                # Minimum is at mid or in left half
                high = mid

        return nums[low]
```

---

## 🧠 Dry Run
### Input
```
nums = [4, 5, 6, 7, 0, 1, 2]
```

### Steps
```
low=0, high=6
  mid=3, nums[3]=7, nums[6]=2 → 7 > 2 → low = 4
low=4, high=6
  mid=5, nums[5]=1, nums[6]=2 → 1 <= 2 → high = 5
low=4, high=5
  mid=4, nums[4]=0, nums[5]=1 → 0 <= 1 → high = 4
low=4, high=4 → exit
return nums[4] = 0 ✅
```

### Already-sorted case (full rotation)
```
nums = [1, 2, 3, 4, 5]
low=0, high=4
  mid=2, nums[2]=3 <= nums[4]=5 → high=2
low=0, high=2
  mid=1, nums[1]=2 <= nums[2]=3 → high=1
low=0, high=1
  mid=0, nums[0]=1 <= nums[1]=2 → high=0
return nums[0] = 1 ✅
```

---

## ⏱️ Time Complexity
```
O(log n)   the window halves on every iteration.
```

## 💾 Space Complexity
```
O(1)   two integer pointers, no auxiliary structures.
```

---

## ⚠️ Edge Cases
- **No rotation** (`[1, 2, 3]`): `nums[mid] <= nums[high]` always — `high` walks down to `0`. Returns `nums[0]`. ✅
- **Single element** (`[5]`): loop never enters (`low == high`); returns `nums[0]`. ✅
- **Two elements, rotated** (`[2, 1]`): `mid=0`, `nums[0]=2 > nums[1]=1` → `low=1`. Returns `1`. ✅
- **Two elements, not rotated** (`[1, 2]`): `mid=0`, `1 <= 2` → `high=0`. Returns `1`. ✅
- **Rotation equal to length** (`[3, 4, 5, 1, 2]` rotated 3 times back to itself happens to look identical to "shifted" — still works since the structural test only cares about the drop point).
- **Negative values** (`[-5, -2, -1, -10, -8]`): comparison is by value, not sign — works identically.

### ⚠️ Don't compare against `nums[low]`
A naive variant uses `if nums[mid] > nums[low]` to pick a half. That fails on `[3, 1, 2]`: `mid=1`, `nums[1]=1`, `nums[0]=3` → `1 < 3` so you'd go left, but the minimum *is* at `mid=1`. Always anchor against `nums[high]` for this template.

---

## 🎯 Interview Takeaways
- For "find the rotation point / minimum in a rotated sorted array (uniques)", the canonical binary search compares `nums[mid]` to `nums[high]` and uses `high = mid` (inclusive) on the lower-half branch.
- The two ingredients that keep this template correct: (1) the inclusive `high = mid` so we don't skip a candidate minimum, and (2) the strict-`<` loop so we converge to one index instead of overshooting.
- This is the **prep template** for LC 154 (with duplicates — adds a `nums[mid] == nums[high]: high -= 1` branch) and LC 33 (search-target-in-rotated, which extends the same partition logic).

---

## 📌 Key Pattern
👉 **"Rotated sorted (uniques) → binary search anchored at `nums[high]`, with `high = mid` on the inclusive side."**

---

## 🔁 Related Problems
- 33. Search in Rotated Sorted Array
- 81. Search in Rotated Sorted Array II
- 154. Find Minimum in Rotated Sorted Array II
- 162. Find Peak Element
- 852. Peak Index in a Mountain Array

---

## 🚀 Final Thoughts
The classic rotated-array binary search. The two design choices that make this code bulletproof — anchoring against `nums[high]` and using inclusive `high = mid` — are worth memorizing as a template, because the moment you reach for `nums[low]` as the comparator or `high = mid - 1` as the contraction, you fall into off-by-one traps that are hard to debug under interview pressure.

---

✨ **Rule to remember:**
> When binary-searching a rotated sorted array, compare `nums[mid]` to **`nums[high]`** (not `nums[low]`), and shrink with **`high = mid`** (inclusive) on the safe side. Strict-`<` loop, exit when `low == high`.
