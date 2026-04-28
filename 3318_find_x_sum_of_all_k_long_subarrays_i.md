# 3318. Find X-Sum of All K-Long Subarrays I

## 🔗 Problem Link
https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Hash Table, Sliding Window, Heap (Priority Queue), Ordered Set

---

## 🧩 Problem Summary
Given an array `nums` and integers `k` and `x`, compute the x-sum of every contiguous subarray of length `k`. The x-sum is the sum of the top `x` most frequent elements (ties broken by value). If the subarray has fewer than `x` distinct elements, sum all elements.

### 📌 Constraints
- `1 <= nums.length <= 50`
- `1 <= x <= k <= nums.length`
- `1 <= nums[i] <= 50`

---

## 💭 Intuition
👉 Maintain a sliding window with two ordered sets: `top` (the x most frequent/valuable elements) and `bot` (the rest). As the window slides, update counts and rebalance between top and bot.

---

## ⚡ Approach — Two Multisets with Sliding Window

### 🧠 Idea
- Use a `top` multiset for the x highest (count, value) pairs, and `bot` for the rest.
- On each window slide, update the frequency count and move elements between sets as needed.
- Track `windowSum` as the sum of `value * count` for elements in `top`.

---

## 💻 Code

```cpp
class Solution {
 public:
  vector<int> findXSum(vector<int>& nums, int k, int x) {
    vector<int> ans;
    long windowSum = 0;
    unordered_map<int, int> count;
    multiset<pair<int, int>> top;  // the top x elements
    multiset<pair<int, int>> bot;  // the rest of the elements

    // Updates the count of num by freq and the window sum accordingly.
    auto update = [&count, &top, &bot, &windowSum](int num, int freq) -> void {
      if (count[num] > 0) {  // Clean up the old count.
        if (auto it = bot.find({count[num], num}); it != bot.end()) {
          bot.erase(it);
        } else {
          it = top.find({count[num], num});
          top.erase(it);
          windowSum -= num * count[num];
        }
      }
      count[num] += freq;
      if (count[num] > 0)
        bot.insert({count[num], num});
    };

    for (int i = 0; i < nums.size(); ++i) {
      update(nums[i], 1);
      if (i >= k)
        update(nums[i - k], -1);
      // Move the bottom elements to the top if needed.
      while (!bot.empty() && top.size() < x) {
        const auto [countB, b] = *bot.rbegin();
        bot.erase(--bot.end());
        top.insert({countB, b});
        windowSum += b * countB;
      }
      // Swap the bottom and top elements if needed.
      while (!bot.empty() && *bot.rbegin() > *top.begin()) {
        const auto [countB, b] = *bot.rbegin();
        const auto [countT, t] = *top.begin();
        bot.erase(--bot.end());
        top.erase(top.begin());
        bot.insert({countT, t});
        top.insert({countB, b});
        windowSum += b * countB;
        windowSum -= t * countT;
      }
      if (i >= k - 1)
        ans.push_back(windowSum);
    }

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [1, 1, 2, 2, 3, 4, 2, 3], k = 6, x = 2
```
### Steps
```
Window [1,1,2,2,3,4]: counts {1:2, 2:2, 3:1, 4:1}
  top = {(2,2), (2,1)} → windowSum = 2*2 + 1*2 = 6
Window [1,2,2,3,4,2]: counts {1:1, 2:3, 3:1, 4:1}
  top = {(3,2), (1,4)} → windowSum = 2*3 + 4*1 = 10
Window [2,2,3,4,2,3]: counts {2:3, 3:2, 4:1}
  top = {(3,2), (2,3)} → windowSum = 2*3 + 3*2 = 12
```

---

## ⏱️ Time Complexity
```
O(n * log x) — each element update involves log-time set operations
```

## 💾 Space Complexity
```
O(n) — for the count map and sets
```

---

## ⚠️ Edge Cases
- `x >= k` → all elements are in top, x-sum equals regular sum
- All elements are the same → single element in top with full count
- `k = 1` → each element is its own x-sum

---

## 🎯 Interview Takeaways
- Two-set partitioning (top/bottom) is a powerful pattern for "top-k" sliding window problems.
- Always rebalance after updates to maintain the invariant.

---

## 📌 Key Pattern
👉 **"Two ordered sets to maintain top-x elements in a sliding window"**

---

## 🔁 Related Problems
- 3321. Find X-Sum of All K-Long Subarrays II
- 480. Sliding Window Median
- 295. Find Median from Data Stream

---

## 🚀 Final Thoughts
The two-multiset approach cleanly separates the top-x tracking from window management. This pattern scales well to the harder version (3321).

---

✨ **Rule to remember:**
> "For top-k in a sliding window, split into two ordered containers and rebalance on every update."
