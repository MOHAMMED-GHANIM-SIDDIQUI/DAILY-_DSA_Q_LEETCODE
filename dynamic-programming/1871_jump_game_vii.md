# 1871. Jump Game VII

## 🔗 Problem Link
https://leetcode.com/problems/jump-game-vii/

## ⚡ Difficulty
Medium

## 🏷️ Topics
String, Dynamic Programming, Prefix Sum, Sliding Window

---

## 🧩 Problem Summary
You are given a binary string `s` and two integers `minJump` and `maxJump`. You start at index `0` (guaranteed `s[0] == '0'`). From index `i` you may jump to index `j` if **all** of:
- `i + minJump <= j <= min(i + maxJump, n - 1)`, and
- `s[j] == '0'`.

Return `True` if you can reach the **last** index `n - 1`.

### 📌 Constraints
- `2 <= s.length <= 10^5`
- `s[i]` is `'0'` or `'1'`
- `s[0] == '0'`
- `1 <= minJump <= maxJump < s.length`

---

## 💭 Intuition
Let `f[i] = 1` if index `i` is **reachable**. Then:

> `f[i] = 1` iff `s[i] == '0'` and there exists some reachable `j` in the window `[i - maxJump, i - minJump]`.

So index `i` is reachable when **at least one** position in a fixed-width window behind it is reachable. "Is there a reachable index in `[L, R]`?" is a **range-sum > 0** query over `f`. Maintaining a **prefix sum** `pre` of `f` answers each window in `O(1)`, giving an `O(n)` DP. (This is the prefix-sum / sliding-window optimisation of the naive `O(n·(maxJump-minJump))` DP.)

---

## ⚡ Approach — Reachability DP + prefix-sum window

### 🧠 Idea
1. `f[0] = 1` (start). `pre[i]` = `f[0] + f[1] + ... + f[i]`.
2. Seed `pre[i] = 1` for `i` in `[0, minJump-1]` — only index 0 is reachable there, so the running prefix is 1 across that span (no index in that range can be a *landing* spot from 0, since the minimum jump is `minJump`).
3. For `i` from `minJump` to `n-1`:
   - Window of possible predecessors: `left = i - maxJump`, `right = i - minJump`.
   - If `s[i] == '0'`, count reachable predecessors in `[left, right]` via prefix sums:
     `total = pre[right] - (pre[left-1] if left > 0 else 0)`.
     `f[i] = 1` iff `total != 0`.
   - Update `pre[i] = pre[i-1] + f[i]`.
4. Return `bool(f[n-1])`.

### 🔑 Why prefix sums
The predecessor window slides by one each step but the question is always "any reachable index inside it?" — a range sum. Prefix sums turn each range sum into a constant-time subtraction, so the whole DP is linear instead of quadratic.

---

## 💻 Code

```python
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        f, pre = [0] * n, [0] * n
        f[0] = 1
        for i in range(minJump):
            pre[i] = 1
        for i in range(minJump, n):
            left, right = i - maxJump, i - minJump
            if s[i] == "0":
                total = pre[right] - (0 if left <= 0 else pre[left - 1])
                f[i] = int(total != 0)
            pre[i] = pre[i - 1] + f[i]
        return bool(f[n - 1])
```

---

## 🧠 Dry Run
### Input
```
s = "011010", minJump = 2, maxJump = 3
index: 0 1 2 3 4 5
```

### Setup
```
f[0]=1
pre[0..1] = 1, 1   (minJump=2 → fill i in [0,1])
```

### Loop
```
i=2: s='1' → f[2]=0; pre[2]=pre[1]+0=1
i=3: s='0', window [0,1]: total=pre[1]-0=1 → f[3]=1; pre[3]=1+1=2
i=4: s='1' → f[4]=0; pre[4]=2
i=5: s='0', window [2,3]: total=pre[3]-pre[1]=2-1=1 → f[5]=1; pre[5]=3
```
`f[5] = 1` → `True`.

---

## ⏱️ Time Complexity
```
O(n)   — single pass; each window query is O(1) via prefix sums.
```

## 💾 Space Complexity
```
O(n)   — the f[] and pre[] arrays (prefix can be folded into one array if desired).
```

---

## ⚠️ Edge Cases
- **`s[n-1] == '1'`** → last index can never be a landing spot → `False`.
- **`left < 0`** → clamp: treat `pre[left-1]` as `0` (window starts at index 0).
- **Window entirely before reachable region** → `total == 0`, index stays unreachable.
- **minJump == maxJump** → window is a single index; still handled by the same range formula.
- The `pre` seeding for `[0, minJump-1]` encodes that only index 0 contributes there.

---

## 🎯 Interview Takeaways
- The naive DP is `f[i] = OR over j in [i-maxJump, i-minJump] of f[j]` — `O(n·k)`. The interviewer wants you to spot that the OR-over-a-window is a **range existence** query and optimise with **prefix sums** (or a sliding-window count, or a monotonic deque).
- Equivalent sliding-window phrasing: keep a running count of reachable indices entering/leaving the `[i-maxJump, i-minJump]` window — same `O(n)`, sometimes cleaner.
- Careful index bookkeeping (the `left <= 0` clamp, the `[0, minJump-1]` seed) is where bugs hide; the dry run is worth doing on paper.

---

## 📌 Key Pattern
👉 **"Reachability DP where each state depends on 'any true state in a sliding window' → convert the windowed OR into a prefix-sum range query for O(n)."**

---

## 🔁 Related Problems
- 55. Jump Game
- 45. Jump Game II
- 1306. Jump Game III
- 1345. Jump Game IV
- 1696. Jump Game VI

---

## 🚀 Final Thoughts
The reachability recurrence is obvious; the craft is realising "does any reachable index sit in this back-window?" is a range-sum, and prefix sums answer it in `O(1)`. That single optimisation drops the solution from quadratic to linear and is the whole point of the problem.

---

✨ **Rule to remember:**
> When a DP transition is "true if any earlier state in a fixed window is true," don't loop the window — maintain a prefix sum (or sliding-window count) and test whether the range total is positive.
