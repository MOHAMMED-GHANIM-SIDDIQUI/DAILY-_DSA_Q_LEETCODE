# 2161. Partition Array According to Given Pivot

## 🔗 Problem Link
https://leetcode.com/problems/partition-array-according-to-given-pivot/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Two Pointers

---

## 🧩 Problem Summary
Given an array `nums` and an integer `pivot`, rearrange the array so that all elements less than `pivot` come first, then all elements equal to `pivot`, then all elements greater than `pivot`. The relative order of elements within each group must be preserved.

### 📌 Constraints
- `1 <= nums.length <= 10^5`
- `-10^6 <= nums[i] <= 10^6`
- `pivot` equals an element of `nums`

---

## 💭 Intuition
👉 Three-pass approach: collect elements less than pivot, equal to pivot, and greater than pivot separately, preserving order.

---

## ⚡ Approach — Three-Pass Collection

### 🧠 Idea
- Pass 1: collect all elements < pivot.
- Pass 2: collect all elements == pivot.
- Pass 3: collect all elements > pivot.
- Concatenate the three groups into the result.

---

## 💻 Code

```cpp
class Solution {
public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        vector<int>ans;
        int n=nums.size();
        for(int i=0;i<n;i++)
        {
            if(nums[i]<pivot)
            ans.push_back(nums[i]);
        }
        for(int i=0;i<n;i++)
        {
            if(nums[i]==pivot)
            ans.push_back(nums[i]);
        }
        for(int i=0;i<n;i++)
        {
            if(nums[i]>pivot)
            ans.push_back(nums[i]);
        }
        return ans;

    }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [9, 12, 5, 10, 14, 3, 10], pivot = 10
```
### Steps
```
Pass 1 (< 10): [9, 5, 3]
Pass 2 (== 10): [10, 10]
Pass 3 (> 10): [12, 14]
Result: [9, 5, 3, 10, 10, 12, 14]
```

---

## ⏱️ Time Complexity
```
O(n) — three linear passes through the array
```

## 💾 Space Complexity
```
O(n) — for the result array
```

---

## ⚠️ Edge Cases
- All elements equal to pivot → result is the same array
- No elements equal to pivot → only two groups
- Single element array

---

## 🎯 Interview Takeaways
- This is a stable partition problem — relative order must be preserved.
- Three-pass is simple and clean; avoids complex in-place swapping.
- Similar to the Dutch National Flag problem but requires stability.

---

## 📌 Key Pattern
👉 **"Three-bucket stable partition around a pivot"**

---

## 🔁 Related Problems
- 75. Sort Colors (Dutch National Flag)
- 905. Sort Array By Parity
- 922. Sort Array By Parity II

---

## 🚀 Final Thoughts
The three-pass approach is the cleanest way to achieve a stable partition. It trades a little extra space for simplicity and correctness in preserving relative order.

---

✨ **Rule to remember:**
> "For stable partition around a pivot, collect into three buckets: less, equal, greater."
