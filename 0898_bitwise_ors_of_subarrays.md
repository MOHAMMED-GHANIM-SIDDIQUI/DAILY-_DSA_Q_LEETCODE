# 898. Bitwise ORs of Subarrays

## 🔗 Problem Link
https://leetcode.com/problems/bitwise-ors-of-subarrays/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Dynamic Programming, Bit Manipulation, Array

---

## 🧩 Problem Summary
Given an integer array `arr`, return the number of distinct bitwise OR results of all non-empty subarrays. For each subarray `arr[i..j]`, compute `arr[i] | arr[i+1] | ... | arr[j]` and count the unique values.

### 📌 Constraints
- `1 <= arr.length <= 5 * 10^4`
- `0 <= arr[i] <= 10^9`

---

## 💭 Intuition
👉 For each new element, the set of OR values ending at that position is formed by OR-ing the element with all distinct OR values ending at the previous position. Since OR can only add bits, the number of distinct values per position is bounded by the number of bits (~30).

---

## ⚡ Approach — Iterative OR Set Propagation

### 🧠 Idea
- Maintain a running list of distinct OR values from previous subarrays.
- For each new element `a`, compute new OR values by combining `a` with all previous values.
- Deduplicate by only keeping values that produce new results.
- Collect all values into a set for the final count.

---

## 💻 Code

```cpp
class Solution {
 public:
  int subarrayBitwiseORs(vector<int>& arr) {
    vector<int> s;
    int l = 0;

    for (const int a : arr) {
      const int r = s.size();
      s.push_back(a);
      // s[l..r) are values generated in the previous iteration
      for (int i = l; i < r; ++i)
        if (s.back() != (s[i] | a))
          s.push_back(s[i] | a);
      l = r;
    }

    return unordered_set<int>(s.begin(), s.end()).size();
  }
};
```

---

## 🧠 Dry Run
### Input
```
arr = [1, 2, 4]
```
### Steps
```
a=1: s=[1], l=0
a=2: s=[1, 2, 1|2=3], l=1
a=4: s=[1, 2, 3, 4, 2|4=6, 3|4=7], l=3

Distinct values: {1, 2, 3, 4, 6, 7} -> size = 6
```

---

## ⏱️ Time Complexity
```
O(n * 30) = O(n * log(max_val)), since at most 30 distinct OR values per position
```

## 💾 Space Complexity
```
O(n * 30) for all collected OR values
```

---

## ⚠️ Edge Cases
- Single element array: return 1.
- All elements are the same: OR of any subarray is the same value, return 1.
- All zeros: return 1.

---

## 🎯 Interview Takeaways
- OR is monotonically non-decreasing as subarrays grow, limiting distinct values.
- The key insight is that the number of distinct OR values ending at any position is O(log(max_val)).
- This avoids brute-force O(n^2) enumeration.

---

## 📌 Key Pattern
👉 **"Propagate a bounded set of OR values per position, leveraging the monotonic bit-setting property of OR"**

---

## 🔁 Related Problems
- 201. Bitwise AND of Numbers Range
- 1521. Find a Value of a Mysterious Function Closest to Target

---

## 🚀 Final Thoughts
This problem exploits a fundamental property of bitwise OR: once a bit is set, it stays set. This means the number of distinct OR values ending at each position is limited to at most 30 (number of bits), making the approach efficient despite seeming quadratic at first glance.

---

✨ **Rule to remember:**
> "Bitwise OR can only add bits, so distinct OR values ending at any index are bounded by O(log(max_val))."
