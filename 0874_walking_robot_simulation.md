# 874. Walking Robot Simulation

## 🔗 Problem Link
https://leetcode.com/problems/walking-robot-simulation/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Hash Table, Simulation

---

## 🧩 Problem Summary

A robot on an infinite XY-plane starts at `(0, 0)` facing north. It receives a sequence of commands: `-2` (turn left 90 degrees), `-1` (turn right 90 degrees), or `1 <= k <= 9` (move forward k units, stopping if blocked by an obstacle). Return the maximum Euclidean distance squared from the origin at any point during the walk.

### 📌 Constraints
- `1 <= commands.length <= 10^4`
- `-2 <= commands[i] <= 9`, `commands[i] != 0`
- `0 <= obstacles.length <= 10^4`
- `-3 * 10^4 <= obstacles[i][0], obstacles[i][1] <= 3 * 10^4`

---

## 💭 Intuition

We simulate the robot step by step. 👉 The key optimization is storing obstacles in a set for O(1) lookup. We move one cell at a time (not k cells at once) since any cell along the path might be blocked.

---

## ⚡ Approach — Simulation with Direction Array and Obstacle Set

### 🧠 Idea

- Store obstacles as a set of tuples for O(1) membership checks.
- Use a direction array `[(0,1), (1,0), (0,-1), (-1,0)]` for North, East, South, West.
- Track current direction index; turn right = `+1 mod 4`, turn left = `-1 mod 4`.
- For move commands, step one unit at a time, checking for obstacles before each step.
- Track the maximum squared distance throughout.

---

## 💻 Code

```python
class Solution:
    def robotSim(self, commands, obstacles):
        # Store obstacles as a set of tuples for fast lookup
        obstacle_set = set(map(tuple, obstacles))

        # Directions: North, East, South, West
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        #    /\
        #  < || >
        #    \/
        x = y = 0
        direction = 0  # its the idx of the direction ===> start facing north
        max_dist = 0

        for cmd in commands:
            if cmd == -1:  # turn right
                direction = (direction + 1) % 4
            elif cmd == -2:  # turn left
                direction = (direction - 1) % 4
            else:
                dx, dy = directions[direction]

                for _ in range(cmd):
                    nx, ny = x + dx, y + dy

                    if (nx, ny) in obstacle_set:
                        break

                    x, y = nx, ny
                    max_dist = max(max_dist, x*x + y*y)

        return max_dist
```

---

## 🧠 Dry Run

### Input
```
commands = [4, -1, 3], obstacles = []
```

### Steps
```
cmd=4: direction=0 (North), move 4 steps → (0,1),(0,2),(0,3),(0,4)
  max_dist = 16
cmd=-1: turn right → direction=1 (East)
cmd=3: direction=1 (East), move 3 steps → (1,4),(2,4),(3,4)
  max_dist = max(16, 9+16) = 25
Return 25
```

---

## ⏱️ Time Complexity

```
O(n + k)
```

Where n is the number of commands and k is the total steps taken (sum of all move commands, at most 9 * n).

---

## 💾 Space Complexity

```
O(m)
```

Where m is the number of obstacles stored in the set.

---

## ⚠️ Edge Cases

- **No commands:** Robot stays at origin → 0
- **Blocked immediately:** Obstacle at (0,1) and robot faces north → stays at origin
- **No obstacles:** Robot moves freely, just track max distance

---

## 🎯 Interview Takeaways

- Use a set for obstacle lookup — converting a list of coordinates to a set of tuples is O(m).
- Direction arrays with modular arithmetic are the standard way to handle NSEW movement.
- Move one step at a time when obstacles can block mid-path.
- Track the answer (max distance) during simulation, not just at the end.

---

## 📌 Key Pattern

👉 **"Simulate grid movement with direction array, obstacle set, and step-by-step advancement"**

---

## 🔁 Related Problems

- 657. Robot Return to Origin
- 1041. Robot Bounded In Circle
- 2120. Execution of All Suffix Instructions Staying in a Grid

---

## 🚀 Final Thoughts

A good simulation problem that tests direction handling and efficient obstacle checking. The direction array pattern with modular arithmetic is reusable across many grid problems.

---

✨ **Rule to remember:**
> When obstacles can block mid-path, always move one step at a time and check before each step.
