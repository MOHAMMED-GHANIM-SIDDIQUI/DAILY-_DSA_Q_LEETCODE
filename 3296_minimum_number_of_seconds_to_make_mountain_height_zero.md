# 3296. Minimum Number of Seconds to Make Mountain Height Zero

## 🔗 Problem Link
https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Binary Search, Math, Array

---

## 🧩 Problem Summary
Given a mountain of height `mountainHeight` and an array `workerTimes`, each worker `i` takes `workerTimes[i] * (1 + 2 + ... + h)` seconds to reduce the mountain by `h` units. All workers work in parallel. Find the minimum number of seconds needed to reduce the mountain height to zero.

### 📌 Constraints
- `1 <= mountainHeight <= 10^5`
- `1 <= workerTimes.length <= 10^4`
- `1 <= workerTimes[i] <= 10^6`

---

## 💭 Intuition
👉 Binary search on the answer (time). For a given time `mid`, compute how much height each worker can reduce using the formula derived from `t * h * (h+1) / 2 <= mid`. If the total height reduction >= mountainHeight, the time is sufficient.

---

## ⚡ Approach — Binary Search on Time

### 🧠 Idea
- Binary search on the total time `mid`.
- For each worker with time `t`, the maximum height they can reduce in `mid` seconds is `h = floor(sqrt(2 * mid / t + 0.25) - 0.5)`.
- Sum all workers' contributions; if the sum >= mountainHeight, the time is feasible.
- Find the minimum feasible time.

---

## 💻 Code

```python
import math
from typing import List

class Solution:
    def check(self, mid: int, workerTimes: List[int], mH: int) -> bool:
        h = 0

        for t in workerTimes:
            h += int(math.sqrt(2.0 * mid / t + 0.25) - 0.5)

            if h >= mH:
                return True

        return h >= mH

    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        maxTime = max(workerTimes)

        l = 1
        r = maxTime * mountainHeight * (mountainHeight + 1) // 2

        result = 0

        while l <= r:
            mid = l + (r - l) // 2

            if self.check(mid, workerTimes, mountainHeight):
                result = mid
                r = mid - 1
            else:
                l = mid + 1

        return result
```

---

## 🧠 Dry Run
### Input
```
mountainHeight = 4, workerTimes = [2, 1, 1]
```
### Steps
```
1. r = 2 * 4 * 5 / 2 = 20, l = 1
2. mid = 10: worker0 reduces floor(sqrt(10+0.25)-0.5)=floor(2.7)=2,
             worker1 reduces floor(sqrt(20+0.25)-0.5)=floor(4.0)=4 >= 4 => True
   result=10, r=9
3. mid = 5: worker0=floor(sqrt(5+0.25)-0.5)=1, worker1=floor(sqrt(10+0.25)-0.5)=2,
            worker2=floor(sqrt(10+0.25)-0.5)=2, total=5>=4 => True
   result=5, r=4
4. Continue narrowing... result = 3
```

---

## ⏱️ Time Complexity
```
O(n * log(maxTime * H^2)) where n is the number of workers and H is mountainHeight.
```

## 💾 Space Complexity
```
O(1) — constant extra space.
```

---

## ⚠️ Edge Cases
- Single worker: answer is `workerTimes[0] * mountainHeight * (mountainHeight + 1) / 2`.
- All workers have the same time: evenly distribute the height.
- `mountainHeight = 1`: answer is `min(workerTimes)`.

---

## 🎯 Interview Takeaways
- Binary search on the answer is powerful when the feasibility check is monotonic.
- Deriving the inverse formula (time -> max height) from the quadratic `t * h * (h+1)/2` is a key math step.
- Early termination in the check function when the sum already exceeds the target is a nice optimization.

---

## 📌 Key Pattern
👉 **"Binary search on answer with a monotonic feasibility check"**

---

## 🔁 Related Problems
- 875. Koko Eating Bananas
- 1011. Capacity To Ship Packages Within D Days
- 2064. Minimized Maximum of Products Distributed to Any Store

---

## 🚀 Final Thoughts
A classic binary search on the answer problem. The main challenge is deriving the formula for how much height a worker can reduce in a given time, which involves solving a quadratic inequality. Once that's established, the binary search framework is straightforward.

---

✨ **Rule to remember:**
> When workers operate in parallel and you need the minimum time, binary search on time and check if total work meets the target.
