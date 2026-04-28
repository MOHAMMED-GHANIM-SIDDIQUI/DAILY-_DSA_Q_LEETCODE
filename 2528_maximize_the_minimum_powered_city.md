# 2528. Maximize the Minimum Powered City

## 🔗 Problem Link
https://leetcode.com/problems/maximize-the-minimum-powered-city/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Binary Search, Greedy, Sliding Window, Prefix Sum

---

## 🧩 Problem Summary
Given `n` cities in a line with power stations and a range `r` (each station powers cities within distance `r`), you can build `k` additional stations. Maximize the minimum power among all cities.

### 📌 Constraints
- `1 <= n <= 10^5`
- `0 <= stations[i] <= 10^5`
- `0 <= r <= n - 1`
- `0 <= k <= 10^9`

---

## 💭 Intuition
👉 Binary search on the answer (minimum power). For each candidate minimum, greedily check if `k` stations suffice by scanning left to right and placing stations at the farthest useful position when a city's power falls short.

---

## ⚡ Approach — Binary Search + Greedy Validation

### 🧠 Idea
- Binary search the answer in `[min(stations), sum(stations) + k]`.
- For each candidate `minPower`, simulate: scan cities left to right, compute each city's power using a sliding window sum.
- If a city's power < `minPower`, greedily add stations at position `min(n-1, i+r)` to maximize coverage.
- If total added stations exceed `k`, the candidate is too high.

---

## 💻 Code

```cpp
class Solution {
 public:
  long long maxPower(vector<int>& stations, int r, int k) {
    long left = ranges::min(stations);
    long right = accumulate(stations.begin(), stations.end(), 0L) + k + 1;

    while (left < right) {
      const long mid = (left + right) / 2;
      if (check(stations, r, k, mid))
        left = mid + 1;
      else
        right = mid;
    }

    return left - 1;
  }

 private:
  // Returns true if each city can have at least `minPower`.
  bool check(vector<int> stations, int r, int additionalStations,
             long minPower) {
    const int n = stations.size();
    // Initilaize `power` as the 0-th city's power - stations[r].
    long power = accumulate(stations.begin(), stations.begin() + r, 0L);

    for (int i = 0; i < n; ++i) {
      if (i + r < n)
        power += stations[i + r];  // `power` = sum(stations[i - r..i + r]).
      if (power < minPower) {
        const long requiredPower = minPower - power;
        // There're not enough stations to plant.
        if (requiredPower > additionalStations)
          return false;
        // Greedily plant `requiredPower` power stations in the farthest place
        // to cover as many cities as possible.
        stations[min(n - 1, i + r)] += requiredPower;
        additionalStations -= requiredPower;
        power += requiredPower;
      }
      if (i - r >= 0)
        power -= stations[i - r];
    }

    return true;
  }
};
```

---

## 🧠 Dry Run
### Input
```
stations = [1,2,4,5,0], r = 1, k = 2
```
### Steps
```
Binary search range: [0, 14]
mid = 7: check if min power >= 7
  City 0: power = stations[0]+stations[1] = 3 < 7, need 4 > k=2 → false
mid = 3: check if min power >= 3
  Simulate with greedy placement... → feasible
Continue binary search...
Result: 5
```

---

## ⏱️ Time Complexity
```
O(n * log(sum + k)) — binary search over answer range, O(n) validation per check.
```

## 💾 Space Complexity
```
O(n) — copy of stations array in each check.
```

---

## ⚠️ Edge Cases
- `k = 0`: answer is the current minimum city power.
- `r >= n-1`: every station powers every city.
- All stations are 0: distribute k stations optimally.

---

## 🎯 Interview Takeaways
- "Maximize the minimum" screams binary search on the answer.
- Greedy placement at the farthest position maximizes coverage.
- The sliding window maintains each city's power efficiently.

---

## 📌 Key Pattern
👉 **"Binary search on answer + greedy validation for 'maximize the minimum' problems."**

---

## 🔁 Related Problems
- 1552. Magnetic Force Between Two Balls
- 2517. Maximum Tastiness of Candy Basket
- 875. Koko Eating Bananas

---

## 🚀 Final Thoughts
This problem beautifully combines binary search on the answer with a greedy validation strategy. The key greedy insight — placing stations as far right as possible — ensures maximum coverage for cities yet to be processed.

---

✨ **Rule to remember:**
> "Maximize the minimum? Binary search the answer, greedily validate each candidate."
