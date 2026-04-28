# 1437. Check If All 1's Are at Least Length K Places Away

## 🔗 Problem Link
https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array

---

## 🧩 Problem Summary
Given a binary array `nums` and an integer `k`, return `true` if all `1`s are at least `k` places away from each other, otherwise return `false`.

### 📌 Constraints
- `1 <= nums.length <= 10^5`
- `0 <= k <= nums.length`
- `nums[i]` is `0` or `1`

---

## 💭 Intuition
👉 Track the position of the last seen `1`. When we encounter the next `1`, check if the gap is at least `k`. A two-pointer style scan handles this in one pass.

---

## ⚡ Approach — Two-Pointer Gap Check

### 🧠 Idea
- Use `curr` to track the last position of a `1`, and `next` to scan forward.
- When `next` finds a `1`:
  - If `curr` was also a `1` and the distance `next - curr <= k`, return `False`.
  - Update `curr = next`.
- If `k == 0`, immediately return `True` (no spacing required).

---

## 💻 Code

```python
class Solution:
  def kLengthApart(self, nums: list[int], k: int) -> bool:
    if k == 0:
      return True

    n = len(nums)
    curr = 0
    next = 1

    while curr < n and next < n:
      if nums[next] == 1:
        if nums[curr] == 1 and next - curr <= k:
          return False
        curr = next
      next += 1

    return True
```

---

## 🧠 Dry Run
### Input
```
nums = [1, 0, 0, 0, 1, 0, 0, 1, 0, 0], k = 2
```
### Steps
```
curr=0 (val=1), next=1
next=1: val=0 → skip, next=2
next=2: val=0 → skip, next=3
next=3: val=0 → skip, next=4
next=4: val=1, curr=0 is 1, gap=4-0=4 > 2 ✓ → curr=4, next=5
next=5: val=0 → skip, next=6
next=6: val=0 → skip, next=7
next=7: val=1, curr=4 is 1, gap=7-4=3 > 2 ✓ → curr=7, next=8
next=8,9: val=0 → skip
Result = True
```

---

## ⏱️ Time Complexity
```
O(n)
```

## 💾 Space Complexity
```
O(1)
```

---

## ⚠️ Edge Cases
- `k = 0` → always true, no spacing needed
- No `1`s in the array → trivially true
- Only one `1` → trivially true
- Two `1`s adjacent with `k >= 1` → false

---

## 🎯 Interview Takeaways
- A single pass with two pointers is sufficient for gap-checking problems.
- Early return for `k = 0` avoids unnecessary work.
- Tracking the last seen position of a target value is a common pattern.

---

## 📌 Key Pattern
👉 **"Track last occurrence and check gap distance — one-pass linear scan."**

---

## 🔁 Related Problems
- 605. Can Place Flowers
- 849. Maximize Distance to Closest Person
- 821. Shortest Distance to a Character

---

## 🚀 Final Thoughts
A clean one-pass problem. Track the previous `1`, check the gap when the next `1` appears, and return false immediately if the constraint is violated.

---

✨ **Rule to remember:**
> To verify spacing constraints, track the last occurrence and check distance on each new match.
