# 2598. Smallest Missing Non-negative Integer After Operations

## 🔗 Problem Link
https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Hash Table, Math, Greedy

---

## 🧩 Problem Summary
You are given an array `nums` and an integer `value`. You can add or subtract `value` from any element any number of times. Find the smallest non-negative integer (MEX) that is NOT present in the array after performing optimal operations.

### 📌 Constraints
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `1 <= value <= 10^9`

---

## 💭 Intuition
👉 Adding/subtracting `value` from a number preserves its remainder modulo `value`. So each number `nums[i]` can become any non-negative integer with the same remainder `(nums[i] % value + value) % value`. Count how many numbers map to each remainder, then find the smallest integer whose remainder bucket is empty.

---

## ⚡ Approach — Modular Counting

### 🧠 Idea
- For each number, compute its remainder `(num % value + value) % value` and count occurrences per remainder.
- Iterate from 0 upward: for integer `i`, check if the bucket `i % value` has remaining capacity. If not, `i` is the MEX.

---

## 💻 Code

```cpp
class Solution {
 public:
  int findSmallestInteger(vector<int>& nums, int value) {
    unordered_map<int, int> count;

    for (const int num : nums)
      ++count[(num % value + value) % value];

    for (int i = 0; i < nums.size(); ++i)
      if (--count[i % value] < 0)
        return i;

    return nums.size();
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [1,-10,7,13,6,8], value = 5
```
### Steps
```
Remainders: 1%5=1, (-10%5+5)%5=0, 7%5=2, 13%5=3, 6%5=1, 8%5=3
count = {0:1, 1:2, 2:1, 3:2}

i=0: i%5=0, count[0]=1->0, ok
i=1: i%5=1, count[1]=2->1, ok
i=2: i%5=2, count[2]=1->0, ok
i=3: i%5=3, count[3]=2->1, ok
i=4: i%5=4, count[4]=0->-1 < 0, return 4

Answer: 4
```

---

## ⏱️ Time Complexity
```
O(n)
```

## 💾 Space Complexity
```
O(value) for the hash map, but at most O(n) entries
```

---

## ⚠️ Edge Cases
- All elements are the same — depends on how many share the same remainder
- Negative numbers — handled by `(num % value + value) % value`
- `value = 1` — every number can become any non-negative integer, so MEX = n

---

## 🎯 Interview Takeaways
- Adding/subtracting a fixed value preserves the modular residue — this is the key insight.
- The MEX is determined by which residue class runs out of "coverage" first.

---

## 📌 Key Pattern
👉 **"Modular arithmetic to group elements by equivalence class"**

---

## 🔁 Related Problems
- 41. First Missing Positive
- 268. Missing Number
- 2003. Smallest Missing Genetic Value in Each Subtree

---

## 🚀 Final Thoughts
The key insight is that repeated addition/subtraction of `value` only lets a number traverse its residue class mod `value`. Once you see this, the problem reduces to counting residues and finding the first gap.

---

✨ **Rule to remember:**
> Adding/subtracting a constant preserves the modular residue — group by remainder to find the MEX.
