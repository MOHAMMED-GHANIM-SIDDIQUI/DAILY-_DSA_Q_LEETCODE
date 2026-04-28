# 3464. Maximize the Distance Between Points on a Square

## 🔗 Problem Link
https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Binary Search, Geometry, Greedy, Sorting

---

## 🧩 Problem Summary
Given a square with side length `side` and points on its perimeter, select `k` points such that the minimum distance between any two consecutive selected points (along the perimeter) is maximized. Return this maximum possible minimum distance.

### 📌 Constraints
- `2 <= side <= 10^9`
- `4 <= points.length <= min(4 * side, 10^5)`
- `2 <= k <= points.length`
- Points lie on the perimeter of the square.

---

## 💭 Intuition
👉 Map 2D perimeter points to 1D positions along the perimeter, then binary search on the minimum distance. For each candidate distance, greedily check if we can place `k` points with at least that spacing by trying each point as a potential starting point.

---

## ⚡ Approach — Binary Search + Greedy Placement

### 🧠 Idea
- Convert each 2D point to a 1D perimeter position (0 to 4*side) based on which edge it's on.
- Sort the 1D positions.
- Binary search on the minimum distance `limit`.
- For each candidate `limit`, try each point as the starting point and greedily place the remaining `k-1` points using binary search (`bisect_left`) to find the next valid point with spacing >= `limit`.
- Ensure the last point and first point also satisfy the distance constraint (wrap-around).

---

## 💻 Code

```python
class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        arr = []
        for x, y in points:
            if x == 0:
                arr.append(y)
            elif y == side:
                arr.append(side + x)
            elif x == side:
                arr.append(side * 3 - y)
            else:
                arr.append(side * 4 - x)

        arr.sort()

        def check(limit: int) -> bool:
            perimeter = side * 4
            for start in arr:
                end = start + perimeter - limit
                cur = start
                for _ in range(k - 1):
                    idx = bisect.bisect_left(arr, cur + limit)
                    if idx == len(arr) or arr[idx] > end:
                        cur = -1
                        break
                    cur = arr[idx]
                if cur != -1:
                    return True
            return False

        low, high = 1, side
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
```

---

## 🧠 Dry Run
### Input
```
side = 2, points = [[0,0],[0,1],[0,2],[2,2],[2,1],[2,0],[1,0],[1,2]], k = 4
```
### Steps
```
1. Convert to 1D: [0, 1, 2, 4, 5, 6, 7, 3] => sorted: [0, 1, 2, 3, 4, 5, 6, 7]
2. Perimeter = 8
3. Binary search: low=1, high=2
4. mid=1: check(1) => try start=0, place at 1, 2, 3 => all within end=7 ✓ => True
   ans=1, low=2
5. mid=2: check(2) => try start=0, place at 2, 4, 6 => all within end=6 ✓ => True
   ans=2, low=3
6. low > high => return 2
```

---

## ⏱️ Time Complexity
```
O(n^2 * k * log(side)) where n is the number of points — for each binary search step, try each starting point and greedily place k points using binary search.
```

## 💾 Space Complexity
```
O(n) for the sorted 1D position array.
```

---

## ⚠️ Edge Cases
- Points clustered on one edge: limits the achievable minimum distance.
- `k = 2`: binary search for the maximum gap between any two points on the perimeter.
- `side` is very large: binary search keeps the range manageable.

---

## 🎯 Interview Takeaways
- Mapping 2D perimeter points to 1D simplifies distance calculations.
- Binary search on the answer combined with a greedy feasibility check is a powerful pattern.
- Handling the wrap-around (circular perimeter) requires careful boundary management.

---

## 📌 Key Pattern
👉 **"2D perimeter to 1D mapping + binary search on minimum distance with greedy placement"**

---

## 🔁 Related Problems
- 1552. Magnetic Force Between Two Balls
- 2517. Maximum Tastiness of Candy Basket
- 2064. Minimized Maximum of Products Distributed to Any Store

---

## 🚀 Final Thoughts
This hard problem combines geometry (perimeter linearization) with binary search and greedy algorithms. The critical insight is converting the 2D square perimeter into a 1D line, which reduces the problem to a classic "maximize minimum spacing" binary search problem.

---

✨ **Rule to remember:**
> For spacing problems on a perimeter, linearize the perimeter to 1D, then binary search on the minimum distance with greedy placement.
