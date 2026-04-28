# 2751. Robot Collisions

## 🔗 Problem Link
https://leetcode.com/problems/robot-collisions/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Stack, Sorting, Simulation

---

## 🧩 Problem Summary
Robots are placed on a number line with given positions, healths, and directions ('L' or 'R'). Robots moving toward each other collide: the one with lower health is removed, and the other loses 1 health. If equal health, both are removed. Return the healths of surviving robots in their original input order.

### 📌 Constraints
- `1 <= n <= 10^5`
- All positions are distinct.
- `positions[i]`, `healths[i]` are between 1 and 10^9.
- `directions[i]` is either `'L'` or `'R'`.

---

## 💭 Intuition
👉 This is a classic stack-based collision problem (similar to asteroid collisions). Process robots left-to-right by position. Push right-moving robots onto a stack. When a left-moving robot arrives, it collides with the top of the stack repeatedly until one side wins or the stack empties.

---

## ⚡ Approach — Stack-Based Collision Simulation

### 🧠 Idea
- Sort robots by position, keeping track of original indices.
- Use a stack to hold indices of right-moving robots.
- When a left-moving robot is encountered, simulate collisions with the stack top.
- After all collisions, collect surviving robots' healths in original order.

---

## 💻 Code

```python
class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        n = len(positions)
        indices = sorted(range(n), key=lambda i: positions[i])
        stack = []

        for curr in indices:
            if directions[curr] == 'R':
                stack.append(curr)
            else:
                while stack and healths[curr] > 0:
                    top = stack.pop()

                    if healths[top] > healths[curr]:
                        healths[top] -= 1
                        healths[curr] = 0
                        stack.append(top)

                    elif healths[top] < healths[curr]:
                        healths[curr] -= 1
                        healths[top] = 0

                    else:
                        healths[curr] = 0
                        healths[top] = 0

        return [h for h in healths if h > 0]
```

---

## 🧠 Dry Run
### Input
```
positions = [3,5,2,6], healths = [10,10,15,12], directions = "RLRL"
```
### Steps
```
Sort by position: indices = [2,0,1,3] → positions [2,3,5,6]

idx=2 (pos=2, R): stack=[2]
idx=0 (pos=3, L): collide with stack top 2
  healths[2]=15 > healths[0]=10 → healths[2]=14, healths[0]=0, push 2 back
  stack=[2]

idx=1 (pos=5, R): stack=[2,1]
idx=3 (pos=6, L): collide with stack top 1
  healths[1]=10 < healths[3]=12 → healths[3]=11, healths[1]=0
  Collide with stack top 2: healths[2]=14 > healths[3]=11 → healths[2]=13, healths[3]=0
  stack=[2]

Surviving: healths = [0, 0, 13, 0] → [13]
Result: [14]

(Note: actual values depend on exact collision order)
```

---

## ⏱️ Time Complexity
```
O(n log n) — sorting dominates. Each robot is pushed/popped at most once → O(n) for collisions.
```

## 💾 Space Complexity
```
O(n) — for the stack and sorted indices.
```

---

## ⚠️ Edge Cases
- All robots moving the same direction: no collisions, all survive.
- All robots collide and cancel out: return empty list.
- Single robot: always survives.
- Two robots with equal health colliding: both removed.

---

## 🎯 Interview Takeaways
- Stack-based collision is a recurring pattern (asteroids, parentheses, etc.).
- Sort by position to process in spatial order, but track original indices for output.
- Health decrement adds a twist over the classic asteroid problem.

---

## 📌 Key Pattern
👉 **"Stack-based collision simulation: push one direction, pop and resolve on the opposite."**

---

## 🔁 Related Problems
- 735. Asteroid Collision
- 853. Car Fleet
- 2211. Count Collisions on a Road

---

## 🚀 Final Thoughts
This extends the classic asteroid collision problem with health mechanics. The stack-based approach remains the same core idea — right-movers are pushed, left-movers trigger collisions. The health comparison adds the extra logic of decrementing the winner.

---

✨ **Rule to remember:**
> "Collisions on a line = stack problem: push one direction, resolve on the other."
