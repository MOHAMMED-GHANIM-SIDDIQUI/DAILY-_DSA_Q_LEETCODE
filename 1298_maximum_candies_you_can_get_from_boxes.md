# 1298. Maximum Candies You Can Get From Boxes

## 🔗 Problem Link
https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, BFS, Graph

---

## 🧩 Problem Summary

You are given boxes, each of which may be open or closed, contain candies, hold keys to other boxes, and contain other boxes. Starting with some initial boxes, find the maximum total candies you can collect by opening boxes, using found keys, and exploring contained boxes.

### 📌 Constraints
- `n == status.length == candies.length == keys.length == containedBoxes.length`
- `1 <= n <= 1000`
- `0 <= candies[i] <= 1000`
- `0 <= keys[i].length, containedBoxes[i].length <= n`

---

## 💭 Intuition

👉 This is a BFS simulation: process boxes you can open, collect candies and keys, discover new boxes, and repeat until no more boxes can be opened.

👉 A box can be opened when you both have it AND have its key (or it's already open). Track "reached but closed" boxes separately.

---

## ⚡ Approach — BFS Simulation

### 🧠 Idea
- Use a queue for boxes ready to open (have the box + it's open/unlocked).
- Track `reachedClosedBoxes` — boxes you have but can't open yet.
- When processing a box: collect candies, use keys (which may unlock reached-but-closed boxes), and add contained boxes.
- A key unlocks a reached-but-closed box immediately into the queue.

---

## 💻 Code

```cpp
class Solution {
 public:
  int maxCandies(vector<int>& status, vector<int>& candies,
                 vector<vector<int>>& keys, vector<vector<int>>& containedBoxes,
                 vector<int>& initialBoxes) {
    int ans = 0;
    queue<int> q;
    vector<bool> reachedClosedBoxes(status.size());

    auto pushBoxesIfPossible = [&status, &q,
                                &reachedClosedBoxes](const vector<int>& boxes) {
      for (const int box : boxes)
        if (status[box])
          q.push(box);
        else
          reachedClosedBoxes[box] = true;
    };

    pushBoxesIfPossible(initialBoxes);

    while (!q.empty()) {
      const int currBox = q.front();
      q.pop();

      // Add the candies.
      ans += candies[currBox];

      // Push `reachedClosedBoxes` by `key` obtained in this turn and change
      // their statuses.
      for (const int key : keys[currBox]) {
        if (!status[key] && reachedClosedBoxes[key])
          q.push(key);
        status[key] = 1;  // boxes[key] is now open.
      }

      // Push the boxes contained in `currBox`.
      pushBoxesIfPossible(containedBoxes[currBox]);
    }

    return ans;
  }
};
```

---

## 🧠 Dry Run

### Input
```
status = [1,0,1,0], candies = [7,5,4,100]
keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]]
initialBoxes = [0]
```

### Steps
```
Initial: box 0 is open → queue = [0]

Process box 0: ans += 7 = 7
  keys[0] = [] → no new keys
  containedBoxes[0] = [1,2]
    box 1: status=0 → reachedClosed[1]=true
    box 2: status=1 → queue = [2]

Process box 2: ans += 4 = 11
  keys[2] = [1] → status[1] was 0, reachedClosed[1]=true → push box 1, status[1]=1
  containedBoxes[2] = [] → nothing
  queue = [1]

Process box 1: ans += 5 = 16
  keys[1] = [] → nothing
  containedBoxes[1] = [3]
    box 3: status=0 → reachedClosed[3]=true
  queue = []

Queue empty. No key for box 3.
Output: 16
```

---

## ⏱️ Time Complexity
```
O(n)
```
Each box is processed at most once, and each key/contained box relation is examined once.

---

## 💾 Space Complexity
```
O(n)
```
For the queue and the `reachedClosedBoxes` array.

---

## ⚠️ Edge Cases
- No initial boxes → return 0.
- All boxes are open from the start → BFS collects everything reachable.
- Circular key dependencies (A contains key for B, B contains key for A) → handled naturally by BFS.
- A box is both initial and contained in another box → processed only once since status changes.

---

## 🎯 Interview Takeaways
- This is a graph traversal problem disguised as a simulation.
- The "reached but closed" tracking is the key insight — without it, you'd miss boxes that become openable later.
- BFS naturally handles the order of operations: open a box, get keys, discover new boxes.
- Lambda functions can keep BFS logic clean and avoid code duplication.

---

## 📌 Key Pattern
👉 **"BFS with deferred processing — track items that are discovered but not yet actionable, and activate them when conditions are met."**

---

## 🔁 Related Problems
- 841 - Keys and Rooms
- 1136 - Parallel Courses
- 207 - Course Schedule

---

## 🚀 Final Thoughts
A well-designed BFS simulation problem. The critical insight is maintaining a "reached but closed" set and checking it whenever a new key is found. This two-condition activation pattern appears in many graph problems.

---

✨ **Rule to remember:**
> "When an action requires two conditions (having the box AND having the key), track each condition separately and activate when both are met."
