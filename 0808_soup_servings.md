# 808. Soup Servings

## 🔗 Problem Link
https://leetcode.com/problems/soup-servings/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Math, Dynamic Programming, Memoization

---

## 🧩 Problem Summary
There are two types of soup, A and B. Each turn, one of four operations is chosen with equal probability, serving different amounts from A and B. Return the probability that soup A empties first, plus half the probability that both empty at the same time.

### 📌 Constraints
- `0 <= n <= 10^9`

---

## 💭 Intuition
👉 Since soup A is served more on average, for large `n` the probability converges to 1.0. We can short-circuit for `n >= 4800`. For smaller values, we scale down by 25 and use memoized DFS over the four serving options.

---

## ⚡ Approach — Memoized DFS with Scaling

### 🧠 Idea
- For `n >= 4800`, return `1.0` directly (probability is close enough to 1).
- Scale `n` by dividing by 25 (rounding up) to reduce the state space.
- Use DFS with memoization over `(a, b)` states representing remaining servings.
- At each state, recurse on 4 operations with equal probability (0.25 each).

---

## 💻 Code

```cpp
class Solution {
 public:
  double soupServings(int n) {
    return n >= 4800 ? 1.0 : dfs((n + 24) / 25, (n + 24) / 25);
  }

 private:
  vector<vector<double>> mem =
      vector<vector<double>>(4800 / 25, vector<double>(4800 / 25));

  double dfs(int a, int b) {
    if (a <= 0 && b <= 0)
      return 0.5;
    if (a <= 0)
      return 1.0;
    if (b <= 0)
      return 0.0;
    if (mem[a][b] > 0)
      return mem[a][b];
    return mem[a][b] = 0.25 * (dfs(a - 4, b) + dfs(a - 3, b - 1) +
                               dfs(a - 2, b - 2) + dfs(a - 1, b - 3));
  }
};
```

---

## 🧠 Dry Run
### Input
```
n = 50
```
### Steps
```
Scaled: a = b = ceil(50/25) = 2
dfs(2,2) = 0.25 * (dfs(-2,2) + dfs(-1,1) + dfs(0,0) + dfs(1,-1))
         = 0.25 * (1.0 + 1.0 + 0.5 + 0.0)
         = 0.25 * 2.5
         = 0.625
```

---

## ⏱️ Time Complexity
```
O((n/25)^2) for small n, O(1) for n >= 4800
```

## 💾 Space Complexity
```
O((n/25)^2) for the memoization table
```

---

## ⚠️ Edge Cases
- `n = 0`: Both soups are empty, return `0.5`.
- `n >= 4800`: Probability is effectively 1.0.
- Small `n`: Exact computation via DFS.

---

## 🎯 Interview Takeaways
- Recognizing convergence allows short-circuiting for large inputs.
- Scaling down the problem (dividing by 25) drastically reduces state space.
- Memoization on a 2D state is natural for this type of probability problem.

---

## 📌 Key Pattern
👉 **"Probability DFS with memoization, short-circuited by convergence for large inputs"**

---

## 🔁 Related Problems
- 688. Knight Probability in an N x N Chessboard
- 837. New 21 Game

---

## 🚀 Final Thoughts
The clever insight here is that soup A runs out faster on average, so beyond a threshold, the answer is essentially 1.0. This avoids TLE on huge inputs while still being exact for small ones. The scaling trick is also key to keeping the state space manageable.

---

✨ **Rule to remember:**
> "When a probability converges for large N, find the threshold and short-circuit; use scaling to shrink the state space."
