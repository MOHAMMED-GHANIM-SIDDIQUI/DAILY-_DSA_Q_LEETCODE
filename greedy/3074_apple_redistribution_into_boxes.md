# 3074. Apple Redistribution into Boxes

## 🔗 Problem Link
https://leetcode.com/problems/apple-redistribution-into-boxes/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Greedy, Sorting

---

## 🧩 Problem Summary
You have packs of apples and boxes with given capacities. Find the minimum number of boxes needed to redistribute all the apples. Each box can hold up to its capacity, and you want to use as few boxes as possible.

### 📌 Constraints
- `1 <= apple.length, capacity.length <= 50`
- `1 <= apple[i], capacity[i] <= 50`
- The total capacity is guaranteed to be >= total apples.

---

## 💭 Intuition
👉 To minimize the number of boxes, always use the largest boxes first. Sort capacities in descending order and greedily fill until all apples are accommodated.

---

## ⚡ Approach — Greedy (Largest Box First)

### 🧠 Idea
- Compute the total number of apples.
- Sort box capacities in descending order.
- Greedily add the largest boxes until the cumulative capacity meets or exceeds the total apples.
- Return the number of boxes used.

---

## 💻 Code

```python
class Solution:
  def minimumBoxes(self, apple: list[int], capacity: list[int]) -> int:
    appleSum = sum(apple)
    capacitySum = 0

    for i, c in enumerate(sorted(capacity, reverse=True)):
      capacitySum += c
      if capacitySum >= appleSum:
        return i + 1

    return len(capacity)
```

---

## 🧠 Dry Run
### Input
```
apple = [1, 3, 2], capacity = [4, 3, 1, 5, 2]
```
### Steps
```
1. appleSum = 1 + 3 + 2 = 6
2. Sorted capacity (desc) = [5, 4, 3, 2, 1]
3. i=0: capacitySum = 5 < 6 => continue
4. i=1: capacitySum = 5 + 4 = 9 >= 6 => return 2
Result: 2
```

---

## ⏱️ Time Complexity
```
O(n log n) where n is the number of boxes (for sorting).
```

## 💾 Space Complexity
```
O(n) for the sorted array (or O(1) if sorting in-place).
```

---

## ⚠️ Edge Cases
- Only one box that fits all apples: return 1.
- Every box is needed: return len(capacity).
- Single apple pack and single box: return 1.

---

## 🎯 Interview Takeaways
- Greedy "largest first" is optimal for bin-packing when minimizing container count.
- Always compute the total requirement first, then greedily fill from the largest.

---

## 📌 Key Pattern
👉 **"Greedy largest-first selection to minimize container count"**

---

## 🔁 Related Problems
- 1710. Maximum Units on a Truck
- 881. Boats to Save People

---

## 🚀 Final Thoughts
A straightforward greedy problem. Sort the capacities in descending order and accumulate until the total is met. The simplicity of the approach matches the easy difficulty.

---

✨ **Rule to remember:**
> To minimize the number of containers, always pick the largest ones first — sort descending and accumulate.
