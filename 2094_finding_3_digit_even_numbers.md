# 2094. Finding 3-Digit Even Numbers

## 🔗 Problem Link
https://leetcode.com/problems/finding-3-digit-even-numbers/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Hash Table, Sorting, Enumeration

---

## 🧩 Problem Summary
Given an integer array `digits`, find all unique 3-digit even numbers that can be formed using elements from the array (each element used at most once per number). Return the sorted result in increasing order.

### 📌 Constraints
- `3 <= digits.length <= 100`
- `0 <= digits[i] <= 9`

---

## 💭 Intuition
👉 Instead of generating all permutations of 3 digits, enumerate all valid 3-digit even numbers (100 to 998) and check if they can be formed using the available digits.

---

## ⚡ Approach — Enumerate All Valid Numbers

### 🧠 Idea
- Count the frequency of each digit in the input.
- Iterate over all 3-digit combinations `abc` where `a` is 1-9, `b` is 0-9, `c` is 0,2,4,6,8.
- Check if the required digits are available (accounting for duplicates like `a == b`).
- This naturally produces results in sorted order.

---

## 💻 Code

```cpp
class Solution {
 public:
  vector<int> findEvenNumbers(vector<int>& digits) {
    vector<int> ans;
    vector<int> count(10);

    for (const int digit : digits)
      ++count[digit];

    // Try to construct `abc`.
    for (int a = 1; a <= 9; ++a)
      for (int b = 0; b <= 9; ++b)
        for (int c = 0; c <= 8; c += 2)
          if (count[a] > 0 && count[b] > (b == a) &&
              count[c] > (c == a) + (c == b))
            ans.push_back(a * 100 + b * 10 + c);

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
digits = [2, 1, 3, 0]
```
### Steps
```
count = [1,1,1,1,0,0,0,0,0,0]  (digits 0,1,2,3 each appear once)
a=1, b=0, c=2: count[1]>0, count[0]>(0==1)=0, count[2]>(2==1)+(2==0)=0 -> 102 added
a=1, b=2, c=0: count[1]>0, count[2]>(2==1)=0, count[0]>(0==1)+(0==2)=0 -> 120 added
a=1, b=3, c=0: -> 130 added
a=1, b=3, c=2: -> 132 added
a=2, b=0, c=0: count[0]>(0==2)+(0==0) = count[0]>1 = 1>1? No -> skip (only one 0)
a=2, b=1, c=0: -> 210 added
...
Result: [102, 120, 130, 132, 210, 230, 302, 310, 312, 320]
```

---

## ⏱️ Time Complexity
```
O(1) -- at most 9 * 10 * 5 = 450 iterations, independent of input size
```

## 💾 Space Complexity
```
O(1) for the count array (size 10)
```

---

## ⚠️ Edge Cases
- All digits are 0: no valid 3-digit number
- All digits are odd: no even number possible
- Duplicate digits: frequency counting handles correctly
- Single digit repeated many times, e.g., [2,2,2]: 222 is valid

---

## 🎯 Interview Takeaways
- Enumerating the answer space (450 numbers) is simpler and faster than generating permutations.
- The condition `count[b] > (b == a)` elegantly handles duplicate digit usage.
- Results are automatically sorted by the enumeration order.

---

## 📌 Key Pattern
👉 **"Enumerate answer candidates and validate against available resources"**

---

## 🔁 Related Problems
- 47. Permutations II
- 1323. Maximum 69 Number
- 949. Largest Time for Given Digits

---

## 🚀 Final Thoughts
This problem showcases how reversing the approach -- enumerating answers instead of input permutations -- can lead to cleaner and more efficient solutions. The frequency-based validation is both elegant and correct.

---

✨ **Rule to remember:**
> When the answer space is smaller than the permutation space, enumerate answers and validate.
