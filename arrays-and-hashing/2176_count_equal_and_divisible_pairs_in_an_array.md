# 2176. Count Equal and Divisible Pairs in an Array

## 🔗 Problem Link
https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Brute Force

---

## 🧩 Problem Summary
Given an array `nums` and an integer `k`, count the number of pairs `(i, j)` where `i < j`, `nums[i] == nums[j]`, and `(i * j) % k == 0`.

### 📌 Constraints
- `1 <= nums.length <= 100`
- `1 <= nums[i], k <= 100`

---

## 💭 Intuition
👉 With small constraints (n <= 100), a brute-force O(n^2) approach checking all pairs is efficient enough.

---

## ⚡ Approach — Brute Force All Pairs

### 🧠 Idea
- Iterate over all pairs `(i, j)` with `i < j`.
- Check if `nums[i] == nums[j]` and `(i * j) % k == 0`.
- Count valid pairs.

---

## 💻 Code

```cpp
class Solution {
public:
    int countPairs(vector<int>& nums, int k) {
        int n=nums.size();
        int ans=0;
        for(int i=0;i<n;i++)
        {
            for(int j=i+1;j<n;j++)
            {
                if(nums[i]==nums[j] && (i*j)%k==0)
                ans++;
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
nums = [3, 1, 2, 2, 2, 1, 3], k = 2
```
### Steps
```
(0,6): nums[0]==nums[6]=3, 0*6=0, 0%2=0 ✓ → ans=1
(1,5): nums[1]==nums[5]=1, 1*5=5, 5%2=1 ✗
(2,3): nums[2]==nums[3]=2, 2*3=6, 6%2=0 ✓ → ans=2
(2,4): nums[2]==nums[4]=2, 2*4=8, 8%2=0 ✓ → ans=3
(3,4): nums[3]==nums[4]=2, 3*4=12, 12%2=0 ✓ → ans=4
Result: 4
```

---

## ⏱️ Time Complexity
```
O(n^2) — checking all pairs
```

## 💾 Space Complexity
```
O(1) — no extra data structures
```

---

## ⚠️ Edge Cases
- All elements are distinct → 0 pairs
- k = 1 → divisibility always holds, just count equal pairs
- All elements are the same → check divisibility for every pair

---

## 🎯 Interview Takeaways
- Always check constraints first — brute force is acceptable for n <= 100.
- The divisibility condition on indices (not values) is the twist here.
- For larger n, grouping by value and checking index pairs within groups would optimize.

---

## 📌 Key Pattern
👉 **"Brute-force pair enumeration with dual conditions"**

---

## 🔁 Related Problems
- 1. Two Sum
- 2154. Keep Multiplying Found Values by Two
- 2006. Count Number of Pairs With Absolute Difference K

---

## 🚀 Final Thoughts
A straightforward brute-force problem. The key is reading the conditions carefully — equality of values AND divisibility of the product of indices.

---

✨ **Rule to remember:**
> "When n <= 100, brute-force all pairs confidently — O(n^2) is only 10,000 operations."
