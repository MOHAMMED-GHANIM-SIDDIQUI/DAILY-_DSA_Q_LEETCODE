# 3510. Minimum Pair Removal to Sort Array II

## 🔗 Problem Link
https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Sorted Container, Linked List, Greedy, Simulation

---

## 🧩 Problem Summary
Same as Minimum Pair Removal to Sort Array I, but with much larger constraints. Repeatedly find the pair of adjacent elements with the smallest sum, merge them, and return the number of operations to make the array non-decreasing. Requires an efficient approach.

### 📌 Constraints
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

## 💭 Intuition
👉 Use a SortedList to efficiently find and remove the minimum pair sum, and maintain a virtual linked list (next/prev arrays) to skip removed elements — track inversion count incrementally instead of rescanning.

---

## ⚡ Approach — SortedList + Linked List with Inversion Tracking

### 🧠 Idea
- Maintain a SortedList of `(pairSum, index)` for all adjacent pairs.
- Use `nextIndices` and `prevIndices` arrays to simulate a doubly linked list.
- Track the total inversion count; update it incrementally when pairs are merged.
- At each step, pop the smallest pair sum, merge, update neighbors, and adjust inversion count.

---

## 💻 Code

```python
class Solution:
  def minimumPairRemoval(self, nums: list[int]) -> int:
    n = len(nums)
    ans = 0
    inversionsCount = sum(nums[i + 1] < nums[i] for i in range(n - 1))
    nextIndices = [i + 1 for i in range(n)]
    prevIndices = [i - 1 for i in range(n)]
    pairSums = SortedList((a + b, i)
                          for i, (a, b) in enumerate(itertools.pairwise(nums)))

    while inversionsCount > 0:
      ans += 1
      smallestPair = pairSums.pop(0)
      pairSum, currIndex = smallestPair
      nextIndex = nextIndices[currIndex]
      prevIndex = prevIndices[currIndex]

      if prevIndex >= 0:
        oldPairSum = nums[prevIndex] + nums[currIndex]
        newPairSum = nums[prevIndex] + pairSum
        pairSums.remove((oldPairSum, prevIndex))
        pairSums.add((newPairSum, prevIndex))
        if nums[prevIndex] > nums[currIndex]:
          inversionsCount -= 1
        if nums[prevIndex] > pairSum:
          inversionsCount += 1

      if nums[nextIndex] < nums[currIndex]:
        inversionsCount -= 1

      nextNextIndex = nextIndices[nextIndex] if nextIndex < n else n
      if nextNextIndex < n:
        oldPairSum = nums[nextIndex] + nums[nextNextIndex]
        newPairSum = pairSum + nums[nextNextIndex]
        pairSums.remove((oldPairSum, nextIndex))
        pairSums.add((newPairSum, currIndex))
        if nums[nextNextIndex] < nums[nextIndex]:
          inversionsCount -= 1
        if nums[nextNextIndex] < pairSum:
          inversionsCount += 1
        prevIndices[nextNextIndex] = currIndex

      nextIndices[currIndex] = nextNextIndex
      nums[currIndex] = pairSum

    return ans
```

---

## 🧠 Dry Run
### Input
```
nums = [5, 2, 3, 1]
```
### Steps
```
Initial: inversionsCount=2, pairSums=[(3,2),(7,0),(5,1)]
  nextIndices=[1,2,3,4], prevIndices=[-1,0,1,2]

Step 1: pop (3,2) → merge indices 2,3: sum=4
  prevIndex=1: old=(2+3=5), new=(2+4=6), no inversion change
  nextIndex=3, nextNext=4 (out of bounds)
  nums[2]=4, nextIndices[2]=4
  inversionsCount=2-1=1 (3>1 removed), ans=1

Step 2: pop (6,1) → merge indices 1,2: sum=6
  prevIndex=0: old=(5+2=7), new=(5+6=11)
  5>2 was inversion → -1, 5>6 no → no +1
  nextNext=4, out of bounds
  inversionsCount=1-1=0, ans=2

Result: 2
```

---

## ⏱️ Time Complexity
```
O(n log n) — each of the up to n-1 operations does O(log n) SortedList operations
```

## 💾 Space Complexity
```
O(n) — for the SortedList, next/prev arrays
```

---

## ⚠️ Edge Cases
- Already sorted → return 0 immediately
- All elements identical → return 0
- Large negative values causing overflow in pair sums
- Array reduces to a single element

---

## 🎯 Interview Takeaways
- SortedList (or balanced BST) is essential for efficient min-extraction + removal.
- Virtual linked lists (next/prev arrays) avoid costly list deletions.
- Incremental inversion counting avoids O(n) rescanning each step.

---

## 📌 Key Pattern
👉 **"Efficient simulation with SortedList + linked list — track inversions incrementally instead of rescanning."**

---

## 🔁 Related Problems
- 3507. Minimum Pair Removal to Sort Array I
- 23. Merge k Sorted Lists
- 295. Find Median from Data Stream

---

## 🚀 Final Thoughts
This is a masterclass in optimizing brute-force simulation. The three key upgrades from the easy version are: SortedList for O(log n) min-finding, linked list arrays for O(1) neighbor access, and incremental inversion tracking for O(1) sorted-check.

---

✨ **Rule to remember:**
> "When brute-force simulation is too slow, use sorted containers + linked lists + incremental state tracking."
