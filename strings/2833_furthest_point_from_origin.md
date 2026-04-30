# 2833. Furthest Point From Origin

## 🔗 Problem Link
https://leetcode.com/problems/furthest-point-from-origin/

## ⚡ Difficulty
Easy

## 🏷️ Topics
String, Counting

---

## 🧩 Problem Summary
Given a string `moves` consisting of 'L', 'R', and '_', where 'L' moves left, 'R' moves right, and '_' can be either, return the furthest distance from the origin after performing all moves optimally.

### 📌 Constraints
- `1 <= moves.length <= 10^5`
- `moves` consists of characters `'L'`, `'R'`, and `'_'`.

---

## 💭 Intuition
👉 The 'L' and 'R' moves are fixed, so compute their net displacement. The '_' moves should all go in the same direction (whichever maximizes distance), so add the count of underscores to the absolute net displacement.

---

## ⚡ Approach — Counting with Greedy Assignment

### 🧠 Idea
- Track net displacement: +1 for 'R', -1 for 'L'.
- Count all '_' characters separately.
- The answer is `|net displacement| + count_of_underscores` — assign all wildcards to the dominant direction.

---

## 💻 Code

```python
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
      ans = 0
      cnt_of_underscore = 0
      for move in moves:
        if move == 'L':
          ans-=1
        elif move == 'R':
          ans+=1
        else :
          cnt_of_underscore+=1
      return cnt_of_underscore + abs(ans)
```

---

## 🧠 Dry Run
### Input
```
moves = "L_RL__R"
```
### Steps
```
L: ans=-1
_: cnt=1
R: ans=0
L: ans=-1
_: cnt=2
_: cnt=3
R: ans=0

Result = 3 + |0| = 3
(All 3 underscores go in one direction → distance = 3)
```

---

## ⏱️ Time Complexity
```
O(n) — single pass through the string.
```

## 💾 Space Complexity
```
O(1) — two integer variables.
```

---

## ⚠️ Edge Cases
- All underscores: answer is n (all go in one direction).
- No underscores: answer is |count_L - count_R|.
- Equal L and R with underscores: answer is count of underscores.

---

## 🎯 Interview Takeaways
- Wildcards should always be assigned greedily to maximize/minimize the objective.
- Net displacement plus wildcard count is a common pattern.
- Simple counting often suffices — no need for simulation.

---

## 📌 Key Pattern
👉 **"Greedy wildcard assignment: all wildcards go in the dominant direction."**

---

## 🔁 Related Problems
- 657. Robot Return to Origin
- 1041. Robot Bounded In Circle
- 2833. Furthest Point From Origin

---

## 🚀 Final Thoughts
An elegant easy problem that tests greedy thinking. The key insight is that wildcards should all be assigned uniformly to maximize distance, making the solution a simple counting exercise.

---

✨ **Rule to remember:**
> "Wildcards maximize distance when they all move in the same direction as the net displacement."
