# 1863. Sum of All Subset XOR Totals

## 🔗 Problem Link
https://leetcode.com/problems/sum-of-all-subset-xor-totals/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Math, Bit Manipulation, Backtracking, Combinatorics

---

## 🧩 Problem Summary
Given an array `nums`, return the sum of all XOR totals for every subset. The XOR total of a subset is the XOR of all its elements, or 0 if the subset is empty.

### 📌 Constraints
- `1 <= nums.length <= 12`
- `1 <= nums[i] <= 20`

---

## 💭 Intuition
👉 Each bit position contributes to exactly half of all subsets. The OR of all elements gives us which bits appear at all, and each such bit contributes `2^(n-1)` times across all subsets. So the answer is `(OR of all elements) << (n-1)`.

---

## ⚡ Approach — Bit Manipulation (Mathematical)

### 🧠 Idea
- Compute the OR of all elements (this tells us which bits are present in any element).
- Each bit that is set in any element will appear in exactly half of all `2^n` subsets.
- Multiply the OR by `2^(n-1)` using a left shift.

---

## 💻 Code

```cpp
class Solution {
 public:
  int subsetXORSum(vector<int>& nums) {
    return accumulate(nums.begin(), nums.end(), 0, bit_or<>())
           << nums.size() - 1;
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [1, 3]
```
### Steps
```
OR of all elements: 1 | 3 = 3 (binary: 11)
n = 2, shift by n-1 = 1
Result = 3 << 1 = 6

Verification: Subsets are {}, {1}, {3}, {1,3}
XOR totals: 0, 1, 3, 1^3=2
Sum = 0 + 1 + 3 + 2 = 6 ✓
```

---

## ⏱️ Time Complexity
```
O(n) for the accumulate operation
```

## 💾 Space Complexity
```
O(1)
```

---

## ⚠️ Edge Cases
- Single element: answer is the element itself (only one non-empty subset).
- All elements are the same: XOR of even count is 0, odd count is the element.

---

## 🎯 Interview Takeaways
- The mathematical insight that each bit contributes to exactly half the subsets is powerful.
- OR + shift is an O(n) solution to what seems like a 2^n problem.
- Understanding bit-level contributions across subsets is a valuable skill.

---

## 📌 Key Pattern
👉 **"Each bit set in any element contributes to half of all subsets: answer = OR(all) << (n-1)"**

---

## 🔁 Related Problems
- 78. Subsets
- 1734. Decode XORed Permutation
- 2425. Bitwise XOR of All Pairings

---

## 🚀 Final Thoughts
This is a beautiful example of how mathematical insight can reduce an exponential brute-force solution to a linear one. The key observation about bit contributions across subsets is a pattern that applies to many XOR-related problems.

---

✨ **Rule to remember:**
> "Sum of XOR over all subsets = (OR of all elements) shifted left by (n-1)."
