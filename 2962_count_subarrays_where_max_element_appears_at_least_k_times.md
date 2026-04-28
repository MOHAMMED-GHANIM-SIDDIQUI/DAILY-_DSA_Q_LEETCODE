# 2962. Count Subarrays Where Max Element Appears at Least K Times

## 🔗 Problem Link
https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Sliding Window

---

## 🧩 Problem Summary
Given an integer array `nums` and a positive integer `k`, count the number of subarrays where the maximum element of the entire array appears at least `k` times.

### 📌 Constraints
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^6
- 1 <= k <= 10^5

---

## 💭 Intuition
👉 Find the global maximum first. Then use a sliding window: once the window contains at least `k` occurrences of the max element, every extension to the right is also valid. Count all valid subarrays by adding `(n - right)` when shrinking from the left.

---

## ⚡ Approach — Sliding Window

### 🧠 Idea
- Find the global maximum of the array.
- Use two pointers (`left`, `right`). Expand `right` and count occurrences of `maxNum`.
- When count >= k, all subarrays starting at `left` and ending at `right` or beyond are valid — add `(n - right)`.
- Shrink from `left` and repeat.

---

## 💻 Code

```cpp
class Solution {
public:
    long long countSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        int maxNum = *max_element(nums.begin(), nums.end());
        long long ans = 0;
        int count = 0; // count of maxNum in current window
        int left = 0;

        for (int right = 0; right < n; ++right) {
            if (nums[right] == maxNum) {
                count++;
            }

            while (count >= k) {
                // when we have at least k maxNum in window
                ans += (n - right); // all subarrays from left to beyond right are valid
                if (nums[left] == maxNum) {
                    count--;
                }
                left++;
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
nums = [1, 3, 2, 3, 3], k = 2
```
### Steps
```
maxNum = 3, n = 5

right=0: nums[0]=1, count=0
right=1: nums[1]=3, count=1
right=2: nums[2]=2, count=1
right=3: nums[3]=3, count=2 >= 2
  ans += (5-3) = 2, nums[0]=1, left=1, count=2
  ans += (5-3) = 4, nums[1]=3, left=2, count=1
right=4: nums[4]=3, count=2 >= 2
  ans += (5-4) = 5, nums[2]=2, left=3, count=2
  ans += (5-4) = 6, nums[3]=3, left=4, count=1

Output: 6
```

---

## ⏱️ Time Complexity
```
O(n) — each element is visited at most twice (once by right, once by left)
```

## 💾 Space Complexity
```
O(1) — constant extra space
```

---

## ⚠️ Edge Cases
- `k = 1`: Every subarray containing the max element counts.
- Max element appears fewer than `k` times total: answer is 0.
- All elements are the same: many valid subarrays.

---

## 🎯 Interview Takeaways
- Sliding window with "at least k" counting uses the trick of adding `(n - right)` valid extensions.
- Finding the global max first simplifies the window condition.
- The two-pointer approach ensures each element is processed at most twice.

---

## 📌 Key Pattern
👉 **"Sliding window for 'at least k' subarray counting — add (n - right) valid extensions"**

---

## 🔁 Related Problems
- 992. Subarrays with K Different Integers
- 1248. Count Number of Nice Subarrays
- 2444. Count Subarrays With Fixed Bounds

---

## 🚀 Final Thoughts
The key trick is converting "at least k occurrences" into a sliding window problem. When the window satisfies the condition, all rightward extensions are also valid, giving us `(n - right)` additional subarrays per left pointer position.

---

✨ **Rule to remember:**
> For "at least k" subarray problems, once the window is valid, count all extensions to the right as (n - right).
