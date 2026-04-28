# 2410. Maximum Matching of Players With Trainers

## 🔗 Problem Link
https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Two Pointers, Greedy, Sorting

---

## 🧩 Problem Summary
Given arrays `players` (abilities) and `trainers` (capacities), match each player to at most one trainer such that the player's ability does not exceed the trainer's capacity. Return the maximum number of matchings.

### 📌 Constraints
- `1 <= players.length, trainers.length <= 10^5`
- `1 <= players[i], trainers[j] <= 10^9`

---

## 💭 Intuition
👉 Sort both arrays. Greedily assign the smallest available trainer to the smallest unmatched player. If a trainer can handle the current player, match them; otherwise, try the next trainer.

---

## ⚡ Approach — Greedy with Sorting

### 🧠 Idea
- Sort both `players` and `trainers`.
- Use a pointer for players (`ans`) and iterate through trainers.
- If the current trainer's capacity >= current player's ability, increment the match count.
- Stop when all players are matched or all trainers are exhausted.

---

## 💻 Code

```cpp
class Solution {
 public:
  int matchPlayersAndTrainers(vector<int>& players, vector<int>& trainers) {
    int ans = 0;

    ranges::sort(players);
    ranges::sort(trainers);

    for (int i = 0; i < trainers.size(); ++i)
      if (players[ans] <= trainers[i] && ++ans == players.size())
        return ans;

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
players = [4,7,9], trainers = [8,2,5,8]
```
### Steps
```
Sort players: [4,7,9], trainers: [2,5,8,8]
ans = 0
i=0: trainers[0]=2, players[0]=4 → 4 > 2, skip
i=1: trainers[1]=5, players[0]=4 → 4 <= 5, ans=1
i=2: trainers[2]=8, players[1]=7 → 7 <= 8, ans=2
i=3: trainers[3]=8, players[2]=9 → 9 > 8, skip

Result: 2
```

---

## ⏱️ Time Complexity
```
O(n log n + m log m) where n = players.length, m = trainers.length. Dominated by sorting.
```

## 💾 Space Complexity
```
O(1) — sorting in-place (ignoring sort's internal space).
```

---

## ⚠️ Edge Cases
- All trainers are too weak for any player: answer is 0.
- All players can be matched.
- Players and trainers arrays have very different sizes.

---

## 🎯 Interview Takeaways
- Sort + greedy is the standard approach for assignment/matching problems.
- Matching the smallest player to the smallest capable trainer is optimal.
- Early termination when all players are matched saves time.

---

## 📌 Key Pattern
👉 **"Sort both sides, greedily match smallest to smallest — classic assignment pattern."**

---

## 🔁 Related Problems
- 455. Assign Cookies
- 881. Boats to Save People
- 2592. Maximize Greatness of an Array

---

## 🚀 Final Thoughts
This is essentially the same problem as "Assign Cookies" (LeetCode 455). Sort both arrays and greedily match. The compact loop with early return makes the solution elegant.

---

✨ **Rule to remember:**
> "Sort both, match greedily from smallest — the classic two-pointer assignment."
