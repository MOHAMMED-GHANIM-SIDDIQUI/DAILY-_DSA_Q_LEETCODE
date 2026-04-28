# 3577. Count the Number of Computer Unlocking Permutations

## 🔗 Problem Link
https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Math, Combinatorics

---

## 🧩 Problem Summary
Given an array `complexity` where `complexity[0]` is the starting computer, count the number of permutations of computers [1..n-1] such that each computer can be unlocked by a previously unlocked computer with strictly lower complexity. Return the count modulo 10^9 + 7.

### 📌 Constraints
- `2 <= complexity.length <= 10^5`
- `1 <= complexity[i] <= 10^9`

---

## 💭 Intuition
👉 Computer 0 is always first (it's the starting point). Every other computer must have complexity strictly greater than `complexity[0]`. If any computer has complexity <= complexity[0], it can never be unlocked, so return 0. Otherwise, all (n-1)! orderings of the remaining computers work.

---

## ⚡ Approach — Factorial with Validation

### 🧠 Idea
- Check that `complexity[0]` is strictly less than all other complexities.
- If any `complexity[i] <= complexity[0]` for i > 0, return 0.
- Otherwise, the answer is `(n - 1)! mod (10^9 + 7)`.

---

## 💻 Code

```python
class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(complexity)

        # Track minimum prefix complexity up to i-1
        pref_min = complexity[0]

        for i in range(1, n):
            if pref_min >= complexity[i]:
                return 0
            pref_min = min(pref_min, complexity[i])

        # If all unlockable, count is (n - 1)!
        ans = 1
        for k in range(1, n):
            ans = ans * k % MOD
        return ans
```

---

## 🧠 Dry Run
### Input
```
complexity = [1, 3, 2, 4]
```
### Steps
```
pref_min = 1
i=1: pref_min(1) < complexity[1](3)? Yes. pref_min = min(1,3) = 1
i=2: pref_min(1) < complexity[2](2)? Yes. pref_min = min(1,2) = 1
i=3: pref_min(1) < complexity[3](4)? Yes. pref_min = min(1,4) = 1

All pass. Answer = (4-1)! = 3! = 6

Result: 6
```

---

## ⏱️ Time Complexity
```
O(n) — single pass for validation + factorial computation
```

## 💾 Space Complexity
```
O(1) — constant extra space
```

---

## ⚠️ Edge Cases
- complexity[0] is the maximum → return 0 (no computer can be unlocked)
- All complexities equal → return 0
- Two computers → return 1 if complexity[1] > complexity[0], else 0

---

## 🎯 Interview Takeaways
- Recognize when a complex-sounding problem reduces to a simple combinatorial check.
- The starting element being the minimum is the necessary and sufficient condition.
- Factorial mod computation is a basic building block.

---

## 📌 Key Pattern
👉 **"Validate a minimum condition, then count as factorial — a permutation problem in disguise."**

---

## 🔁 Related Problems
- 1569. Number of Ways to Reorder Array to Get Same BST
- 62. Unique Paths (combinatorics)
- 1359. Count All Valid Pickup and Delivery Options

---

## 🚀 Final Thoughts
Despite its complex description, this problem boils down to checking if the first element is the unique minimum and computing (n-1)! if so. Recognizing this simplification is the key challenge.

---

✨ **Rule to remember:**
> When the first element must be the root and all others are unconstrained relative to each other, the answer is (n-1)!.
