# 3633. Earliest Finish Time for Land and Water Rides I

## 🔗 Problem Link
https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Enumeration

---

## 🧩 Problem Summary
You must take **one land ride** and **one water ride**, in **either order** (land→water or water→land). Land ride `i` opens at `landStartTime[i]` and takes `landDuration[i]`; water ride `j` opens at `waterStartTime[j]` and takes `waterDuration[j]`. A ride can only start at or after its open time; the second ride can only start after the first ride **finishes**. Return the **earliest** possible finish time of the second ride.

### 📌 Constraints
- Equal-length arrays for each ride type; small enough that an `O(n + m)` pass works.
- `1 <= startTime[i], duration[i]` (non-negative times).

---

## 💭 Intuition
We do exactly two rides, one of each type, and we pick the order. So the answer is the **minimum over the two orderings**:

- **land then water**, and
- **water then land**.

For a fixed order "type-A first, then type-B," the best plan is:
1. Pick the type-A ride that **finishes earliest** → `finish1 = min(startA[i] + durationA[i])`. Finishing A as early as possible never hurts B, since B can only start after A is done.
2. For each type-B ride, it starts at `max(its open time, finish1)` and ends `+ durationB`. Take the **minimum** finish over all B rides.

Run this `solve` both ways and return the smaller result.

---

## ⚡ Approach — Earliest first-ride finish, then best second ride

### 🧠 Idea
```
solve(start1, dur1, start2, dur2):
    finish1 = min over i of  start1[i] + dur1[i]          # earliest we can finish ride 1
    finish2 = min over j of  max(start2[j], finish1) + dur2[j]
    return finish2

answer = min( solve(land→water), solve(water→land) )
```

### 🔑 Why "earliest finish of ride 1" is enough
Ride 2 depends on ride 1 only through `finish1`, and its start is `max(start2[j], finish1)` — **monotonic** in `finish1`. A smaller `finish1` can only make ride 2 start the same or sooner. So among all ride-1 choices, the one finishing earliest dominates; we never need to try the others.

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
land:  start=[2, 8], dur=[4, 1]
water: start=[6],    dur=[3]
```

### land → water
```
finish1 = min(2+4, 8+1) = min(6, 9) = 6
finish2 = max(6, 6) + 3 = 9
```

### water → land
```
finish1 = 6 + 3 = 9
finish2 = min( max(2,9)+4, max(8,9)+1 ) = min(13, 10) = 10
```

### Answer
```
min(9, 10) = 9
```

---

## ⏱️ Time Complexity
```
O(n + m)   — each ordering scans both arrays once; two orderings → still linear.
```

## 💾 Space Complexity
```
O(1)   — only running minima.
```

---

## ⚠️ Edge Cases
- **Second ride already open before ride 1 finishes** → `max(start2, finish1) = finish1`, so it starts immediately at handoff.
- **Second ride opens later than the handoff** → its own open time dominates.
- **One ride of each type only** → both orderings still evaluated; the cheaper wins.

---

## 🎯 Interview Takeaways
- Two-activity sequencing with a free order → enumerate the two orders; within each, greedily finish the first activity as early as possible.
- The monotonicity argument (`max(s, f) + d` is non-decreasing in `f`) is what licenses collapsing ride-1 to its single earliest-finishing option — say it out loud in an interview.
- **3635** is the same setup with tighter constraints; the `O(n+m)` idea here is the foundation.

---

## 📌 Key Pattern
👉 **"Sequence two phases in either order: try both orders; per order, minimise phase-1 finish, then minimise `max(open, finish1) + dur` over phase-2."**

---

## 🔁 Related Problems
- 3635. Earliest Finish Time for Land and Water Rides II
- 1326. Minimum Number of Taps to Open to Water a Garden
- 2589. Minimum Time to Complete All Tasks
- 1834. Single-Threaded CPU

---

## 🚀 Final Thoughts
The "either order" clause splits cleanly into two symmetric subproblems, and each subproblem rewards a single greedy fact: finish the first ride as early as you can. Two linear passes and a `min` finish it.

---

✨ **Rule to remember:**
> When two phases can run in either order and phase 2 only sees phase 1 through its finish time, evaluate both orders and finish phase 1 as early as possible — earliest finish dominates because the dependency is monotonic.
