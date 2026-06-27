# 3020. Find the Maximum Number of Elements in Subset

## 🔗 Problem Link
https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Hash Table, Enumeration

---

## 🧩 Problem Summary

Pick a subset of `nums` that can be arranged in a 0-indexed array following the pattern `[x, x^2, x^4, ..., x^(k/2), x^k, x^(k/2), ..., x^4, x^2, x]` — a palindromic chain of repeated squarings where `k` is a power of 2. Return the maximum number of elements such a subset can contain.

### 📌 Constraints
- `2 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`

---

## 💭 Intuition

👉 Count how many times each value appears. For a base `x > 1`, you can keep climbing `x -> x^2 -> x^4 -> ...` as long as the current value has at least 2 copies (needed for the mirrored sides) and its square also exists; the peak contributes one extra element. The value `1` is special since `1^2 = 1`, so it only needs as many copies as you can use in pairs.

---

## ⚡ Approach — Counter + Chain Walk

### 🧠 Idea
- Build a `Counter` of all values.
- For each distinct `key`:
  - If `key == 1`: the chain is all 1's, which must form a palindrome of odd length → use `count[1]` if it's odd, otherwise `count[1] - 1`.
  - Otherwise: walk `key -> key*key` while `count[key] >= 2` and `key*key` is present, adding 2 each step (the two mirrored copies). Then add 1 for the unique peak element.
- Track the maximum chain length across all keys and return it.

---

## 💻 Code

```python
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count = Counter(nums)

        res = 0
        for key in count.keys():
            if key == 1:
                total = count[key] if count[key] % 2 else count[key] - 1
            else:
                total = 0

                while count[key] >= 2 and key * key in count:
                    total += 2
                    key = key * key
                
                total += 1
            
            res = max(res, total)
        
        return res
```

---

## 🧠 Dry Run

### Input
```
nums = [5, 4, 1, 2, 2]   ->  count = {5:1, 4:1, 1:1, 2:2}
```

### Steps
```
key=5: 5!=1, count[5]=1 < 2 -> while skipped, total=0+1=1, res=1
key=4: 4!=1, count[4]=1 < 2 -> while skipped, total=1, res=1
key=1: count[1]=1 odd -> total=1, res=1
key=2: 2!=1
       count[2]=2>=2 and 2*2=4 in count -> total=2, key=4
       count[4]=1 < 2 -> stop
       total=2+1=3, res=max(1,3)=3
return 3        (subset [2,4,2])
```

---

## ⏱️ Time Complexity
```
O(n log(max))
```
Each distinct key walks a squaring chain of length O(log of the max value); total work is bounded by O(n log max).

---

## 💾 Space Complexity
```
O(n)
```
The Counter stores up to `n` distinct values.

---

## ⚠️ Edge Cases
- Value `1` with even count → drop one to keep odd palindrome length.
- A base whose square is missing → chain length is just 1 (single peak).
- A base appearing only once → cannot mirror, contributes only 1.
- Note: reusing `key` as the loop variable mutates it inside the chain walk, which is fine since each `count.keys()` iteration starts fresh.

---

## 🎯 Interview Takeaways
- The pattern is a palindrome of squarings; only the apex is unpaired.
- The `>= 2` check encodes "need two copies for the symmetric sides."
- Handle `x == 1` separately because squaring leaves it unchanged.

---

## 📌 Key Pattern
👉 **"Hash count + greedy power-chain expansion"**

---

## 🔁 Related Problems
- 0128 - Longest Consecutive Sequence
- 0954 - Array of Doubled Pairs
- 2350 - Shortest Impossible Sequence of Rolls

---

## 🚀 Final Thoughts
The crux is mapping the visual `[x, x^2, ..., x^2, x]` shape onto a "climb while square exists and you have a pair" loop, with `1` as the lone special case.

---

✨ **Rule to remember:**
> "Count occurrences, then greedily extend the squaring chain while pairs and squares exist, treating 1 specially."
