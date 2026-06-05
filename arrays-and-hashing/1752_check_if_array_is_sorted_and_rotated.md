# 1752. Check if Array Is Sorted and Rotated

## 🔗 Problem Link
https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array

---

## 🧩 Problem Summary
Given an array `nums`, return `True` if it was originally sorted in **non-decreasing** order and then **rotated** some number of positions (including zero). Otherwise return `False`. Values may repeat.

### 📌 Constraints
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`

---

## 💭 Intuition
A sorted-then-rotated array is a sorted array that "wraps around" at exactly **one** point. Walking the array circularly, every adjacent pair should satisfy `nums[i] <= nums[i+1]` — except at the single seam where the rotation happened (where a larger value is followed by the smaller start).

So the rule is: **count the number of "drops"** (places where the current element is greater than the next, going circularly). If there are `0` drops the array is already sorted; if there is exactly `1` drop it is a valid rotation; `2` or more drops means it can never be a single rotation of a sorted array.

---

## ⚡ Approach — Count circular descents

### 🧠 Idea
1. Walk `i` from `0` to `n-1`.
2. Compare `nums[i]` with `nums[(i + 1) % n]` — the modulo lets the last element compare against the first, closing the circle.
3. Every time `nums[i] > nums[(i+1) % n]`, increment `mistakes`.
4. If `mistakes` ever exceeds `1`, return `False` early.
5. Survive the loop → return `True`.

---

## 💻 Code

```python
class Solution:
    def check(self, nums):
        n = len(nums)
        mistakes = 0

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                mistakes += 1

            if mistakes > 1:
                return False

        return True
```

---

## 🧠 Dry Run
### Input
```
nums = [3, 4, 5, 1, 2]
```

### Trace
```
i=0: 3 <= 4            mistakes=0
i=1: 4 <= 5            mistakes=0
i=2: 5 >  1            mistakes=1   ← the rotation seam
i=3: 1 <= 2            mistakes=1
i=4: 2 >  3 (wrap)?  2 <= 3 → no   mistakes=1
```
Exactly one drop → `True`.

### Counter-example
```
nums = [2, 1, 3, 4]
i=0: 2 > 1   mistakes=1
i=2: 4 > 2 (wrap)  mistakes=2 → False
```

---

## ⏱️ Time Complexity
```
O(n)   — one circular pass.
```

## 💾 Space Complexity
```
O(1)   — only a counter.
```

---

## ⚠️ Edge Cases
- **Already sorted** (`[1,2,3]`) → `0` drops → `True`.
- **All equal** (`[2,2,2]`) → no strict `>` anywhere → `True`.
- **Single element** → loop compares it to itself via `% n`, `nums[0] > nums[0]` is false → `True`.
- **Strictly decreasing** (`[3,2,1]`) → two drops → `False`.

---

## 🎯 Interview Takeaways
- The "rotated sorted array has exactly one inversion point" invariant is the same fact binary search on rotated arrays relies on (LC 33 / 153 / 154).
- The `% n` wrap is the clean way to fold the "last vs first" check into the same loop instead of special-casing it afterward.

---

## 📌 Key Pattern
👉 **"A sorted-then-rotated array has at most one circular descent. Count drops over `(i, (i+1) % n)`; ≤ 1 ⇒ valid."**

---

## 🔁 Related Problems
- 33. Search in Rotated Sorted Array
- 153. Find Minimum in Rotated Sorted Array
- 154. Find Minimum in Rotated Sorted Array II
- 1539. Kth Missing Positive Number

---

## 🚀 Final Thoughts
The trick is reframing "sorted and rotated" into a counting problem instead of trying to find the pivot and re-sort. One pass, one counter, one modulo — and the early exit on the second mistake makes it self-documenting.

---

✨ **Rule to remember:**
> Rotation introduces exactly one seam. Whenever a problem says "sorted then rotated," think *count the inversions on the circle* — the answer is about how many seams exist, not where they are.
