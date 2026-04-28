# 2594. Minimum Time to Repair Cars

## 🔗 Problem Link
https://leetcode.com/problems/minimum-time-to-repair-cars/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Binary Search

---

## 🧩 Problem Summary
You are given an array `ranks` where `ranks[i]` is the rank of the i-th mechanic. A mechanic with rank `r` takes `r * n^2` minutes to repair `n` cars. All mechanics work simultaneously. Return the minimum time needed to repair all `cars`.

### 📌 Constraints
- `1 <= ranks.length <= 10^5`
- `1 <= ranks[i] <= 100`
- `1 <= cars <= 10^6`

---

## 💭 Intuition
👉 Binary search on time. For a given time `t`, each mechanic with rank `r` can fix `floor(sqrt(t / r))` cars. If the total across all mechanics >= `cars`, the time is sufficient.

---

## ⚡ Approach — Binary Search on Time

### 🧠 Idea
- Binary search in range `[0, minRank * cars * cars]`.
- For each candidate time `mid`, sum up `floor(sqrt(mid / rank))` over all mechanics.
- If total cars fixed >= target, try less time; otherwise, try more.

---

## 💻 Code

```cpp
#include <vector>
#include <algorithm>
#include <cmath>

class Solution {
public:
    long long repairCars(std::vector<int>& ranks, int cars) {
        // Binary search bounds
        long left = 0;
        long right = static_cast<long>(*std::min_element(ranks.begin(), ranks.end())) * cars * cars;

        // Binary search to minimize the time
        while (left < right) {
            const long mid = (left + right) / 2;

            // Check if we can fix enough cars in 'mid' minutes
            if (numCarsFixed(ranks, mid) >= cars)
                right = mid;  // Try to minimize the time
            else
                left = mid + 1;  // Increase the time
        }

        return left;  // The minimum time to repair all cars
    }

private:
    // Function to calculate how many cars can be repaired in the given 'minutes'
    long numCarsFixed(const std::vector<int>& ranks, long minutes) {
        long carsFixed = 0;

        // Calculate cars fixed by each worker
        for (const int rank : ranks) {
            carsFixed += static_cast<long>(sqrt(minutes / rank));
        }

        return carsFixed;
    }
};
```

---

## 🧠 Dry Run
### Input
```
ranks = [4,2,3,1], cars = 10
```
### Steps
```
left=0, right=1*10*10=100
mid=50: mechanic r=4: sqrt(50/4)=3, r=2: sqrt(25)=5, r=3: sqrt(16)=4, r=1: sqrt(50)=7 => total=19 >= 10, right=50
mid=25: r=4: sqrt(6)=2, r=2: sqrt(12)=3, r=3: sqrt(8)=2, r=1: sqrt(25)=5 => total=12 >= 10, right=25
mid=12: r=4: sqrt(3)=1, r=2: sqrt(6)=2, r=3: sqrt(4)=2, r=1: sqrt(12)=3 => total=8 < 10, left=13
mid=19: r=4: sqrt(4)=2, r=2: sqrt(9)=3, r=3: sqrt(6)=2, r=1: sqrt(19)=4 => total=11 >= 10, right=19
mid=16: r=4: sqrt(4)=2, r=2: sqrt(8)=2, r=3: sqrt(5)=2, r=1: sqrt(16)=4 => total=10 >= 10, right=16
...converges to 16
```

---

## ⏱️ Time Complexity
```
O(n * log(minRank * cars^2)) where n is the number of mechanics
```

## 💾 Space Complexity
```
O(1)
```

---

## ⚠️ Edge Cases
- Single mechanic — answer is `rank * cars^2`
- All mechanics have rank 1
- `cars = 1` — minimum rank mechanic fixes it in `rank * 1` time

---

## 🎯 Interview Takeaways
- Binary search on the answer works when the feasibility function is monotonic.
- The formula `r * n^2 = t` inverts to `n = sqrt(t/r)`, giving cars fixed in time `t`.

---

## 📌 Key Pattern
👉 **"Binary search on time with a capacity-check feasibility function"**

---

## 🔁 Related Problems
- 875. Koko Eating Bananas
- 1011. Capacity To Ship Packages Within D Days
- 2560. House Robber IV

---

## 🚀 Final Thoughts
A classic binary search on the answer problem. The key mathematical insight is inverting the time-to-cars formula to compute capacity at a given time, then binary searching for the minimum feasible time.

---

✨ **Rule to remember:**
> When all workers operate in parallel and you need minimum time, binary search on time and check total capacity.
