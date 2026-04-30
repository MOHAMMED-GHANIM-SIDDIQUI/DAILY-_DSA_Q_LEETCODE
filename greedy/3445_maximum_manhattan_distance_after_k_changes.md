# 3445. Maximum Manhattan Distance After K Changes

## 🔗 Problem Link
https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/

## ⚡ Difficulty
Medium

## 🏷️ Topics
String, Greedy

---

## 🧩 Problem Summary
Given a string s and an integer k, a robot starts at the origin and moves in cardinal directions (N, S, E, W) based on the characters in s. You can flip at most k moves (change the direction of k characters). Find the maximum Manhattan distance from the origin after all moves.

### 📌 Constraints
- 1 <= s.length <= 10^5
- s consists of 'N', 'S', 'E', 'W'
- 0 <= k <= s.length

---

## 💭 Intuition
👉 The Manhattan distance decomposes into |x| + |y|. Maximizing it means maximizing displacement in one diagonal direction. Try all 4 diagonal directions (NE, NW, SE, SW) and for each, greedily flip opposite moves to favorable ones.

---

## ⚡ Approach — Greedy Flip per Direction

### 🧠 Idea
- For each of the 4 diagonal directions (e.g., "NE"), a move is "positive" if it matches N or E, otherwise "negative."
- Track the net positive count and how many opposite moves we've seen.
- At each step, the best achievable distance is pos + 2 * min(k, opposite) — flipping up to k opposite moves.
- Return the maximum across all 4 directions.

---

## 💻 Code

```cpp
class Solution {
 public:
  int maxDistance(string s, int k) {
    return max({flip(s, k, "NE"), flip(s, k, "NW"),  //
                flip(s, k, "SE"), flip(s, k, "SW")});
  }

 private:
  int flip(const string& s, int k, const string& direction) {
    int res = 0;
    int pos = 0;
    int opposite = 0;

    for (const char c : s) {
      if (direction.find(c) != string::npos) {
        ++pos;
      } else {
        --pos;
        ++opposite;
      }
      res = max(res, pos + 2 * min(k, opposite));
    }

    return res;
  }
};
```

---

## 🧠 Dry Run
### Input
```
s = "NWSE", k = 1
```
### Steps
```
Direction "NE":
  N: pos=1, opp=0, res=max(0, 1+0)=1
  W: pos=0, opp=1, res=max(1, 0+2*min(1,1))=2
  S: pos=-1, opp=2, res=max(2, -1+2*min(1,2))=max(2,1)=2
  E: pos=0, opp=2, res=max(2, 0+2*min(1,2))=2

Direction "NW":
  N: pos=1, opp=0, res=1
  W: pos=2, opp=0, res=2
  S: pos=1, opp=1, res=max(2, 1+2)=3
  E: pos=0, opp=2, res=max(3, 0+2)=3

Max across all directions: 3
```

---

## ⏱️ Time Complexity
```
O(n) — 4 passes through the string (constant factor)
```

## 💾 Space Complexity
```
O(1) — constant extra space
```

---

## ⚠️ Edge Cases
- k = 0 → no flips, regular Manhattan distance
- k >= n → can flip all moves, maximum distance = n
- All moves in the same direction → no need to flip, distance = n

---

## 🎯 Interview Takeaways
- Manhattan distance naturally decomposes into diagonal directions.
- Flipping a move from negative to positive direction gains +2 distance.
- Trying all 4 diagonal directions covers all cases.

---

## 📌 Key Pattern
👉 **"Greedy direction flipping with Manhattan distance decomposition"**

---

## 🔁 Related Problems
- 1266. Minimum Time Visiting All Points
- 657. Robot Return to Origin

---

## 🚀 Final Thoughts
The key insight is decomposing Manhattan distance into 4 diagonal directions and greedily flipping the most impactful opposite moves. Each direction is processed independently in O(n).

---

✨ **Rule to remember:**
> For maximum Manhattan distance with flips, try all 4 diagonal directions and greedily flip opposite moves.
