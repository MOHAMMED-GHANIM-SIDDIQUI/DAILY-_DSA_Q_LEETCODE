# 3396. Minimum Number of Operations to Make Elements in Array Distinct

## 🔗 Problem Link
https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Hash Table, Greedy

---

## 🧩 Problem Summary
Given an array of integers, you can remove the first 3 elements in one operation. Find the minimum number of operations needed so that all remaining elements are distinct. If the array is already distinct, return 0.

### 📌 Constraints
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100

---

## 💭 Intuition
👉 Scan from the end to find the rightmost duplicate. All elements up to and including that index must be removed. Since each operation removes 3 elements from the front, the answer is ceil((index + 1) / 3).

---

## ⚡ Approach — Reverse Scan with Set

### 🧠 Idea
- Traverse the array from right to left, adding elements to a set.
- When a duplicate is found at index i, we need to remove elements [0..i].
- Number of operations = ceil((i + 1) / 3).
- If no duplicate is found, return 0.

---

## 💻 Code

```cpp
class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        unordered_set<int> seen;
        for (int i = nums.size() - 1; i >= 0; --i) {
            if (seen.count(nums[i])) {
                return (i + 1 + 2) / 3;  // Equivalent to ceil((i + 1) / 3)
            }
            seen.insert(nums[i]);
        }
        return 0;
    }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [1, 2, 3, 4, 2, 3, 3, 5, 7]
```
### Steps
```
Scan from right:
i=8: 7 → seen={7}
i=7: 5 → seen={7,5}
i=6: 3 → seen={7,5,3}
i=5: 3 → duplicate found! return ceil(6/3) = 2

Result: 2 (remove [1,2,3] then [4,2,3], leaving [3,5,7])
```

---

## ⏱️ Time Complexity
```
O(n) — single reverse pass
```

## 💾 Space Complexity
```
O(n) — for the hash set
```

---

## ⚠️ Edge Cases
- Already all distinct → return 0
- All elements are the same → need to remove until at most 1 remains
- Array length <= 3 and has duplicates → 1 operation

---

## 🎯 Interview Takeaways
- Scanning from the end helps find the "minimum prefix to remove."
- Integer ceiling division: ceil(a/b) = (a + b - 1) / b.
- Greedy: removing from the front in chunks of 3.

---

## 📌 Key Pattern
👉 **"Reverse scan to find first (rightmost) conflict, then compute prefix removal"**

---

## 🔁 Related Problems
- 1Remove Duplicates from Sorted Array
- 2357. Make Array Zero by Subtracting Equal Amounts

---

## 🚀 Final Thoughts
The reverse-scan approach is elegant: by scanning from right to left, we identify the exact prefix that must be removed. The ceiling division gives the number of 3-element removal operations needed.

---

✨ **Rule to remember:**
> Scan from the end to find the rightmost duplicate — everything before it must be removed in chunks of 3.
