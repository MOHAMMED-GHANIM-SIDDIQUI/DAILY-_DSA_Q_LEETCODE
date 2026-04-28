# 2140. Solving Questions With Brainpower

## 🔗 Problem Link
https://leetcode.com/problems/solving-questions-with-brainpower/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Dynamic Programming

---

## 🧩 Problem Summary
You are given a 0-indexed 2D array `questions` where `questions[i] = [points_i, brainpower_i]`. If you solve question `i`, you earn `points_i` but must skip the next `brainpower_i` questions. Return the maximum points you can earn.

### 📌 Constraints
- `1 <= questions.length <= 10^5`
- `questions[i].length == 2`
- `1 <= points_i, brainpower_i <= 10^5`

---

## 💭 Intuition
👉 Process questions from right to left. For each question, decide whether to solve it (earn points + best from next valid question) or skip it (take the best from the next question).

---

## ⚡ Approach — Bottom-Up Dynamic Programming

### 🧠 Idea
- Define `dp[i]` = maximum points starting from question `i`.
- For each question from right to left:
  - If solved: `points + dp[i + brainpower + 1]` (if in bounds, else just `points`).
  - If skipped: `dp[i + 1]`.
  - `dp[i] = max(solve, skip)`.

---

## 💻 Code

```cpp
class Solution {
public:
    long long mostPoints(vector<vector<int>>& questions) {
        const int n = questions.size(); // Total number of questions
        vector<long> dp(n + 1, 0); // dp[i] will store the maximum points starting from question i

        // Process the questions from the last one to the first one
        for (int i = n - 1; i >= 0; --i) {
            const int points = questions[i][0]; // Points for the current question
            const int brainpower = questions[i][1]; // Number of questions to skip after this question
            const int nextIndex = i + brainpower + 1; // The index of the next question after skipping the brainpower questions

            // If nextIndex is within bounds, we take the points from the next question, otherwise 0
            const long nextPoints = nextIndex < n ? dp[nextIndex] : 0;

            // dp[i] = max points by either:
            // 1. Taking the current question's points + the points we can get from the next valid question
            // 2. Skipping the current question and taking the points starting from the next question
            dp[i] = max(points + nextPoints, dp[i + 1]);
        }

        // The answer is the maximum points starting from the first question (dp[0])
        return dp[0];
    }
};
```

---

## 🧠 Dry Run
### Input
```
questions = [[3,2],[4,3],[4,4],[2,5]]
```
### Steps
```
n=4, dp = [0,0,0,0,0]
i=3: points=2, brainpower=5, nextIndex=9>=4 -> nextPoints=0
     dp[3] = max(2+0, dp[4]=0) = 2
i=2: points=4, brainpower=4, nextIndex=7>=4 -> nextPoints=0
     dp[2] = max(4+0, dp[3]=2) = 4
i=1: points=4, brainpower=3, nextIndex=5>=4 -> nextPoints=0
     dp[1] = max(4+0, dp[2]=4) = 4
i=0: points=3, brainpower=2, nextIndex=3<4 -> nextPoints=dp[3]=2
     dp[0] = max(3+2, dp[1]=4) = 5
Return 5
```

---

## ⏱️ Time Complexity
```
O(n), single pass from right to left
```

## 💾 Space Complexity
```
O(n) for the dp array
```

---

## ⚠️ Edge Cases
- Only one question: return its points
- All brainpower values are 0: solve all questions
- Very large brainpower: solving one question might mean skipping the rest
- Points vary wildly: DP correctly evaluates all trade-offs

---

## 🎯 Interview Takeaways
- Right-to-left DP is natural when decisions affect future choices.
- The "solve or skip" pattern is a classic DP formulation.
- Bounds checking on `nextIndex` prevents array out-of-bounds.

---

## 📌 Key Pattern
👉 **"Right-to-left DP with solve-or-skip decision at each step"**

---

## 🔁 Related Problems
- 198. House Robber
- 740. Delete and Earn
- 1626. Best Team With No Conflicts

---

## 🚀 Final Thoughts
This is a clean DP problem that follows the "take or skip" pattern similar to House Robber, but with variable skip lengths. Processing right-to-left makes the recurrence straightforward.

---

✨ **Rule to remember:**
> When solving a question forces you to skip future ones, use right-to-left DP with solve-or-skip at each index.
