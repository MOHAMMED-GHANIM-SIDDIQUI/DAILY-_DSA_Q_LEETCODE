# 1534. Count Good Triplets

## 🔗 Problem Link
https://leetcode.com/problems/count-good-triplets/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Enumeration

---

## 🧩 Problem Summary
Given an array of integers `arr` and three integers `a`, `b`, and `c`, count the number of good triplets. A triplet `(arr[i], arr[j], arr[k])` is good if `i < j < k` and `|arr[i] - arr[j]| <= a`, `|arr[j] - arr[k]| <= b`, and `|arr[i] - arr[k]| <= c`.

### 📌 Constraints
- `3 <= arr.length <= 100`
- `0 <= arr[i] <= 1000`
- `0 <= a, b, c <= 1000`

---

## 💭 Intuition
👉 With `n <= 100`, a brute-force O(n^3) triple nested loop is perfectly fine. Simply check all triplets and count the ones satisfying all three conditions.

---

## ⚡ Approach — Brute Force Triple Loop

### 🧠 Idea
- Iterate over all triples `(i, j, k)` with `i < j < k`.
- Check all three absolute difference conditions.
- Increment counter if all conditions are met.

---

## 💻 Code

```cpp
class Solution {
public:
    int countGoodTriplets(vector<int>& arr, int a, int b, int c) {
        int ans = 0;
        int n = arr.size();

        for (int i = 0; i < n - 2; ++i) {
            for (int j = i + 1; j < n - 1; ++j) {
                for (int k = j + 1; k < n; ++k) {
                    if (abs(arr[i] - arr[j]) <= a &&
                        abs(arr[j] - arr[k]) <= b &&
                        abs(arr[i] - arr[k]) <= c) {
                        ++ans;
                    }
                }
            }
        }
        return ans;
    }
};
```

---

## 🧠 Dry Run
### Input
```
arr = [3, 0, 1, 1, 9, 7], a = 7, b = 2, c = 3
```
### Steps
```
(i=0,j=1,k=2): |3-0|=3<=7, |0-1|=1<=2, |3-1|=2<=3 → good, ans=1
(i=0,j=1,k=3): |3-0|=3<=7, |0-1|=1<=2, |3-1|=2<=3 → good, ans=2
(i=0,j=1,k=4): |3-0|=3<=7, |0-9|=9>2 → skip
(i=0,j=2,k=3): |3-1|=2<=7, |1-1|=0<=2, |3-1|=2<=3 → good, ans=3
...
(i=2,j=3,k=5): |1-1|=0<=7, |1-7|=6>2 → skip
Final answer: 4
```

---

## ⏱️ Time Complexity
```
O(n^3), where n is the length of arr
```

## 💾 Space Complexity
```
O(1)
```

---

## ⚠️ Edge Cases
- `n = 3` — only one triplet to check.
- `a = b = c = 0` — only triplets where all three elements are equal.
- `a = b = c = 1000` — all triplets are good (since `arr[i] <= 1000`).

---

## 🎯 Interview Takeaways
- When constraints are small (n <= 100), brute force is the right approach.
- Always check constraints first before optimizing.
- An optimization: check `|arr[i] - arr[j]| <= a` first and skip the inner loop early.

---

## 📌 Key Pattern
👉 **"Brute force enumeration with small constraints — O(n^3) is acceptable when n <= 100"**

---

## 🔁 Related Problems
- 15 — 3Sum
- 611 — Valid Triangle Number
- 1995 — Count Special Quadruplets

---

## 🚀 Final Thoughts
This is a straightforward brute-force problem where the small constraint (n <= 100) makes O(n^3) perfectly acceptable. The key takeaway is to always check constraints before spending time on optimization.

---

✨ **Rule to remember:**
> "When n <= 100, an O(n^3) brute force with condition checks is the simplest and most correct approach."
