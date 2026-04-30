# 2300. Successful Pairs of Spells and Potions

## 🔗 Problem Link
https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Binary Search, Sorting, Two Pointers

---

## 🧩 Problem Summary
Given arrays `spells` and `potions` and a threshold `success`, for each spell find how many potions form a successful pair (spell * potion >= success). Return an array of counts.

### 📌 Constraints
- `1 <= spells.length, potions.length <= 10^5`
- `1 <= spells[i], potions[i] <= 10^5`
- `1 <= success <= 10^10`

---

## 💭 Intuition
👉 Sort potions, then for each spell binary search for the smallest potion that satisfies the threshold. All potions from that index onward are successful.

---

## ⚡ Approach — Sort + Binary Search

### 🧠 Idea
- Sort the `potions` array.
- For each spell, binary search for the first potion index where `spell * potion >= success`.
- The count of successful pairs is `potions.size() - index`.

---

## 💻 Code

```cpp
class Solution {
 public:
  vector<int> successfulPairs(vector<int>& spells, vector<int>& potions,
                              long long success) {
    vector<int> ans;
    ranges::sort(potions);

    for (const int spell : spells)
      ans.push_back(potions.size() -
                    firstIndexSuccess(spell, potions, success));

    return ans;
  }

 private:
  // Returns the first index i s.t. spell * potions[i] >= success.
  int firstIndexSuccess(int spell, const vector<int>& potions, long success) {
    int l = 0;
    int r = potions.size();
    while (l < r) {
      const int m = (l + r) / 2;
      if (static_cast<long>(spell) * potions[m] >= success)
        r = m;
      else
        l = m + 1;
    }
    return l;
  }
};
```

---

## 🧠 Dry Run
### Input
```
spells = [5, 1, 3], potions = [1, 2, 3, 4, 5], success = 7
```
### Steps
```
Sorted potions: [1, 2, 3, 4, 5]

Spell 5: need potion >= ceil(7/5) = 2 → index 1, count = 5-1 = 4
Spell 1: need potion >= 7 → index 5 (not found), count = 5-5 = 0
Spell 3: need potion >= ceil(7/3) = 3 → index 2, count = 5-2 = 3

Result: [4, 0, 3]
```

---

## ⏱️ Time Complexity
```
O((n + m) log m) — sort potions O(m log m), binary search per spell O(n log m)
```

## 💾 Space Complexity
```
O(1) — excluding the output array
```

---

## ⚠️ Edge Cases
- Spell is very large → all potions succeed
- Spell is 1 and success is very large → few or no potions succeed
- All potions are identical → binary search finds the boundary quickly

---

## 🎯 Interview Takeaways
- Sort one array, binary search for each element of the other — classic O(n log m) pattern.
- Use `long` casting to avoid integer overflow in multiplication.
- The "first index" binary search template is reusable across many problems.

---

## 📌 Key Pattern
👉 **"Sort + binary search for threshold counting across two arrays"**

---

## 🔁 Related Problems
- 2226. Maximum Candies Allocated to K Children
- 875. Koko Eating Bananas
- 34. Find First and Last Position of Element in Sorted Array

---

## 🚀 Final Thoughts
A classic application of sorting one array and binary searching from the other. The key detail is handling long overflow when multiplying spell by potion.

---

✨ **Rule to remember:**
> "Sort potions once, binary search per spell — O(n log m) beats O(n * m) brute force."
