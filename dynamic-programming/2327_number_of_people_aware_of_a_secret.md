# 2327. Number of People Aware of a Secret

## 🔗 Problem Link
https://leetcode.com/problems/number-of-people-aware-of-a-secret/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Dynamic Programming, Simulation

---

## 🧩 Problem Summary
On day 1, one person discovers a secret. Each person who knows the secret can share it starting from `delay` days after discovering it, and forgets it `forget` days after discovering it. Return the number of people who know the secret at the end of day `n`.

### 📌 Constraints
- `2 <= n <= 1000`
- `1 <= delay < forget <= n`

---

## 💭 Intuition
👉 Track how many people discover the secret on each day using DP. A person discovered on day `i` shares from day `i+delay` to day `i+forget-1`, and forgets on day `i+forget`. Use a running `share` variable to track the active sharers.

---

## ⚡ Approach — Sliding Window DP

### 🧠 Idea
- `dp[i]` = number of people who discover the secret on day `i`.
- Maintain a running `share` count: add `dp[i-delay]` (new sharers) and subtract `dp[i-forget]` (people who forget).
- At the end, sum `dp[n-forget..n-1]` since only people who discovered in the last `forget` days still remember.

---

## 💻 Code

```cpp
class Solution {
 public:
  int peopleAwareOfSecret(int n, int delay, int forget) {
    constexpr int kMod = 1'000'000'007;
    long share = 0;
    // dp[i] := the number of people know the secret at day i
    vector<int> dp(n);  // Maps day i to i + 1.
    dp[0] = 1;

    for (int i = 1; i < n; ++i) {
      if (i - delay >= 0)
        share += dp[i - delay];
      if (i - forget >= 0)
        share -= dp[i - forget];
      share += kMod;
      share %= kMod;
      dp[i] = share;
    }

    // People before day `n - forget - 1` already forget the secret.
    return accumulate(dp.end() - forget, dp.end(), 0,
                      [&](int acc, int d) { return (acc + d) % kMod; });
  }
};
```

---

## 🧠 Dry Run
### Input
```
n = 6, delay = 2, forget = 4
```
### Steps
```
dp[0] = 1 (person discovers secret on day 1)
i=1: share=0, dp[1]=0
i=2: share += dp[0]=1, share=1, dp[2]=1
i=3: share += dp[1]=0, share=1, dp[3]=1
i=4: share += dp[2]=1, share=2; share -= dp[0]=1, share=1, dp[4]=1
i=5: share += dp[3]=1, share=2; share -= dp[1]=0, share=2, dp[5]=2

Sum dp[2..5] = 1+1+1+2 = 5
Result: 5
```

---

## ⏱️ Time Complexity
```
O(n) — single pass through days.
```

## 💾 Space Complexity
```
O(n) — dp array of size n.
```

---

## ⚠️ Edge Cases
- `delay = forget - 1`: each person can only share for one day.
- `n = 2`: minimal case, only original person remains.
- Large `n` with small `forget`: most early discoverers have forgotten.

---

## 🎯 Interview Takeaways
- Sliding window on DP transitions avoids nested loops.
- Modular arithmetic requires careful handling of subtraction (add MOD before taking mod).
- Only people in the last `forget` days still know the secret.

---

## 📌 Key Pattern
👉 **"Sliding window over DP states to track active contributors."**

---

## 🔁 Related Problems
- 70. Climbing Stairs
- 1137. N-th Tribonacci Number
- 2466. Count Ways To Build Good Strings

---

## 🚀 Final Thoughts
This problem transforms a simulation into an efficient DP with a sliding window. The running `share` variable elegantly captures the range of active sharers without iterating over the window each time.

---

✨ **Rule to remember:**
> "Use a running sum over a DP window to track who's actively sharing vs. who has forgotten."
