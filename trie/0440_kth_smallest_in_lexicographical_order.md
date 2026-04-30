# 440. K-th Smallest in Lexicographical Order

## 🔗 Problem Link
https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Trie, Math

---

## 🧩 Problem Summary
Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n]. Unlike problem 386, this must work efficiently for very large n without generating all numbers.

### 📌 Constraints
- `1 <= k <= n <= 10^9`

---

## 💭 Intuition
👉 Think of numbers [1, n] as a 10-ary trie. To find the kth element, we need to efficiently count how many nodes are in each subtree so we can skip entire subtrees instead of visiting every node.

---

## ⚡ Approach — Trie Gap Counting

### 🧠 Idea
- Start at prefix 1. Maintain a counter i = 1 (we're at the 1st element).
- Compute the "gap" — the number of nodes in the subtree rooted at the current prefix.
- If `i + gap <= k`, skip the entire subtree (move to the next sibling by incrementing prefix).
- Otherwise, go deeper into the subtree (multiply prefix by 10, increment i).
- The `getGap` function counts nodes between two adjacent prefixes level by level.

---

## 💻 Code

```cpp
class Solution {
 public:
  int findKthNumber(int n, int k) {
    long ans = 1;

    for (int i = 1; i < k;) {
      const long gap = getGap(ans, ans + 1, n);
      if (i + gap <= k) {
        i += gap;
        ++ans;
      } else {
        ++i;
        ans *= 10;
      }
    }

    return ans;
  }

 private:
  long getGap(long a, long b, long n) {
    long gap = 0;
    while (a <= n) {
      gap += min(n + 1, b) - a;
      a *= 10;
      b *= 10;
    }
    return gap;
  };
};
```

---

## 🧠 Dry Run
### Input
```
n = 13, k = 2
```
### Steps
```
ans=1, i=1
gap = getGap(1, 2, 13):
  a=1,b=2: gap += min(14,2)-1 = 1
  a=10,b=20: gap += min(14,20)-10 = 4
  a=100,b=200: 100>13, stop. gap=5
i + gap = 1 + 5 = 6 > 2, so go deeper: i=2, ans=10
i=2 == k=2, stop.
Result: 10
```

---

## ⏱️ Time Complexity
```
O(log(n)^2) — at most O(log n) steps, each getGap call is O(log n)
```

## 💾 Space Complexity
```
O(1)
```

---

## ⚠️ Edge Cases
- `k = 1` — always returns 1.
- `n < 10` — simple linear order.
- Very large n (up to 10^9) — the gap counting ensures efficiency.
- k equals n — need to traverse the entire trie logically.

---

## 🎯 Interview Takeaways
- Counting nodes in a trie subtree without building the trie is the core skill.
- The level-by-level gap counting is elegant and avoids enumeration.
- This problem extends problem 386 (Lexicographical Numbers) to handle large n.

---

## 📌 Key Pattern
👉 **"Count trie subtree sizes to skip entire branches — O(log^2 n) lexicographic search"**

---

## 🔁 Related Problems
- 386. Lexicographical Numbers
- 1415. The k-th Lexicographical String of All Happy Strings

---

## 🚀 Final Thoughts
This is one of the hardest trie/math problems on LeetCode. The key insight is treating the number range as a virtual trie and counting subtree sizes to navigate efficiently without materializing the structure.

---

✨ **Rule to remember:**
> "Don't enumerate — count subtree sizes to skip entire branches in the lexicographic trie."
