# 657. Robot Return to Origin

## 🔗 Problem Link
https://leetcode.com/problems/robot-return-to-origin/

## ⚡ Difficulty
Easy

## 🏷️ Topics
String, Simulation

---

## 🧩 Problem Summary

There is a robot starting at the origin `(0, 0)` on a 2D plane. Given a string `moves` consisting of characters `'U'`, `'D'`, `'L'`, and `'R'`, determine if the robot returns to the origin after completing all its moves.

### 📌 Constraints
- `1 <= moves.length <= 2 * 10^4`
- `moves` only contains the characters `'U'`, `'D'`, `'L'`, and `'R'`

---

## 💭 Intuition

The robot returns to the origin only if every left move is balanced by a right move and every up move is balanced by a down move. 👉 We just need to track horizontal and vertical displacement and check if both are zero at the end.

---

## ⚡ Approach — Counter / Balance Tracking

### 🧠 Idea

- Maintain two counters: one for vertical displacement and one for horizontal displacement.
- Increment or decrement based on the direction of each move.
- At the end, if both counters are zero the robot is back at the origin.

---

## 💻 Code

```python
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        vertical_bal = 0
        horizontal_bal = 0
        for move in moves:
          if move =='L':
            horizontal_bal-=1
          elif move =='R':
            horizontal_bal+=1
          elif move =='U':
            vertical_bal+=1
          else:
            vertical_bal-=1
        return vertical_bal ==  horizontal_bal == 0
```

---

## 🧠 Dry Run

### Input
```
moves = "UD"
```

### Steps
```
move = 'U' → vertical_bal = 1, horizontal_bal = 0
move = 'D' → vertical_bal = 0, horizontal_bal = 0
Return: 0 == 0 == 0 → True
```

---

## ⏱️ Time Complexity

```
O(n)
```

We iterate through the moves string once, where n is the length of the string.

---

## 💾 Space Complexity

```
O(1)
```

Only two integer counters are used regardless of input size.

---

## ⚠️ Edge Cases

- **All same direction:** `"LLLL"` → `False` (horizontal_bal = -4)
- **Empty-like balanced:** `"LRUD"` → `True` (all directions cancel out)
- **Single move:** `"U"` → `False`

---

## 🎯 Interview Takeaways

- Simple simulation problems can often be solved with counters.
- The chained comparison `a == b == 0` in Python checks both values equal zero.
- Always think about what "returning to origin" means mathematically: net displacement = 0 in both axes.

---

## 📌 Key Pattern

👉 **"Track net displacement using counters for each axis"**

---

## 🔁 Related Problems

- 1041. Robot Bounded In Circle
- 874. Walking Robot Simulation
- 2120. Execution of All Suffix Instructions Staying in a Grid

---

## 🚀 Final Thoughts

A straightforward simulation problem. The key insight is that returning to the origin simply means the count of opposing moves must match.

---

✨ **Rule to remember:**
> A robot returns to origin if and only if L cancels R and U cancels D — just count them.
