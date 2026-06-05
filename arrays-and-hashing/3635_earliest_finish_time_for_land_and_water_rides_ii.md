# 3635. Earliest Finish Time for Land and Water Rides II

## 🔗 Problem Link
https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Binary Search, Sorting, Enumeration

---

## 🧩 Problem Summary
Identical setup to **3633**: you take exactly **one land ride** and **one water ride**, in either order. A ride starts no earlier than its open time, and the second ride starts only after the first finishes. Return the **earliest** finish time of the second ride. The "II" version raises the input limits, so an efficient `O(n + m)` (or `O(n log n)`) solution is expected rather than a quadratic all-pairs scan.

### 📌 Constraints
- Larger array sizes than 3633 (the reason this is the Medium follow-up).
- `1 <= startTime[i], duration[i]`.

---

## 💭 Intuition
The same key observation as 3633 makes the larger constraints harmless: for a fixed order "A first, then B," ride 2 depends on ride 1 **only** through ride 1's finish time, and `max(open2, finish1) + dur2` is **monotonic** in `finish1`. So the single best ride-1 is the one that **finishes earliest** — no need to pair every A with every B (which would be the `O(n·m)` trap the bigger limits punish).

Therefore:
1. Compute `finish1 = min(start1[i] + dur1[i])` in one pass.
2. Compute `finish2 = min(max(start2[j], finish1) + dur2[j])` in one pass.
3. Do this for **both orders** and take the minimum.

This is linear and sidesteps sorting/binary-search entirely while still respecting the tighter limits.

---

## ⚡ Approach — Earliest first-finish, linear scan (no all-pairs)

### 🧠 Idea
```
solve(start1, dur1, start2, dur2):
    finish1 = min over i of start1[i] + dur1[i]
    finish2 = min over j of max(start2[j], finish1) + dur2[j]
    return finish2

answer = min( solve(land, water), solve(water, land) )
```

### 🔑 Why this beats the quadratic version
Pairing every land ride with every water ride is `O(n·m)`. But ride 1 only matters via `finish1`, and a smaller `finish1` never makes ride 2 worse — so only the earliest-finishing ride 1 can be optimal. That single value is found in one pass, dropping the whole thing to `O(n + m)`.

---

## 💻 Code

```python
class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:

        def solve(start1, duration1, start2, duration2):
            # Earliest finish time for the first activity
            finish1 = inf
            for i in range(len(start1)):
                finish1 = min(finish1, start1[i] + duration1[i])

            # Earliest finish time for the second activity
            finish2 = inf
            for i in range(len(start2)):
                finish2 = min(
                    finish2,
                    max(start2[i], finish1) + duration2[i]
                )

            return finish2

        land_water = solve(
            landStartTime, landDuration,
            waterStartTime, waterDuration,
        )

        water_land = solve(
            waterStartTime, waterDuration,
            landStartTime, landDuration,
        )

        return min(land_water, water_land)
```

---

## 🧠 Dry Run
### Input
```
land:  start=[5], dur=[2]
water: start=[1, 9], dur=[5, 1]
```

### land → water
```
finish1 = 5 + 2 = 7
finish2 = min( max(1,7)+5, max(9,7)+1 ) = min(12, 10) = 10
```

### water → land
```
finish1 = min(1+5, 9+1) = 6
finish2 = max(5,6) + 2 = 8
```

### Answer
```
min(10, 8) = 8
```

---

## ⏱️ Time Complexity
```
O(n + m)   — two linear passes per order, two orders.
```

## 💾 Space Complexity
```
O(1)   — running minima only.
```

---

## ⚠️ Edge Cases
- **Large inputs** → the linear scan is the whole point; an all-pairs solution would TLE here.
- **Handoff dominates open time** → `max(open2, finish1) = finish1`.
- **Open time dominates** → ride 2 waits for its own open time regardless of finish1.
- **Ties in earliest finish1** → any of them yields the same downstream result.

---

## 🎯 Interview Takeaways
- The constraint bump from 3633 → 3635 is a nudge to prove you avoid `O(n·m)`. The monotonicity argument is the proof that one pass suffices.
- The tags mention Binary Search / Sorting — those are alternative routes, but the monotonic-dependency insight makes a plain linear scan both simpler and asymptotically best.
- Reusing one `solve` for both orders by swapping arguments keeps the code DRY and symmetric.

---

## 📌 Key Pattern
👉 **"Two-phase, either-order scheduling where phase 2 sees phase 1 only via its finish time → collapse phase 1 to its earliest finish; linear, not all-pairs."**

---

## 🔁 Related Problems
- 3633. Earliest Finish Time for Land and Water Rides I
- 1834. Single-Threaded CPU
- 2589. Minimum Time to Complete All Tasks
- 630. Course Schedule III

---

## 🚀 Final Thoughts
Same solution as 3633 — and that's the lesson. The "II" version dares you to write an `O(n·m)` pairing; recognising that ride 1 matters only through its earliest finish keeps the identical linear code correct and fast under the heavier limits.

---

✨ **Rule to remember:**
> A bigger-constraints follow-up usually means "your brute force pairing won't pass." Look for a value that fully summarises one phase (here, the earliest finish) and the quadratic collapses to linear.
