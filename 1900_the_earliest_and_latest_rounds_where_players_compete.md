# 1900. The Earliest and Latest Rounds Where Players Compete

## 🔗 Problem Link
https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Dynamic Programming, Memoization, Recursion, Simulation

---

## 🧩 Problem Summary
In a tournament of `n` players in a line, each round the 1st fights the last, 2nd fights second-to-last, etc. Winners maintain relative order for the next round. Given two specific players (`firstPlayer` and `secondPlayer`), find the earliest and latest round they can compete against each other (across all possible outcomes of other matches).

### 📌 Constraints
- `2 <= n <= 28`
- `1 <= firstPlayer < secondPlayer <= n`

---

## 💭 Intuition
👉 Model the state as `(l, r, k)` where `l` is the first player's position from the front, `r` is the second player's position from the end, and `k` is the current number of players. Use memoized recursion to enumerate all valid configurations of winners.

---

## ⚡ Approach — Memoized Recursion (State: Position from Ends + Count)

### 🧠 Idea
- Represent state as positions of the two target players relative to the ends, plus total player count.
- Base case: `l == r` means they are facing each other → round 1.
- Enumerate how many players can win from positions before, between, and after the two target players.
- Recurse with updated positions in the next round (halved player count).
- Track global minimum (earliest) and maximum (latest) across all valid enumerations.

---

## 💻 Code

```cpp
class Solution {
 public:
  vector<int> earliestAndLatest(int n, int firstPlayer, int secondPlayer) {
    using P = pair<int, int>;
    vector<vector<vector<P>>> mem(n + 1,
                                  vector<vector<P>>(n + 1, vector<P>(n + 1)));
    const auto [a, b] = solve(firstPlayer, n - secondPlayer + 1, n, mem);
    return {a, b};
  }

 private:
  // Returns the (earliest, latest) pair, the first player is the l-th player
  // from the front, the second player is the r-th player from the end, and
  // there're k people.
  pair<int, int> solve(int l, int r, int k,
                       vector<vector<vector<pair<int, int>>>>& mem) {
    if (l == r)
      return {1, 1};
    if (l > r)
      swap(l, r);
    if (mem[l][r][k] != pair<int, int>{0, 0})
      return mem[l][r][k];

    int a = INT_MAX;
    int b = INT_MIN;

    // Enumerate all the possible positions.
    for (int i = 1; i <= l; ++i)
      for (int j = l - i + 1; j <= r - i; ++j) {
        if (i + j > (k + 1) / 2 || i + j < l + r - k / 2)
          continue;
        const auto [x, y] = solve(i, j, (k + 1) / 2, mem);
        a = min(a, x + 1);
        b = max(b, y + 1);
      }

    return mem[l][r][k] = {a, b};
  }
};
```

---

## 🧠 Dry Run
### Input
```
n = 11, firstPlayer = 2, secondPlayer = 4
```
### Steps
```
Initial: l=2, r=11-4+1=8, k=11
Enumerate valid (i, j) pairs for next round where (k+1)/2 = 6 players remain.
For each valid configuration, recurse with new positions and k=6.
Continue until l == r (they face each other).
Track min/max rounds across all branches.
Result: [3, 4] (earliest round 3, latest round 4)
```

---

## ⏱️ Time Complexity
```
O(n^3) states, each with O(n^2) enumeration → O(n^5) worst case, but n ≤ 28 makes this feasible
```

## 💾 Space Complexity
```
O(n^3) for memoization table
```

---

## ⚠️ Edge Cases
- `firstPlayer` and `secondPlayer` are at opposite ends → they compete in round 1
- `n = 2` → always round 1
- Players are adjacent → may or may not compete in round 1 depending on positions

---

## 🎯 Interview Takeaways
- Reducing the state space to relative positions (from front and end) is the key simplification.
- Memoization with structured states handles exponential branching efficiently.
- Tournament bracket problems often require careful enumeration of winner configurations.

---

## 📌 Key Pattern
👉 **"Memoized recursion with state reduction to track positions through tournament rounds"**

---

## 🔁 Related Problems
- 390. Elimination Game
- 1900. Closest Dessert Cost (different problem, similar number)
- 1259. Handshakes That Don't Cross

---

## 🚀 Final Thoughts
This is a challenging combinatorial problem where the key insight is representing the state by the relative positions of the two players and the total count, rather than tracking all player positions. The enumeration of valid next-round configurations requires careful bounds checking.

---

✨ **Rule to remember:**
> In tournament problems, track target players by their relative positions, not absolute ones.
