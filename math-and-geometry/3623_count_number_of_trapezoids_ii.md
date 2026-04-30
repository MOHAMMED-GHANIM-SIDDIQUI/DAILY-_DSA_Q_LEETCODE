# 3623. Count Number of Trapezoids II

## 🔗 Problem Link
https://leetcode.com/problems/count-number-of-trapezoids-ii/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Math, Combinatorics, Hash Map, Modular Arithmetic

---

## 🧩 Problem Summary
Given a set of 2D points, count the number of trapezoids that can be formed. A trapezoid has exactly one pair of parallel sides. Here, we count trapezoids with at least one pair of horizontal parallel sides (points sharing the same y-coordinate form horizontal segments).

### 📌 Constraints
- `1 <= points.length <= 10^5`
- Points have integer coordinates

---

## 💭 Intuition
👉 Two horizontal segments on different y-levels form a trapezoid. Count the number of horizontal segment pairs across different y-levels. For y-level with `a` points, there are C(a, 2) horizontal segments. The total trapezoid count is `(sum(C(a,2)))^2 - sum(C(a,2)^2)) / 2` — choosing two segments from different levels.

---

## ⚡ Approach — Combinatorial Counting with Modular Inverse

### 🧠 Idea
- Group points by y-coordinate and count how many are on each level.
- For each y-level with count `c`, compute `a = C(c, 2)` = number of horizontal segments.
- Total pairs of segments from different levels = `(total^2 - sumSq) / 2`, where `total = sum(a)` and `sumSq = sum(a^2)`.
- Use modular inverse of 2 for division under modulo.

---

## 💻 Code

```cpp
class Solution {
public:
    static const long long MOD = 1e9 + 7;
    static const long long INV2 = 500000004LL; // modular inverse of 2 mod MOD

    long long C2(long long k) {
        if (k < 2) return 0;
        // k*(k-1)/2 fits in 64-bit for typical constraints
        return (k * (k - 1) / 2) % MOD;
    }

    int countTrapezoids(vector<vector<int>>& points) {
        unordered_map<int, long long> cnt;
        cnt.reserve(points.size()*2);

        for (auto &p : points) {
            cnt[p[1]]++;
        }

        long long total = 0;   // sum of a_i
        long long sumsq = 0;   // sum of a_i^2

        for (auto &entry : cnt) {
            long long a = C2(entry.second); // number of horizontal segments on this y
            if (a == 0) continue;
            total = (total + a) % MOD;
            sumsq = (sumsq + (a * a) % MOD) % MOD;
        }

        // result = ((total^2 - sumsq) / 2) % MOD
        long long totalSq = (total * total) % MOD;
        long long diff = (totalSq - sumsq + MOD) % MOD;
        long long ans = (diff * INV2) % MOD;
        return (int)ans;
    }
};
```

---

## 🧠 Dry Run
### Input
```
points = [[0,0],[1,0],[0,1],[1,1],[2,1]]
```
### Steps
```
cnt: {0: 2, 1: 3}

y=0: C(2,2) = 1 segment. total=1, sumsq=1
y=1: C(3,2) = 3 segments. total=4, sumsq=1+9=10

totalSq = 16
diff = 16 - 10 = 6
ans = 6 / 2 = 3

Result: 3
```

---

## ⏱️ Time Complexity
```
O(n) — single pass to count + single pass over unique y-values
```

## 💾 Space Complexity
```
O(n) — for the hash map of y-coordinate counts
```

---

## ⚠️ Edge Cases
- Fewer than 2 points on any y-level → no segments from that level
- All points on the same y-level → no trapezoid possible (need two different levels)
- Very large counts → use modular arithmetic throughout

---

## 🎯 Interview Takeaways
- Counting pairs from different groups uses the identity: `C(total, 2) - sum(C(group_i, 2))` or equivalently `(total^2 - sumSq) / 2`.
- Modular inverse is needed for division under a prime modulus.
- Precomputing `INV2 = 500000004` for mod 10^9 + 7 is a common trick.

---

## 📌 Key Pattern
👉 **"Count cross-group pairs using total^2 - sum of squares, divided by 2 with modular inverse."**

---

## 🔁 Related Problems
- 1512. Number of Good Pairs
- 2013. Detect Squares
- 939. Minimum Area Rectangle

---

## 🚀 Final Thoughts
This problem elegantly reduces geometric trapezoid counting to pure combinatorics. The key formula `(total^2 - sumSq) / 2` for cross-group pairing is a versatile technique applicable to many counting problems.

---

✨ **Rule to remember:**
> To count pairs across different groups, use (sum^2 - sum_of_squares) / 2 — it excludes same-group pairs automatically.
