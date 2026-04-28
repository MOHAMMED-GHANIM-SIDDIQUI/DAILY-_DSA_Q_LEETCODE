# 837. New 21 Game

## 🔗 Problem Link
https://leetcode.com/problems/new-21-game/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Math, Dynamic Programming, Sliding Window, Probability

---

## 🧩 Problem Summary
Alice plays a game where she draws numbers in `[1, maxPts]` uniformly at random, stopping when she has `k` or more points. Return the probability that her total points are at most `n`.

### 📌 Constraints
- `0 <= k <= n <= 10^4`
- `1 <= maxPts <= 10^4`

---

## 💭 Intuition
👉 The probability of reaching exactly `i` points is the average of probabilities of the previous `maxPts` states. A sliding window sum efficiently maintains this running average without recomputing each time.

---

## ⚡ Approach — DP with Sliding Window

### 🧠 Idea
- `dp[i]` = probability of having exactly `i` points.
- `dp[i] = windowSum / maxPts`, where `windowSum = dp[i-1] + dp[i-2] + ... + dp[i-maxPts]`.
- Only add `dp[i]` to `windowSum` if `i < k` (game hasn't stopped).
- If `i >= k`, the game ended, so add `dp[i]` to the answer.
- Slide the window by removing `dp[i - maxPts]` when it falls out of range.

---

## 💻 Code

```cpp
class Solution {
 public:
  double new21Game(int n, int k, int maxPts) {
    // When the game ends, the point is in [k..k - 1 maxPts].
    //   P = 1, if n >= k - 1 + maxPts
    //   P = 0, if n < k (note that the constraints already have k <= n)
    if (k == 0 || n >= k - 1 + maxPts)
      return 1.0;

    double ans = 0.0;
    vector<double> dp(n + 1);  // dp[i] := the probability to have i points
    dp[0] = 1.0;
    double windowSum = dp[0];  // P(i - 1) + P(i - 2) + ... + P(i - maxPts)

    for (int i = 1; i <= n; ++i) {
      // The probability to get i points is
      // P(i) = [P(i - 1) + P(i - 2) + ... + P(i - maxPts)] / maxPts
      dp[i] = windowSum / maxPts;
      if (i < k)
        windowSum += dp[i];
      else  // The game ends.
        ans += dp[i];
      if (i - maxPts >= 0)
        windowSum -= dp[i - maxPts];
    }

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
n = 6, k = 1, maxPts = 10
```
### Steps
```
dp[0] = 1.0, windowSum = 1.0
i=1: dp[1] = 1.0/10 = 0.1, i>=k -> ans += 0.1 = 0.1
i=2: dp[2] = 1.0/10 = 0.1, ans += 0.1 = 0.2
...
i=6: dp[6] = 1.0/10 = 0.1, ans += 0.1 = 0.6

Result: 0.6
```

---

## ⏱️ Time Complexity
```
O(n)
```

## 💾 Space Complexity
```
O(n)
```

---

## ⚠️ Edge Cases
- `k = 0`: Alice never draws, she has 0 points which is always <= n. Return 1.0.
- `n >= k - 1 + maxPts`: Maximum possible score is always <= n. Return 1.0.

---

## 🎯 Interview Takeaways
- Sliding window optimization turns an O(n * maxPts) DP into O(n).
- Recognizing when the game "stops" (i >= k) is key to correctly accumulating the answer.
- Early return for trivial cases (k=0 or guaranteed win) simplifies the code.

---

## 📌 Key Pattern
👉 **"Probability DP with sliding window sum for efficient transition computation"**

---

## 🔁 Related Problems
- 70. Climbing Stairs
- 808. Soup Servings
- 1155. Number of Dice Rolls With Target Sum

---

## 🚀 Final Thoughts
This problem beautifully combines probability, DP, and the sliding window technique. The insight that each state depends on a contiguous range of previous states makes the sliding window optimization natural and powerful.

---

✨ **Rule to remember:**
> "When each DP state depends on the sum of a fixed-size window of previous states, use a sliding window to compute it in O(1) per state."
