# 3321. Find X-Sum of All K-Long Subarrays II

## 🔗 Problem Link
https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Hash Table, Sliding Window, Heap (Priority Queue), Ordered Set

---

## 🧩 Problem Summary
Same as problem 3318 but with larger constraints. Given an array `nums` and integers `k` and `x`, compute the x-sum of every contiguous subarray of length `k`. The x-sum uses the top `x` most frequent elements (ties broken by value), requiring an efficient approach.

### 📌 Constraints
- `1 <= nums.length <= 10^5`
- `1 <= x <= k <= nums.length`
- `1 <= nums[i] <= 10^9`

---

## 💭 Intuition
👉 Same two-multiset approach as 3318, but with `long long` to handle large values and `static_cast<long>` to prevent integer overflow during multiplication.

---

## ⚡ Approach — Two Multisets with Sliding Window (Optimized for Large Input)

### 🧠 Idea
- Maintain `top` and `bot` multisets of `(count, value)` pairs.
- Use `static_cast<long>` for multiplication to avoid overflow.
- Slide the window, update counts, and rebalance sets at each step.
- Return `long long` results.

---

## 💻 Code

```cpp
class Solution {
 public:
  // Same as 3318. Find X-Sum of All K-Long Subarrays I
  vector<long long> findXSum(vector<int>& nums, int k, int x) {
    vector<long long> ans;
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
          windowSum -= static_cast<long>(num) * count[num];
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
        windowSum += static_cast<long>(b) * countB;
      }
      // Swap the bottom and top elements if needed.
      while (!bot.empty() && *bot.rbegin() > *top.begin()) {
        const auto [countB, b] = *bot.rbegin();
        const auto [countT, t] = *top.begin();
        bot.erase(--bot.end());
        top.erase(top.begin());
        bot.insert({countT, t});
        top.insert({countB, b});
        windowSum += static_cast<long>(b) * countB;
        windowSum -= static_cast<long>(t) * countT;
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
Window [1,1,2,2,3,4]: top has (2,2) and (2,1) → windowSum = 4 + 2 = 6
Window [1,2,2,3,4,2]: top has (3,2) and (1,4) → windowSum = 6 + 4 = 10
Window [2,2,3,4,2,3]: top has (3,2) and (2,3) → windowSum = 6 + 6 = 12
```

---

## ⏱️ Time Complexity
```
O(n * log x) — set operations are O(log x) per update
```

## 💾 Space Complexity
```
O(n) — for count map, sets, and result array
```

---

## ⚠️ Edge Cases
- Large values (`nums[i]` up to 10^9) require `long long` arithmetic
- `x >= distinct elements` → all elements in top
- Duplicate heavy arrays → frequent rebalancing

---

## 🎯 Interview Takeaways
- Always consider overflow when scaling up from easy to hard versions.
- `static_cast<long>` before multiplication prevents silent overflow.
- The same algorithmic pattern works; only data types change.

---

## 📌 Key Pattern
👉 **"Scale easy solutions to hard constraints by fixing overflow and using appropriate types"**

---

## 🔁 Related Problems
- 3318. Find X-Sum of All K-Long Subarrays I
- 480. Sliding Window Median
- 295. Find Median from Data Stream

---

## 🚀 Final Thoughts
This is a direct scale-up of 3318. The core algorithm is identical, but careful attention to integer overflow with `static_cast<long>` is what makes it pass the harder constraints.

---

✨ **Rule to remember:**
> "When scaling from Easy to Hard, the algorithm stays the same — watch out for overflow."
