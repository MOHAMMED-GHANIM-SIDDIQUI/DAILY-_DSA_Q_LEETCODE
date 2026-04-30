# 2799. Count Complete Subarrays in an Array

## 🔗 Problem Link
https://leetcode.com/problems/count-complete-subarrays-in-an-array/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Hash Table, Sliding Window

---

## 🧩 Problem Summary
Given an array of positive integers `nums`, a subarray is called complete if the number of distinct elements in the subarray equals the number of distinct elements in the entire array. Return the number of complete subarrays.

### 📌 Constraints
- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 2000`

---

## 💭 Intuition
👉 Use a sliding window to find the smallest valid window ending at each right pointer. Once the window contains all distinct elements, every extension of the left boundary to the left also forms a valid subarray. Count these using the left pointer position.

---

## ⚡ Approach — Sliding Window

### 🧠 Idea
- Count `totalDistinct` = number of distinct elements in the entire array.
- Use a sliding window `[l, r]` with a frequency array.
- Expand right, adding elements. When `distinct == totalDistinct`, shrink from the left.
- After shrinking, all subarrays `nums[0..r], nums[1..r], ..., nums[l-1..r]` are complete, so add `l` to the answer.

---

## 💻 Code

```cpp
class Solution {
 public:
  int countCompleteSubarrays(vector<int>& nums) {
    constexpr int kMax = 2000;
    const int totalDistinct =
        unordered_set<int>(nums.begin(), nums.end()).size();
    int ans = 0;
    int distinct = 0;
    vector<int> count(kMax + 1);

    int l = 0;
    for (const int num : nums) {
      if (++count[num] == 1)
        ++distinct;
      while (distinct == totalDistinct)
        if (--count[nums[l++]] == 0)
          --distinct;
      // Assume nums[r] = num,
      // nums[0..r], nums[1..r], ..., nums[l - 1..r] have k different values.
      ans += l;
    }

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [1,3,1,2,2]
```
### Steps
```
totalDistinct = 3 (elements: 1, 2, 3)

r=0 (num=1): count[1]=1, distinct=1. ans+=0
r=1 (num=3): count[3]=1, distinct=2. ans+=0
r=2 (num=1): count[1]=2, distinct=2. ans+=0
r=3 (num=2): count[2]=1, distinct=3 == totalDistinct!
  shrink: count[nums[0]]=count[1]=2->1, l=1, distinct still 3
  shrink: count[nums[1]]=count[3]=1->0, l=2, distinct=2, stop
  ans += 2 => ans=2
r=4 (num=2): count[2]=2, distinct=2. ans+=2 => ans=4

Answer: 4
```

---

## ⏱️ Time Complexity
```
O(n)
```

## 💾 Space Complexity
```
O(n) for the frequency array and set
```

---

## ⚠️ Edge Cases
- All elements are the same — every subarray is complete, answer is `n*(n+1)/2`
- All elements are distinct — only subarray of length `n` is complete, plus any that contain all elements
- Array of length 1

---

## 🎯 Interview Takeaways
- The "shrink left, add left index" pattern counts all valid subarrays ending at the current right pointer.
- This is the same pattern as counting subarrays with k distinct elements.

---

## 📌 Key Pattern
👉 **"Sliding window — shrink to find boundary, count valid subarrays via left pointer"**

---

## 🔁 Related Problems
- 992. Subarrays with K Different Integers
- 2537. Count the Number of Good Subarrays
- 1248. Count Number of Nice Subarrays

---

## 🚀 Final Thoughts
A classic sliding window problem. The key technique is: after shrinking the window until it no longer satisfies the condition, the number of valid starting points is exactly `l`, because all positions `[0, l-1]` as left endpoints with the current right endpoint form valid subarrays.

---

✨ **Rule to remember:**
> To count subarrays satisfying a condition, use a sliding window: shrink left until invalid, then all positions before `l` are valid starting points.
