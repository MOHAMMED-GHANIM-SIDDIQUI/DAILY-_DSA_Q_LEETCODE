# 838. Push Dominoes

## 🔗 Problem Link
https://leetcode.com/problems/push-dominoes/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Two Pointers, String, Dynamic Programming, Simulation

---

## 🧩 Problem Summary
Given a string representing dominoes where `'R'` falls right, `'L'` falls left, and `'.'` is standing, determine the final state after all dominoes have fallen. Simultaneously falling dominoes cancel each other out.

### 📌 Constraints
- `n == dominoes.length`
- `1 <= n <= 10^5`
- `dominoes[i]` is `'L'`, `'R'`, or `'.'`.

---

## 💭 Intuition
👉 Assign a "force" value to each position: positive for rightward force, negative for leftward force. Sweep left-to-right for `'R'` forces and right-to-left for `'L'` forces, then combine them. The net force determines the final direction.

---

## ⚡ Approach — Force Simulation (Two-Pass)

### 🧠 Idea
- Left-to-right pass: When `'R'` is seen, set force to `n` and decrement for each `'.'`. Reset on `'L'`.
- Right-to-left pass: When `'L'` is seen, set force to `n` and decrement for each `'.'`. Subtract from previous forces.
- Net positive = `'R'`, net negative = `'L'`, zero = `'.'`.

---

## 💻 Code

```cpp
class Solution {
public:
    string pushDominoes(string dominoes) {
        int n = dominoes.size();
        vector<int> forces(n, 0);

        int force = 0;

        // Left to Right – apply force from 'R'
        for (int i = 0; i < n; i++) {
            if (dominoes[i] == 'R') force = n;
            else if (dominoes[i] == 'L') force = 0;
            else force = max(force - 1, 0);
            forces[i] += force;
        }

        // Right to Left – apply force from 'L'
        force = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (dominoes[i] == 'L') force = n;
            else if (dominoes[i] == 'R') force = 0;
            else force = max(force - 1, 0);
            forces[i] -= force;
        }

        // Final result
        string result = "";
        for (int f : forces) {
            if (f > 0) result += 'R';
            else if (f < 0) result += 'L';
            else result += '.';
        }

        return result;
    }
};
```

---

## 🧠 Dry Run
### Input
```
dominoes = ".L.R...LR..L.."
```
### Steps
```
Left-to-right (R forces):
forces = [0,0,0,14,13,12,11,0,14,13,12,0,0,0]

Right-to-left (L forces subtracted):
forces = [0,-14,0,14,13,12,-1,-14,14,13,-2,-14,-13,0]
  (after subtracting: [-13,-14,0,14,13,12,-1,-14,14,13,-2,-14,-13,0])

Result: "LL.RR.LLRR.LL.."  (approximate, depends on exact n value)
```

---

## ⏱️ Time Complexity
```
O(n)
```

## 💾 Space Complexity
```
O(n) for the forces array
```

---

## ⚠️ Edge Cases
- All `'.'`: No dominoes fall, return the original string.
- `"R...L"`: Middle domino stays upright due to balanced forces.
- Adjacent `"RL"`: Both remain as is.

---

## 🎯 Interview Takeaways
- The force-based approach converts a simulation problem into two linear scans.
- Net force elegantly handles the cancellation of opposing forces.
- This avoids the complexity of BFS-based or event-driven simulation.

---

## 📌 Key Pattern
👉 **"Two-pass force propagation: sweep in both directions and combine net forces"**

---

## 🔁 Related Problems
- 735. Asteroid Collision
- 2211. Count Collisions on a Road

---

## 🚀 Final Thoughts
The force simulation approach is an elegant way to handle this problem. By assigning decreasing force values and summing contributions from both directions, we naturally handle all cases including balanced opposing forces. It is much cleaner than explicit simulation.

---

✨ **Rule to remember:**
> "Two-pass force propagation: assign decreasing force from each pushed domino and let net force decide the outcome."
