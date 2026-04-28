# 2154. Keep Multiplying Found Values by Two

## 🔗 Problem Link
https://leetcode.com/problems/keep-multiplying-found-values-by-two/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Sorting, Binary Search, Hash Table

---

## 🧩 Problem Summary
Given an array of integers `nums` and an integer `original`, repeatedly double `original` if it is found in `nums`. Return the final value of `original` when it is no longer found in the array.

### 📌 Constraints
- `1 <= nums.length <= 1000`
- `1 <= nums[i], original <= 1000`

---

## 💭 Intuition
👉 Sort the array and use binary search to check if the current value exists; if yes, double it and repeat.

---

## ⚡ Approach — Sort + Binary Search

### 🧠 Idea
- Sort `nums` so binary search can be used.
- While the current value is found via binary search, multiply it by 2.
- Return the value once it is no longer present.

---

## 💻 Code

```cpp
class Solution {
    bool is_present(vector<int> nums, int x )
    {
        int beg=0,end=nums.size()-1;
        while(beg<=end)
        {
            int mid=beg+(end-beg)/2;
            if (nums[mid]==x)
                return true;
            else if (nums[mid]>x)
            end=mid-1;
            else
            beg=mid+1;
        }
        return false;
    }
public:
    int findFinalValue(vector<int>& nums, int original) {
        sort(nums.begin(),nums.end());
        int ans=original;
        while(is_present(nums,ans))
        {
            ans*=2;
        }
        return ans;


    }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [5, 3, 6, 1, 12], original = 3
```
### Steps
```
Sorted nums = [1, 3, 5, 6, 12]
ans = 3 → found → ans = 6
ans = 6 → found → ans = 12
ans = 12 → found → ans = 24
ans = 24 → not found → return 24
```

---

## ⏱️ Time Complexity
```
O(n log n) — sorting dominates; each binary search is O(log n)
```

## 💾 Space Complexity
```
O(1) — in-place sort, no extra data structures
```

---

## ⚠️ Edge Cases
- `original` not in `nums` at all → return `original` immediately
- All elements are the same as `original` → double once
- Value doubles beyond any element in `nums`

---

## 🎯 Interview Takeaways
- A HashSet approach would give O(1) lookups and O(n) overall — simpler alternative.
- Binary search is a valid approach when array is sorted.
- The doubling loop runs at most O(log(max)) times.

---

## 📌 Key Pattern
👉 **"Repeated lookup and transform until condition fails"**

---

## 🔁 Related Problems
- 217. Contains Duplicate
- 1. Two Sum
- 2206. Divide Array Into Equal Pairs

---

## 🚀 Final Thoughts
A straightforward simulation problem. The key decision is how to perform the lookup efficiently — hash set is optimal but binary search on a sorted array works well too.

---

✨ **Rule to remember:**
> "Sort and binary search for repeated membership checks, or use a hash set for O(1) lookups."
