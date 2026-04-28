# 904. Fruit Into Baskets

## 🔗 Problem Link
https://leetcode.com/problems/fruit-into-baskets/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Hash Table, Sliding Window

---

## 🧩 Problem Summary
You have a row of trees, each bearing one type of fruit. You have two baskets, each can hold only one type of fruit. Starting from any tree, pick fruits moving right, stopping when you encounter a third type. Return the maximum number of fruits you can collect.

### 📌 Constraints
- `1 <= fruits.length <= 10^5`
- `0 <= fruits[i] < fruits.length`

---

## 💭 Intuition
👉 This is equivalent to finding the longest subarray with at most 2 distinct elements. A sliding window with a hash map tracking element counts efficiently solves this.

---

## ⚡ Approach — Sliding Window with Hash Map

### 🧠 Idea
- Expand the window by moving `r` right and adding `fruits[r]` to the count map.
- When the map has more than 2 keys (3+ fruit types), shrink from the left until only 2 types remain.
- Track the maximum window size throughout.

---

## 💻 Code

```cpp
class Solution {
 public:
  int totalFruit(vector<int>& fruits) {
    int ans = 0;
    unordered_map<int, int> count;

    for (int l = 0, r = 0; r < fruits.size(); ++r) {
      ++count[fruits[r]];
      while (count.size() > 2) {
        if (--count[fruits[l]] == 0)
          count.erase(fruits[l]);
        ++l;
      }
      ans = max(ans, r - l + 1);
    }

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
fruits = [1, 2, 3, 2, 2]
```
### Steps
```
r=0: count={1:1}, ans=1
r=1: count={1:1, 2:1}, ans=2
r=2: count={1:1, 2:1, 3:1} -> size>2, remove fruits[0]=1 -> count={2:1, 3:1}, l=1, ans=2
r=3: count={2:2, 3:1}, ans=3
r=4: count={2:3, 3:1}, ans=4

Result: 4
```

---

## ⏱️ Time Complexity
```
O(n), each element is added and removed from the window at most once
```

## 💾 Space Complexity
```
O(1), the hash map has at most 3 entries
```

---

## ⚠️ Edge Cases
- All same fruit type: return `n`.
- Only two types: return `n`.
- Alternating types: entire array is valid.

---

## 🎯 Interview Takeaways
- "At most K distinct elements" is a classic sliding window pattern.
- Hash map counting combined with window shrinking is the standard approach.
- Erasing map entries when count reaches 0 keeps the size check accurate.

---

## 📌 Key Pattern
👉 **"Sliding window with at most K distinct elements using a hash map counter"**

---

## 🔁 Related Problems
- 3. Longest Substring Without Repeating Characters
- 159. Longest Substring with At Most Two Distinct Characters
- 340. Longest Substring with At Most K Distinct Characters

---

## 🚀 Final Thoughts
This problem is a straightforward application of the sliding window with K distinct elements pattern. Once you recognize that "two baskets" means "at most 2 distinct types," the solution follows naturally. It is a must-know pattern for interviews.

---

✨ **Rule to remember:**
> "Two baskets = longest subarray with at most 2 distinct values = sliding window with a frequency map."
