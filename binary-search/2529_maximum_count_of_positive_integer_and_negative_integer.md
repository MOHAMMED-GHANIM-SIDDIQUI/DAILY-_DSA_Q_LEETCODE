# 2529. Maximum Count of Positive Integer and Negative Integer

## 🔗 Problem Link
https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Binary Search, Counting

---

## 🧩 Problem Summary
Given a sorted array `nums`, return the maximum between the count of positive integers and the count of negative integers. Zero is neither positive nor negative.

### 📌 Constraints
- `1 <= nums.length <= 2000`
- `-2000 <= nums[i] <= 2000`
- `nums` is sorted in non-decreasing order.

---

## 💭 Intuition
👉 Simply count positives and negatives in one pass and return the larger count. The sorted property could enable binary search, but linear scan is sufficient given the constraints.

---

## ⚡ Approach — Linear Scan

### 🧠 Idea
- Iterate through the array, count elements > 0 as positive and elements < 0 as negative.
- Return `max(pos, neg)`.

---

## 💻 Code

```cpp
class Solution {
public:
    int maximumCount(vector<int>& nums) {
        int pos=0,neg=0;
        for(int i:nums)
        {
            if(i>0)
            pos++;
            else if(i<0)
            neg++;
        }
        return pos>neg?pos:neg;

    }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [-2,-1,-1,1,2,3]
```
### Steps
```
i=-2: neg=1
i=-1: neg=2
i=-1: neg=3
i=1:  pos=1
i=2:  pos=2
i=3:  pos=3

max(3, 3) = 3
Result: 3
```

---

## ⏱️ Time Complexity
```
O(n) — single pass through the array.
```

## 💾 Space Complexity
```
O(1) — two counter variables.
```

---

## ⚠️ Edge Cases
- All zeros: both counts are 0, answer is 0.
- All positive or all negative.
- Array with only zeros and one positive/negative.

---

## 🎯 Interview Takeaways
- For sorted arrays, binary search can find boundaries in O(log n), but O(n) is fine for small constraints.
- The ternary operator provides a concise max without `std::max`.
- Zero is explicitly excluded from both counts.

---

## 📌 Key Pattern
👉 **"Count and compare — straightforward when the question is about frequency."**

---

## 🔁 Related Problems
- 2089. Find Target Indices After Sorting an Array
- 34. Find First and Last Position of Element in Sorted Array
- 704. Binary Search

---

## 🚀 Final Thoughts
A simple counting problem. For an optimized O(log n) solution, use `lower_bound(0)` for the number of negatives and `upper_bound(0)` for the start of positives. But the linear approach is clean and perfectly adequate.

---

✨ **Rule to remember:**
> "Count positives and negatives separately — zeros belong to neither."
