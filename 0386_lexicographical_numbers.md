# 386. Lexicographical Numbers

## 🔗 Problem Link
https://leetcode.com/problems/lexicographical-numbers/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Depth-First Search, Trie

---

## 🧩 Problem Summary
Given an integer n, return all numbers in the range [1, n] sorted in lexicographical order. The algorithm must run in O(n) time and use O(1) extra space (excluding the output).

### 📌 Constraints
- `1 <= n <= 5 * 10^4`

---

## 💭 Intuition
👉 Lexicographical order is like a pre-order traversal of a 10-ary trie. From any number, try to go deeper (multiply by 10). If that exceeds n or we've exhausted a branch, move to the next sibling (increment), handling carries by dividing by 10.

---

## ⚡ Approach — Iterative Trie Traversal

### 🧠 Idea
- Start with `curr = 1`.
- At each step, try to go deeper: if `curr * 10 <= n`, multiply by 10.
- Otherwise, move to next sibling: increment curr, but first backtrack past any 9s or past n by dividing by 10.
- Continue until all n numbers are collected.

---

## 💻 Code

```cpp
class Solution {
 public:
  vector<int> lexicalOrder(int n) {
    vector<int> ans;
    int curr = 1;

    while (ans.size() < n) {
      ans.push_back(curr);
      if (curr * 10 <= n) {
        curr *= 10;
      } else {
        while (curr % 10 == 9 || curr == n)
          curr /= 10;
        ++curr;
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
n = 13
```
### Steps
```
curr=1 -> push 1, 10<=13 -> curr=10
curr=10 -> push 10, 100>13 -> 10%10==0,10!=13 -> curr=11
curr=11 -> push 11, 110>13 -> 11%10!=9,11!=13 -> curr=12
curr=12 -> push 12, 120>13 -> 12%10!=9,12!=13 -> curr=13
curr=13 -> push 13, 130>13 -> 13==13 -> curr=1, curr=2
curr=2 -> push 2, 20>13 -> curr=3
... continue: 3,4,5,6,7,8,9
Result: [1,10,11,12,13,2,3,4,5,6,7,8,9]
```

---

## ⏱️ Time Complexity
```
O(n) — each number is visited exactly once
```

## 💾 Space Complexity
```
O(1) — excluding the output array
```

---

## ⚠️ Edge Cases
- `n = 1` — return [1].
- `n = 9` — return [1,2,...,9], same as normal order.
- `n = 10` — return [1,10,2,3,...,9].
- Numbers ending in 9 require backtracking.

---

## 🎯 Interview Takeaways
- Lexicographical ordering maps naturally to trie traversal.
- The iterative approach avoids recursion overhead and achieves O(1) space.
- Handling the "carry" (backtracking past 9s) is the tricky part.

---

## 📌 Key Pattern
👉 **"Iterative 10-ary trie traversal — go deep (* 10) or move to sibling (+ 1)"**

---

## 🔁 Related Problems
- 440. K-th Smallest in Lexicographical Order
- 1415. The k-th Lexicographical String of All Happy Strings of Length n

---

## 🚀 Final Thoughts
This problem demonstrates how lexicographical order corresponds to pre-order traversal of a number trie. The iterative solution is elegant and efficient, avoiding the overhead of explicit DFS recursion.

---

✨ **Rule to remember:**
> "Lex order = trie pre-order: go deep by * 10, backtrack and sibling by / 10 then + 1."
