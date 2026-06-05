# 3751. Total Waviness

## 🔗 Problem Link
https://leetcode.com/problems/total-waviness/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Math

---

## 🧩 Problem Summary
The **waviness** of a number is the count of its digit positions (excluding the first and last digit) that are a **local extremum** — i.e. a digit strictly greater than **both** neighbours (a "peak") or strictly less than **both** neighbours (a "valley"). Given `num1` and `num2`, return the **sum of waviness** over every integer in the inclusive range `[num1, num2]`.

### 📌 Constraints
- `1 <= num1 <= num2` (range small enough for a direct sweep in this version; the digit-DP version handles wide ranges).

---

## 💭 Intuition
For a single number, "waviness" is a straightforward middle-digit scan: a digit at position `i` (with `0 < i < n-1`) is wavy if it's a strict local max or strict local min of the triple `(s[i-1], s[i], s[i+1])`. Numbers with fewer than 3 digits have waviness `0` (no interior position).

When the range `[num1, num2]` is small, the honest approach is to **brute-force every number** and sum the per-number waviness. (For very large ranges this becomes a digit-DP counting how many numbers have each interior local-extremum — but the brute force is the clean, correct baseline.)

---

## ⚡ Approach — Per-number wavy-digit count over the range

### 🧠 Idea
1. `waviness(x)`:
   - Convert to string `s`; if `len(s) < 3` return `0`.
   - For each interior index `i` in `1 .. n-2`, check if `s[i]` is strictly greater than both neighbours (peak) **or** strictly less than both (valley); count those.
2. Sum `waviness(x)` for `x` in `[num1, num2]`.

### 🔑 Why strict comparisons
A plateau (`s[i] == s[i-1]`) is **not** an extremum — equality on either side disqualifies the position. Hence both branches use strict `>` / `<` on **both** sides.

---

## 💻 Code

```python
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def waviness(x: int) -> int:
            s = str(x)
            n = len(s)

            if n < 3:
                return 0

            cnt = 0
            for i in range(1, n - 1):
                if (s[i] > s[i - 1] and s[i] > s[i + 1]) or (s[i] < s[i - 1] and s[i] < s[i + 1]):
                    cnt += 1
            return cnt

        return sum(waviness(x) for x in range(num1, num2 + 1))
```
> Note: character comparison (`s[i] > s[i-1]`) works because digit characters `'0'..'9'` order the same as their numeric values.

---

## 🧠 Dry Run
### Input
```
num1 = 120, num2 = 122
```

### Per number
```
120 → digits 1,2,0 → middle '2': 2>1 and 2>0 → peak → waviness 1
121 → 1,2,1 → '2': 2>1 and 2>1 → peak → 1
122 → 1,2,2 → '2': 2>1 but 2>2 false; valley? 2<1 false → 0
```
Total = `1 + 1 + 0 = 2`.

---

## ⏱️ Time Complexity
```
O((num2 - num1 + 1) · D)   — D digits per number; D ≤ ~10.
                             Fine when the range is small.
```

## 💾 Space Complexity
```
O(D)   — the string form of one number at a time.
```

---

## ⚠️ Edge Cases
- **Numbers with < 3 digits** (`1..99`) → contribute `0`.
- **Monotonic digits** (`123`, `321`) → no interior extremum → `0`.
- **Plateaus** (`122`, `112`) → equality blocks the extremum, strict checks handle it.
- **Single-number range** (`num1 == num2`) → just that number's waviness.

---

## 🎯 Interview Takeaways
- The per-number logic is the same "local peak/valley" scan as hills-and-valleys array problems — only the input is a digit string.
- Brute force is correct and simple for small ranges; flag that wide ranges demand **digit DP** over `(position, prev_digit, prev_relation)` to count interior extrema without enumerating — a strong follow-up answer.
- Strictness on **both** sides is the subtle correctness point; plateaus are the classic bug.

---

## 📌 Key Pattern
👉 **"Interior digit is wavy ⇔ strict local max OR strict local min of its triple. Sum over the range (brute force small, digit-DP large)."**

---

## 🔁 Related Problems
- 2210. Count Hills and Valleys in an Array
- 845. Longest Mountain in Array
- 1671. Minimum Number of Removals to Make Mountain Array
- 233. Number of Digit One

---

## 🚀 Final Thoughts
At heart this is "count hills and valleys," applied to the digits of each number and summed across a range. The brute force nails correctness; the interesting interview depth is recognising when the range forces a digit-DP reformulation.

---

✨ **Rule to remember:**
> A wavy interior digit is a strict local extremum of its 3-digit window. Sum per-number for small ranges; switch to digit DP when the range is too wide to enumerate.
