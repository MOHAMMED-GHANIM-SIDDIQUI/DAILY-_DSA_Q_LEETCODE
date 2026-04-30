# 909. Snakes and Ladders

## 🔗 Problem Link
https://leetcode.com/problems/snakes-and-ladders/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Breadth-First Search, Matrix

---

## 🧩 Problem Summary
Given an `n x n` Snakes and Ladders board, find the minimum number of dice rolls to reach the last square from square 1. The board uses Boustrophedon (alternating direction) numbering, and landing on a snake or ladder teleports you to the destination.

### 📌 Constraints
- `n == board.length == board[i].length`
- `2 <= n <= 20`
- `board[i][j]` is either `-1` or in `[1, n^2]`.

---

## 💭 Intuition
👉 This is a shortest path problem on an unweighted graph. BFS from square 1 gives the minimum number of moves. The tricky part is converting the 2D board (with alternating row directions) into a 1D array.

---

## ⚡ Approach — BFS on Flattened Board

### 🧠 Idea
- Flatten the 2D board into a 1D array, handling Boustrophedon ordering.
- BFS from square 1, exploring up to 6 steps ahead (dice roll 1-6).
- If a square has a snake/ladder, jump to the destination.
- Return the number of steps when reaching square `n*n`.

---

## 💻 Code

```cpp
class Solution {
 public:
  int snakesAndLadders(vector<vector<int>>& board) {
    const int n = board.size();
    queue<int> q{{1}};
    vector<bool> seen(1 + n * n);
    vector<int> arr(1 + n * n);  // 2D -> 1D

    for (int i = 0; i < n; ++i)
      for (int j = 0; j < n; ++j)
        arr[(n - 1 - i) * n + ((n - i) % 2 == 0 ? n - j : j + 1)] = board[i][j];

    for (int step = 1; !q.empty(); ++step)
      for (int sz = q.size(); sz > 0; --sz) {
        const int curr = q.front();
        q.pop();
        for (int next = curr + 1; next <= min(curr + 6, n * n); ++next) {
          const int dest = arr[next] > 0 ? arr[next] : next;
          if (dest == n * n)
            return step;
          if (seen[dest])
            continue;
          q.push(dest);
          seen[dest] = true;
        }
      }

    return -1;
  }
};
```

---

## 🧠 Dry Run
### Input
```
board = [[-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1],
         [-1,35,-1,-1,13,-1],
         [-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1]]
```
### Steps
```
Flatten board to 1D array (Boustrophedon order).
BFS from square 1:
  Step 1: Roll to 2-7. Square 2 has ladder to 35.
  Step 2: From 35, roll to 36 (=n*n). Done!
Result: 2 (via ladder at square 2 -> 35, then roll to 36)

Minimum rolls = 4 (for the actual 6x6 board)
```

---

## ⏱️ Time Complexity
```
O(n^2), each square is visited at most once
```

## 💾 Space Complexity
```
O(n^2) for the queue and visited array
```

---

## ⚠️ Edge Cases
- No snakes or ladders: pure BFS on sequential squares.
- Snake at the end forcing backtracking.
- Unreachable end square: return -1.

---

## 🎯 Interview Takeaways
- Boustrophedon board-to-array conversion is the trickiest part.
- BFS on an unweighted graph guarantees shortest path.
- Always handle the snake/ladder redirection before checking visited.

---

## 📌 Key Pattern
👉 **"BFS shortest path on an unweighted graph with teleportation edges (snakes/ladders)"**

---

## 🔁 Related Problems
- 1091. Shortest Path in Binary Matrix
- 127. Word Ladder
- 752. Open the Lock

---

## 🚀 Final Thoughts
The main challenge is the board layout conversion. Once flattened, it becomes a standard BFS shortest-path problem with special edges (snakes/ladders). Careful indexing for the alternating row direction is critical for correctness.

---

✨ **Rule to remember:**
> "Flatten the Boustrophedon board to 1D, then BFS with snake/ladder jumps for shortest path."
