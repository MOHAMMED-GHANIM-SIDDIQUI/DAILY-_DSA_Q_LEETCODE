# 1622. Fancy Sequence

## 🔗 Problem Link
https://leetcode.com/problems/fancy-sequence/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Math, Design, Segment Tree, Modular Arithmetic

---

## 🧩 Problem Summary
Design a data structure that supports appending values, adding an increment to all existing elements, multiplying all existing elements by a value, and retrieving the element at a given index — all under modulo `10^9 + 7`.

### 📌 Constraints
- `1 <= val, inc, m <= 100`
- `0 <= idx <= 10^5`
- At most `10^5` calls total to `append`, `addAll`, `multAll`, and `getIndex`.

---

## 💭 Intuition
👉 Instead of updating every element on each `addAll`/`multAll` call (O(n) each), store a global `add` and `mult` accumulator. When appending, "undo" the current transformation so the stored value is in the original coordinate system. When retrieving, "apply" the transformation.

---

## ⚡ Approach — Lazy Propagation with Modular Inverse

### 🧠 Idea
- Maintain global `add` and `mult` accumulators representing the transformation `f(x) = x * mult + add`.
- On `append(val)`: store `(val - add) * mult^(-1) mod M` so that `f(stored) = val`.
- On `addAll(inc)`: update `add = (add + inc) % M`.
- On `multAll(m)`: update `mult = (mult * m) % M` and `add = (add * m) % M`.
- On `getIndex(idx)`: return `(seq[idx] * mult + add) % M`.

---

## 💻 Code

```python
class Fancy:

    def __init__(self):
        self.M = 10**9 + 7
        self.seq = []
        self.add = 0
        self.mult = 1

    def append(self, val: int) -> None:
        x = ((val - self.add) % self.M) * pow(self.mult, self.M - 2, self.M) % self.M
        self.seq.append(x)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.M

    def multAll(self, m: int) -> None:
        self.mult = (self.mult * m) % self.M
        self.add = (self.add * m) % self.M

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.seq):
            return -1
        return (self.seq[idx] * self.mult + self.add) % self.M
```

---

## 🧠 Dry Run
### Input
```
["Fancy","append","addAll","append","multAll","getIndex","addAll","append","getIndex"]
[[],[2],[3],[7],[2],[0],[3],[10],[2]]
```
### Steps
```
append(2): add=0,mult=1 → store (2-0)*1=2, seq=[2]
addAll(3): add=3
append(7): store (7-3)*1=4, seq=[2,4]
multAll(2): mult=2, add=6
getIndex(0): 2*2+6=10 → 10
addAll(3): add=9
append(10): store (10-9)*inv(2)=1*inv(2), seq=[2,4,inv(2)_val]
getIndex(2): inv(2)*2+9=1+9=10 → 10
```

---

## ⏱️ Time Complexity
```
O(log M) per append (for modular inverse), O(1) for addAll, multAll, getIndex
```

## 💾 Space Complexity
```
O(n) — storing the sequence elements
```

---

## ⚠️ Edge Cases
- `getIndex` with index out of bounds → return -1.
- Multiple `multAll` and `addAll` calls before any `append`.
- Modular inverse requires M to be prime (which 10^9+7 is).

---

## 🎯 Interview Takeaways
- Lazy propagation is not just for segment trees — it works for global affine transformations too.
- Modular inverse via Fermat's little theorem: `a^(-1) = a^(M-2) mod M` when M is prime.
- Storing "inverse-transformed" values lets all global operations run in O(1).

---

## 📌 Key Pattern
👉 **"Lazy affine transformation with modular inverse for O(1) bulk operations"**

---

## 🔁 Related Problems
- 307. Range Sum Query - Mutable
- 370. Range Addition
- 1526. Minimum Number of Increments on Subarrays to Form a Target Array

---

## 🚀 Final Thoughts
This problem is a beautiful application of lazy propagation and modular arithmetic. The trick of "un-applying" the transformation at insertion time so retrieval is a simple formula is both elegant and efficient.

---

✨ **Rule to remember:**
> Store values in "raw" form by undoing the current global transformation; apply it back on retrieval — all bulk ops become O(1).
