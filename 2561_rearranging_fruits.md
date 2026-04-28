# 2561. Rearranging Fruits

## 🔗 Problem Link
https://leetcode.com/problems/rearranging-fruits/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Hash Table, Greedy, Sorting

---

## 🧩 Problem Summary
Given two fruit baskets `basket1` and `basket2`, you can swap any fruit from basket1 with any fruit from basket2 at a cost equal to the minimum of the two swapped values. Make both baskets contain the same multiset of fruits with minimum total cost, or return -1 if impossible.

### 📌 Constraints
- `basket1.length == basket2.length <= 10^5`
- `1 <= basket1[i], basket2[i] <= 10^9`

---

## 💭 Intuition
👉 Count the net difference of each fruit. If any fruit has an odd total imbalance, it's impossible. For fruits that need swapping, we can either swap them directly (cost = min of the two) or use a "relay" through the global minimum element (cost = 2 * globalMin). We pick the cheaper option for each swap.

---

## ⚡ Approach — Greedy with Global Minimum Relay

### 🧠 Idea
- Count frequency difference: `++count[b]` for basket1, `--count[b]` for basket2.
- If any frequency is odd, return -1 (can't balance).
- Collect `|freq|/2` copies of each imbalanced fruit into a `swapped` list.
- Partial sort to find the cheaper half of swaps.
- For each swap, cost is `min(2 * globalMin, fruit_value)`.

---

## 💻 Code

```cpp
class Solution {
 public:
  long long minCost(vector<int>& basket1, vector<int>& basket2) {
    vector<int> swapped;
    unordered_map<int, int> count;

    for (const int b : basket1)
      ++count[b];

    for (const int b : basket2)
      --count[b];

    for (const auto& [num, freq] : count) {
      if (freq % 2 != 0)
        return -1;
      for (int i = 0; i < abs(freq) / 2; ++i)
        swapped.push_back(num);
    }

    const int minNum = min(ranges::min(basket1), ranges::min(basket2));
    const auto midIt = swapped.begin() + swapped.size() / 2;
    nth_element(swapped.begin(), midIt, swapped.end());
    return accumulate(swapped.begin(), midIt, 0L, [minNum](long acc, int num) {
      return acc + min(2 * minNum, num);
    });
  }
};
```

---

## 🧠 Dry Run
### Input
```
basket1 = [4,2,2,2], basket2 = [1,4,1,2]
```
### Steps
```
count: {4:0, 2:2, 1:-2}  (after both baskets)
freq of 2 is 2 (even), freq of 1 is -2 (even)
swapped = [2, 1]  (one 2 needs to go out, one 1 needs to come in)
minNum = 1
nth_element splits at midIt (index 1): first half = [1]
cost = min(2*1, 1) = 1
Answer: 1
```

---

## ⏱️ Time Complexity
```
O(n log n) due to nth_element being O(n) average, overall dominated by hash map operations
```

## 💾 Space Complexity
```
O(n)
```

---

## ⚠️ Edge Cases
- Baskets already identical — no swaps needed, cost is 0
- Impossible case where a fruit appears an odd total number of times
- The cheapest swap uses a relay through the smallest element

---

## 🎯 Interview Takeaways
- The "relay swap" trick: instead of directly swapping an expensive fruit, swap it to the minimum element first, then swap that minimum to the target — total cost is `2 * min`.
- `nth_element` is a great tool for partial sorting when you only need the smaller/larger half.

---

## 📌 Key Pattern
👉 **"Greedy swap optimization — use a relay through the global minimum for expensive swaps"**

---

## 🔁 Related Problems
- 1247. Minimum Swaps to Make Strings Equal
- 1029. Two City Scheduling

---

## 🚀 Final Thoughts
The clever insight is the relay swap: for an expensive direct swap, it may be cheaper to do two swaps through the cheapest element. This turns a seemingly complex optimization into a simple greedy choice per swap.

---

✨ **Rule to remember:**
> When swapping is costly, consider relaying through the cheapest available element — two cheap swaps can beat one expensive one.
