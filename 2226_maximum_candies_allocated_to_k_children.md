# 2226. Maximum Candies Allocated to K Children

## 🔗 Problem Link
https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Binary Search

---

## 🧩 Problem Summary
Given an array `candies` where each element is a pile of candies, and `k` children, divide the piles such that each child gets the same number of candies from a single sub-pile. Maximize the number of candies each child gets. Piles can be split but not merged.

### 📌 Constraints
- `1 <= candies.length <= 10^5`
- `1 <= candies[i] <= 10^7`
- `1 <= k <= 10^12`

---

## 💭 Intuition
👉 Binary search on the answer: for a given candy count `m`, check if we can serve at least `k` children by summing `floor(candies[i] / m)` across all piles.

---

## ⚡ Approach — Binary Search on Answer

### 🧠 Idea
- Binary search over the possible candy count per child `[1, total/k]`.
- For each candidate `m`, compute how many children can be served.
- Find the largest `m` where at least `k` children can be served.

---

## 💻 Code

```cpp
class Solution {
 public:
  int maximumCandies(vector<int>& candies, long long k) {
    int l = 1;
    int r = accumulate(candies.begin(), candies.end(), 0L) / k;

    while (l < r) {
      const int m = (l + r) / 2;
      if (numChildren(candies, m) < k)
        r = m;
      else
        l = m + 1;
    }

    return numChildren(candies, l) >= k ? l : l - 1;
  }

 private:
  long numChildren(const vector<int>& candies, int m) {
    return accumulate(candies.begin(), candies.end(), 0L,
                      [&](long subtotal, int c) { return subtotal + c / m; });
  };
};
```

---

## 🧠 Dry Run
### Input
```
candies = [5, 8, 6], k = 3
```
### Steps
```
total = 19, r = 19/3 = 6, l = 1
m = 3: children = 5/3+8/3+6/3 = 1+2+2 = 5 >= 3 → l=4
m = 5: children = 5/5+8/5+6/5 = 1+1+1 = 3 >= 3 → l=6
m = 6: l=6 >= r=6 → exit
numChildren(6) = 0+1+1 = 2 < 3 → return 6-1 = 5
```

---

## ⏱️ Time Complexity
```
O(n log(total/k)) — binary search with O(n) feasibility check per step
```

## 💾 Space Complexity
```
O(1) — constant extra space
```

---

## ⚠️ Edge Cases
- `k` exceeds total candies → return 0
- All piles have size 1 → answer is 0 or 1
- Single pile, single child → answer is the pile size

---

## 🎯 Interview Takeaways
- "Binary search on the answer" is a classic pattern for optimization problems with monotonic feasibility.
- The feasibility check must be efficient — here it is O(n).
- Be careful with the boundary: check if `l` is feasible or return `l-1`.

---

## 📌 Key Pattern
👉 **"Binary search on the answer with a greedy feasibility check"**

---

## 🔁 Related Problems
- 875. Koko Eating Bananas
- 1011. Capacity To Ship Packages Within D Days
- 1552. Magnetic Force Between Two Balls

---

## 🚀 Final Thoughts
A textbook binary search on answer problem. The monotonic property — more candies per child means fewer children served — makes binary search applicable. The feasibility check is a simple sum of integer divisions.

---

✨ **Rule to remember:**
> "When maximizing a distributable quantity, binary search on the answer and verify feasibility greedily."
