# 2126. Destroying Asteroids

## 🔗 Problem Link
https://leetcode.com/problems/destroying-asteroids/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Greedy, Sorting

---

## 🧩 Problem Summary
You start with a planet of mass `mass`. There are asteroids with masses given in `asteroids`. You may collide with the asteroids in **any order**. A collision succeeds only if the planet's mass is **greater than or equal to** the asteroid's mass; on success the planet **absorbs** the asteroid (its mass grows by the asteroid's mass). If at any point the planet's mass is **less than** the asteroid it meets, that collision destroys the planet. Return `True` if **all** asteroids can be destroyed.

### 📌 Constraints
- `1 <= mass <= 10^5`
- `1 <= asteroids.length <= 10^5`
- `1 <= asteroids[i] <= 10^5`

---

## 💭 Intuition
Since we choose the order freely, the safest strategy is **greedy: always eat the smallest remaining asteroid first**. Eating small asteroids grows the planet's mass the most cheaply, which can then unlock larger ones. If even the smallest asteroid at some moment is too big for the current mass, then no other order could have helped — every other asteroid is at least as heavy.

So **sort ascending** and consume in order. The first asteroid you can't beat is a definitive failure.

---

## ⚡ Approach — Sort ascending + greedy absorb

### 🧠 Idea
1. Sort `asteroids` in non-decreasing order.
2. Walk through them; for each `threat`:
   - If `threat > mass`, the planet can't survive this one → return `False`.
   - Otherwise absorb it: `mass += threat`.
3. Survive all → return `True`.

### 🔑 Why greedy is optimal
Mass only ever **increases** as we absorb. Tackling the smallest first maximises the mass available before facing each larger asteroid. If the sorted-ascending pass fails at some asteroid `a`, then at that moment our mass is the **largest it could possibly be** after clearing everything smaller — yet still `< a`. No alternate ordering can do better, so failure is genuine.

---

## 💻 Code

```python
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for threat in asteroids:
            if threat > mass:
                return False
            mass += threat
        return True
```

---

## 🧠 Dry Run
### Input
```
mass = 10
asteroids = [3, 9, 19, 5, 21]
```

### Sorted
```
[3, 5, 9, 19, 21]
```

### Trace
```
mass=10 vs 3  → 3<=10  → mass=13
mass=13 vs 5  → 5<=13  → mass=18
mass=18 vs 9  → 9<=18  → mass=27
mass=27 vs 19 → 19<=27 → mass=46
mass=46 vs 21 → 21<=46 → mass=67
```
All absorbed → `True`.

### Failure example
```
mass = 5, asteroids = [4, 9, 23, 4]  → sorted [4,4,9,23]
5→9 (mass=9), 9→13, 13 vs 9 ok → mass=22, 22 vs 23 → 23>22 → False
```

---

## ⏱️ Time Complexity
```
O(n log n)   — dominated by the sort; the scan is O(n).
```

## 💾 Space Complexity
```
O(1) extra   — in-place sort (O(n) if the sort allocates / counting the recursion).
```

---

## ⚠️ Edge Cases
- **Single asteroid** larger than `mass` → immediate `False`.
- **Equal masses** → `threat == mass` succeeds (the condition is `>` for failure, i.e. `>=` to absorb).
- **Already huge planet** → absorbs everything trivially.
- Watch overflow only in languages with fixed ints — total mass can reach `~10^5 + 10^5·10^5 ≈ 10^{10}`, fine for Python / 64-bit.

---

## 🎯 Interview Takeaways
- The freedom to choose order is the signal for a greedy/sorting solution — "any order" almost always means "find the order that a sort exposes."
- The proof matters: argue that sorted-ascending maximises available mass at every step, so a failure there is unavoidable.
- A min-heap gives the same behaviour but is strictly worse than a single sort here since the set never changes.

---

## 📌 Key Pattern
👉 **"Choose-your-own-order accumulation where a resource grows by what you consume → sort smallest-first and absorb greedily."**

---

## 🔁 Related Problems
- 1326. Minimum Number of Taps to Open to Water a Garden
- 1798. Maximum Number of Consecutive Values You Can Make
- 870. Advantage Shuffle
- 2406. Divide Intervals Into Minimum Number of Groups

---

## 🚀 Final Thoughts
The whole problem rests on one greedy exchange argument: smallest-first never loses. Once you trust that, the code is a sort and a five-line scan. The trap is overthinking the "any order" clause into something combinatorial.

---

✨ **Rule to remember:**
> When you may consume items in any order and consuming one strengthens you, eat the weakest first — the sorted pass is both the algorithm and the proof.
