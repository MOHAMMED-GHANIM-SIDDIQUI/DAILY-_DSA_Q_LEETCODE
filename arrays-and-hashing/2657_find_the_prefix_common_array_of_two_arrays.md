# 2657. Find the Prefix Common Array of Two Arrays

## 🔗 Problem Link
https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Hash Table, Bit Manipulation

---

## 🧩 Problem Summary
You are given two **permutations** `A` and `B` of the integers `1..n`. The **prefix common array** `C` is defined so that `C[i]` is the count of numbers that appear in **both** `A[0..i]` and `B[0..i]`. Return `C`.

### 📌 Constraints
- `1 <= A.length == B.length == n <= 50`
- `1 <= A[i], B[i] <= n`
- `A` and `B` are both permutations of `1..n`.

---

## 💭 Intuition
A number is "common at prefix `i`" once it has been seen in **both** arrays up to index `i`. The naive way is to intersect two growing sets at every `i` (`O(n²)` set work), but there's a cleaner observation:

Maintain a single frequency table across **both** arrays. When a value's running count hits **2**, that means it has now appeared once in `A`'s prefix and once in `B`'s prefix (since each array is a permutation, no value repeats within one array). The moment a value reaches frequency `2`, it becomes newly common — so increment a running `common` counter and never double-count it.

---

## ⚡ Approach — Shared frequency counter

### 🧠 Idea
1. Keep `freq[v]` over values `1..n`, shared by both arrays.
2. At step `i`:
   - Add `A[i]`; if its count just became `2`, it is now common → `common += 1`.
   - Add `B[i]`; if its count just became `2`, it is now common → `common += 1`.
3. Append the current `common` to the answer.

Because each value appears at most once in `A` and once in `B`, a count of `2` happens **exactly once per value** — so `common` only ever grows, and each common element is counted a single time.

---

## 💻 Code

```python
class Solution:
    def findThePrefixCommonArray(self, A, B):
        n = len(A)
        freq = [0] * (n + 1)

        common = 0
        ans = []

        for i in range(n):
            freq[A[i]] += 1
            if freq[A[i]] == 2:
                common += 1

            freq[B[i]] += 1
            if freq[B[i]] == 2:
                common += 1

            ans.append(common)

        return ans
```

---

## 🧠 Dry Run
### Input
```
A = [1, 3, 2, 4]
B = [3, 1, 2, 4]
```

### Trace
```
i=0: A=1 → freq[1]=1 ; B=3 → freq[3]=1            common=0  ans=[0]
i=1: A=3 → freq[3]=2 (+1); B=1 → freq[1]=2 (+1)   common=2  ans=[0,2]
i=2: A=2 → freq[2]=1 ; B=2 → freq[2]=2 (+1)       common=3  ans=[0,2,3]
i=3: A=4 → freq[4]=1 ; B=4 → freq[4]=2 (+1)       common=4  ans=[0,2,3,4]
```
Result: `[0, 2, 3, 4]`.

---

## ⏱️ Time Complexity
```
O(n)   — one pass, constant work per index.
```

## 💾 Space Complexity
```
O(n)   — the frequency array (or O(n/64) with a bitset, see below).
```

---

## ⚠️ Edge Cases
- **n = 1** → both arrays are `[1]`; at `i=0` freq[1] hits 2 → `common=1` → `[1]`.
- **Identical arrays** → every prefix is fully common → `C = [1, 2, ..., n]`.
- **Reverse permutations** → `common` lags and only catches up at the end.

---

## 🎯 Interview Takeaways
- The key insight is that "appears in both prefixes" ⇔ "frequency reached 2" — this collapses an intersection-of-sets problem into a single counter.
- **Bit Manipulation variant**: keep two integers `a` and `b` as bitmasks of seen values; after each step `popcount(a & b)` is the answer. That's the `O(n²/64)` approach the topic tag hints at, and it's worth mentioning as the space-optimal alternative.

---

## 📌 Key Pattern
👉 **"Need the size of an intersection of two growing prefixes? Share one frequency table and watch for the count crossing the threshold."**

---

## 🔁 Related Problems
- 1. Two Sum
- 349. Intersection of Two Arrays
- 2215. Find the Difference of Two Arrays
- 2965. Find Missing and Repeated Values

---

## 🚀 Final Thoughts
The permutation guarantee is the whole trick: it caps each value's per-array count at one, so a shared count of `2` is an unambiguous "now common" signal. Without that guarantee you'd need two separate tables and a more careful threshold.

---

✨ **Rule to remember:**
> When two sequences are permutations and you want their common-prefix size, one shared counter plus a "did it hit 2?" check beats any set intersection.
