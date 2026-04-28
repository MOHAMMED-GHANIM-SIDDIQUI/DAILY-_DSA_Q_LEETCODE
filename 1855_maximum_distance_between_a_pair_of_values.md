# 1855. Maximum Distance Between a Pair of Values

## 🔗 Problem Link
https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Two Pointers, Greedy

---

## 🧩 Problem Summary
Given two non-increasing arrays `nums1` and `nums2`, find the maximum distance `j - i` such that `i <= j` and `nums1[i] <= nums2[j]`. Return 0 if no valid pair exists.

### 📌 Constraints
- `1 <= nums1.length, nums2.length <= 10^5`
- `1 <= nums1[i], nums2[j] <= 10^5`
- Both arrays are non-increasing

---

## 💭 Intuition
👉 Since both arrays are sorted in non-increasing order, we can use two pointers. For each position in `nums1`, we try to extend `j` as far right as possible in `nums2` while the condition `nums1[i] <= nums2[j]` holds.

---

## ⚡ Approach — Two Pointers

### 🧠 Idea
- Initialize pointers `i = 0` and `j = 0`.
- If `nums1[i] <= nums2[j]`, record the distance `j - i` and advance `j` to try a larger distance.
- If `nums1[i] > nums2[j]`, advance `i` to find a smaller value in `nums1`.
- An early exit is added: if the smallest element in `nums1` is greater than the largest in `nums2`, return 0.

---

## 💻 Code

```python
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        # nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]
        #           i                          j
        ans = 0
        if nums1[-1]>nums2[0]:
            return 0
        i , j =0 , 0
        while i < n and j < m:
          if nums1[i] <= nums2[j]:
            ans = max(ans, j-i)
            j+=1
          else:
            i+=1
        return ans
```

---

## 🧠 Dry Run
### Input
```
nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]
```
### Steps
```
i=0, j=0: 55 <= 100 → ans=0, j=1
i=0, j=1: 55 > 20  → i=1
i=1, j=1: 30 > 20  → i=2
i=2, j=1: 5 <= 20  → ans=0 (j-i=-1? no, j<i skip), actually j-i = 1-2 = -1 → max(0,-1)=0, j=2
i=2, j=2: 5 <= 10  → ans=max(0,0)=0, j=3
i=2, j=3: 5 <= 10  → ans=max(0,1)=1, j=4
i=2, j=4: 5 <= 5   → ans=max(1,2)=2, j=5
j=5 out of bounds → return 2
```

---

## ⏱️ Time Complexity
```
O(n + m), where n and m are the lengths of nums1 and nums2
```

## 💾 Space Complexity
```
O(1)
```

---

## ⚠️ Edge Cases
- No valid pair exists → return 0
- One of the arrays has length 1
- All elements in nums1 are greater than all elements in nums2

---

## 🎯 Interview Takeaways
- Two pointers on sorted arrays is a classic technique for finding optimal pairs in linear time.
- The non-increasing sort order allows advancing pointers without missing valid pairs.

---

## 📌 Key Pattern
👉 **"Two pointers on sorted arrays to find optimal pair distance"**

---

## 🔁 Related Problems
- 167. Two Sum II - Input Array Is Sorted
- 826. Most Profit Assigning Work
- 392. Is Subsequence

---

## 🚀 Final Thoughts
The two-pointer approach leverages the sorted nature of both arrays to achieve linear time. The key insight is that advancing `i` when the condition fails is safe because `nums1` is non-increasing — moving `i` forward can only make the value smaller (or equal), which helps satisfy the condition.

---

✨ **Rule to remember:**
> On two non-increasing arrays, advance `j` when the pair is valid, advance `i` when it is not.
