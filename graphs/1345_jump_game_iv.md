# 1345. Jump Game IV

## 🔗 Problem Link
https://leetcode.com/problems/jump-game-iv/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Hash Table, Breadth-First Search

---

## 🧩 Problem Summary
Given an array `arr`, starting at index `0`, in one step from index `i` you may move to:
- `i + 1` (if in bounds),
- `i - 1` (if in bounds), or
- any index `j` where `arr[j] == arr[i]` (same value).

Return the **minimum number of steps** to reach the **last index** `n - 1`.

### 📌 Constraints
- `1 <= arr.length <= 5 * 10^4`
- `-10^8 <= arr[i] <= 10^8`

---

## 💭 Intuition
"Minimum number of steps where every move costs 1" on an **unweighted** graph → **BFS** gives shortest path. Each index is a node; edges are `i±1` plus teleports to all indices sharing the same value.

The danger is the value-edges: a value appearing `k` times creates a `k`-clique, and naively re-expanding it every visit is `O(k²)` and can blow up (e.g. an array of all equal values). The crucial optimisation: once you've used the value-group of `arr[i]`, **clear that group** so it's never expanded again. After the first time you stand on some value `v`, BFS has already enqueued *all* indices with value `v`; revisiting that group later can never give a shorter path, so we drop it.

---

## ⚡ Approach — BFS with value-group clearing

### 🧠 Idea
1. If `n == 1`, we're already at the end → `0` steps.
2. Build `graph: value → list of all indices with that value`.
3. BFS from index `0`, level by level, tracking `steps`:
   - Pop index `i`. If `i == n-1`, return `steps`.
   - Neighbours = `graph[arr[i]]` (all same-value indices) **plus** `i-1`, `i+1`.
   - Enqueue every unvisited neighbour, marking visited.
   - **Clear `graph[arr[i]]`** after expanding — this value's clique is fully processed.
4. Increment `steps` after each BFS level.

### 🔑 Why clearing the group is safe *and* necessary
- **Safe**: the first time any index of value `v` is dequeued, all other `v`-indices are enqueued in that same step. They're now at the minimal distance BFS will ever assign them. Expanding the group again later only revisits nodes already (or about to be) visited — never shorter.
- **Necessary**: without it, an array like `[7,7,7,...,7,11]` re-scans the whole 7-clique from every node → `O(n²)` and TLE. Clearing makes each value-edge set processed once total → `O(n)`.

---

## 💻 Code

```python
from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr):
        n = len(arr)

        if n == 1:
            return 0

        # value -> all indices having that value
        graph = defaultdict(list)
        for i, v in enumerate(arr):
            graph[v].append(i)

        q = deque([0])
        visited = {0}
        steps = 0

        while q:
            for _ in range(len(q)):
                i = q.popleft()

                if i == n - 1:
                    return steps

                # all possible next jumps
                neighbors = graph[arr[i]] + [i - 1, i + 1]

                for nxt in neighbors:
                    if 0 <= nxt < n and nxt not in visited:
                        visited.add(nxt)
                        q.append(nxt)

                # Important optimization:
                # don't process same value again
                graph[arr[i]].clear()

            steps += 1

        return -1
```

---

## 🧠 Dry Run
### Input
```
arr = [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]
                                                  ↑ index 9 = target
```

### BFS
```
steps=0: q=[0]
  i=0 (val 100): neighbors = indices{0,4} + {-1,1}
       enqueue 4 (val 100 teleport), 1; clear group[100]
       visited={0,4,1}
steps=1: q=[4,1]
  i=4 (val 100, group already cleared): neighbors = [] + {3,5}
       enqueue 3, 5; clear (empty)
  i=1 (val -23): neighbors = {1,2} + {0,2}
       enqueue 2; clear group[-23]
       q=[3,5,2]
steps=2: q=[3,5,2]
  i=3 (val 404): group{3,9} + {2,4} → enqueue 9 ✅
       9 == n-1 will be detected next level
       ...
steps=3: i=9 → return 3
```
Answer: `3`.

---

## ⏱️ Time Complexity
```
O(n)   — each index enqueued once; each value-group's edges expanded once total
         thanks to clearing. The `+1/-1` edges are O(1) per node.
```

## 💾 Space Complexity
```
O(n)   — graph map, visited set, and BFS queue.
```

---

## ⚠️ Edge Cases
- **Single element** → answer `0` (handled up front).
- **All identical values** (`[7,7,...,7]`) → one teleport from index 0 reaches the last → `1` step; clearing prevents `O(n²)`.
- **No teleports useful** (all distinct) → degenerates to `i±1`, answer `n-1`.
- **Target reachable by step ±1 only** → standard BFS handles it.
- Marking `visited` **at enqueue time** (not dequeue) prevents the same node being queued twice.

---

## 🎯 Interview Takeaways
- "Minimum steps, unit cost" is the canonical BFS flag — not DP, not Dijkstra.
- The make-or-break detail is the value-group clearing; without it this is a correct-but-TLE solution. Stating *why* it's safe (BFS enqueues the whole clique on first contact) is what separates a pass from a fail.
- An equivalent trick is to delete the value key from `graph` after first use. Either way: **each value's edges are consumed once.**
- This is the BFS sibling of **1306 (Jump Game III)** — same implicit-graph reachability, but here we need the *shortest* path, so BFS over DFS.

---

## 📌 Key Pattern
👉 **"Shortest path on an unweighted implicit graph → BFS. When a node has a large 'same-attribute' clique, expand that clique once and clear it to stay linear."**

---

## 🔁 Related Problems
- 1306. Jump Game III
- 815. Bus Routes
- 127. Word Ladder
- 1654. Minimum Jumps to Reach Home
- 752. Open the Lock

---

## 🚀 Final Thoughts
The graph here is huge only because of value-cliques, and the single optimisation — process each clique once, then erase it — is what turns a quadratic blow-up into clean linear BFS. Recognise the shortest-path-on-unit-edges shape, then defend the clearing step.

---

✨ **Rule to remember:**
> Min-steps with unit moves ⇒ BFS. If a value/attribute links many nodes into a clique, expand it exactly once and clear it — otherwise the same edges get re-walked and the search degrades to O(n²).
