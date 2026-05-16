# 154. Find Minimum in Rotated Sorted Array II

## 🔗 Problem Link
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Binary Search

---

## 🧩 Problem Summary
Given a sorted array `nums` that **may contain duplicates** and has been rotated between `1` and `n` times (a full `n` rotation is allowed — i.e. it can look unrotated), return the **minimum** element. Aim for `O(log n)` on average; `O(n)` worst case is allowed when duplicates collapse the partition.

### 📌 Constraints
- `n == nums.length`
- `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
- `nums` is sorted and rotated between `1` and `n` times.
- Duplicates are **allowed**.

---

## 💭 Intuition
LC 153 (uniques) solves this in `O(log n)` by anchoring against `nums[high]`: if `nums[mid] > nums[high]` the drop is right of `mid`; otherwise it's at `mid` or to its left. Two branches, log time.

Duplicates break that two-branch decision in **one specific case**: when `nums[mid] == nums[high]`. Now we can't tell which half holds the minimum.

- `[3, 3, 1, 3]` → `mid=1`, `nums[1]=3`, `nums[3]=3` — the answer is in the **left** half.
- `[3, 1, 3, 3]` → `mid=1`, `nums[1]=1`, `nums[3]=3` — strict comparison still works here, but if the value at mid had tied with high we'd be stuck.
- `[1, 3, 3, 3]` → `mid=1`, `nums[1]=3`, `nums[3]=3` — the answer is in the **right** half.

We can't decide between left and right when they tie. The safe move: **discard one duplicate**. Set `high -= 1`. The element we drop has a duplicate at the same value at `mid`, so it can't be the unique minimum candidate we'd lose — even if it *were* the minimum, `nums[mid]` (which equals it) is still in the window. We're shrinking by one instead of halving, which gives `O(n)` worst case (all elements equal), but `O(log n)` on average.

This is the textbook "binary-search with a duplicates fallback" pattern.

---

## ⚡ Approach — Binary Search with Tie-Shrink

### 🧠 Idea
1. `low = 0`, `high = len(nums) - 1`.
2. While `low < high`:
   - `mid = low + (high - low) // 2`
   - If `nums[mid] < nums[high]` → minimum is at `mid` or to its left → `high = mid`.
   - Else if `nums[mid] > nums[high]` → minimum is strictly to the right of `mid` → `low = mid + 1`.
   - Else (`nums[mid] == nums[high]`) → can't decide → `high -= 1` (safely discard the tie).
3. Return `nums[low]`.

### 🔑 Why dropping `high` (not advancing `low`) on the tie
The branches above use `nums[high]` as the **anchor**. The discard mirrors the anchor: we shrink from the high side so the anchor on the next iteration is still meaningful (`nums[high-1]`). Advancing `low` on a tie would change which side acts as the anchor and break the partition logic.

### 🔑 Why `high -= 1` is safe
Suppose the minimum lives only at index `high` (the value we're about to drop). Then `nums[high] = min`, and we're told `nums[mid] == nums[high] = min`. So `mid` is *also* a minimum, and the answer is preserved within `[low, high - 1]`. We never lose the answer by dropping a duplicate of the anchor.

---

## 💻 Code

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2

            if nums[mid] < nums[high]:
                high = mid

            elif nums[mid] > nums[high]:
                low = mid + 1

            else:
                high -= 1

        return nums[low]
```

---

## 🧠 Dry Run
### Input
```
nums = [2, 2, 2, 0, 1]
```

### Steps
```
low=0, high=4
  mid=2, nums[2]=2, nums[4]=1 → 2 > 1 → low=3
low=3, high=4
  mid=3, nums[3]=0, nums[4]=1 → 0 < 1 → high=3
low=3, high=3 → exit
return nums[3] = 0 ✅
```

### Tie-shrink case
```
nums = [3, 3, 1, 3]
low=0, high=3
  mid=1, nums[1]=3, nums[3]=3 → tie → high=2
low=0, high=2
  mid=1, nums[1]=3, nums[2]=1 → 3 > 1 → low=2
low=2, high=2 → exit
return nums[2] = 1 ✅
```

### All-duplicates worst case
```
nums = [3, 3, 3, 3]
Each iteration ties → high decremented by 1 → O(n) shrink.
Loop exits at low=0, high=0. Return 3. ✅
```

---

## ⏱️ Time Complexity
```
Average: O(log n)   each strict-comparison iteration halves the window.
Worst:   O(n)       when all elements are equal, every iteration does high -= 1.
```

## 💾 Space Complexity
```
O(1)   two integer pointers.
```

---

## ⚠️ Edge Cases
- **No duplicates** → behaves exactly like LC 153: the tie branch never fires, `O(log n)` throughout.
- **All equal** (`[2, 2, 2, 2]`) → every step hits the tie branch, `O(n)` total, returns the only value.
- **Single element** → loop is skipped; returns `nums[0]`.
- **Unrotated** (`[1, 2, 3]`) → `nums[mid] <= nums[high]` always; `high` walks down to `0`. Returns `nums[0]`.
- **Pivot at the end** (`[1]` rotated `n` times equals itself) → covered by the unrotated branch.
- **Duplicates straddling the pivot** (`[3, 1, 3]`) → `mid=1`, `nums[1]=1 < nums[2]=3` → `high=1`. Correctly returns `1`.

### ⚠️ Don't replace the tie branch with `low += 1`
`low += 1` is *also* safe in isolation, but only when paired with a `nums[low]`-anchored partition. With this template (anchored on `nums[high]`), the tie shrink must come from the **high** side, otherwise the partition invariant breaks on the next iteration.

---

## 🎯 Interview Takeaways
- This is the canonical "binary search degrades to linear on duplicates" pattern. The shape is: two strict-comparison branches that keep you logarithmic, plus a tie branch that shrinks by one to stay safe.
- Anchor and shrink must match sides: `nums[high]` anchor → `high -= 1` on tie. If you flip the anchor to `nums[low]`, flip the shrink to `low += 1`.
- The `O(n)` worst case is unavoidable for this problem — adversarial input `[1, 1, 1, ..., 1, 0, 1]` forces it. Mention this trade-off when discussing complexity.
- This generalizes to LC 81 (Search in Rotated Sorted Array II) — same tie-shrink idea added to LC 33's template.

---

## 📌 Key Pattern
👉 **"Rotated sorted + duplicates → LC 153 template plus a `high -= 1` tie branch. Logarithmic average, linear worst case."**

---

## 🔁 Related Problems
- 33. Search in Rotated Sorted Array
- 81. Search in Rotated Sorted Array II
- 153. Find Minimum in Rotated Sorted Array
- 162. Find Peak Element
- 540. Single Element in a Sorted Array

---

## 🚀 Final Thoughts
LC 154 is what LC 153 looks like when you remove the uniqueness guarantee — and the fix is a single extra branch. The reason this is rated Hard isn't the code (it's three branches), it's the proof that `high -= 1` is safe on ties and that you must keep the shrink direction aligned with the anchor. Internalize "anchor side and shrink side must match," and the whole family of rotated-array problems collapses to one template.

---

✨ **Rule to remember:**
> When duplicates break a binary-search partition decision, shrink by **one** on the anchor side (`high -= 1` for `nums[high]`-anchored, `low += 1` for `nums[low]`-anchored). Accept `O(n)` worst case as the cost of correctness.
