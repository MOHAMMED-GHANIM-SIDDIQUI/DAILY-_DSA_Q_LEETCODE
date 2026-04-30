# 1128. Number of Equivalent Domino Pairs

## 🔗 Problem Link
https://leetcode.com/problems/number-of-equivalent-domino-pairs/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Hash Table, Counting

---

## 🧩 Problem Summary

Given a list of dominoes where each domino is a pair `[a, b]`, two dominoes are equivalent if `(a1 == a2 and b1 == b2)` or `(a1 == b2 and b1 == a2)`. Return the number of equivalent domino pairs `(i, j)` with `i < j`.

### 📌 Constraints
- `1 <= dominoes.length <= 4 * 10^4`
- `dominoes[i].length == 2`
- `1 <= dominoes[i][j] <= 9`

---

## 💭 Intuition

👉 Normalize each domino by sorting its two values, so `[2,1]` and `[1,2]` become the same key `[1,2]`.

👉 For each group of `n` equivalent dominoes, the number of pairs is `n*(n-1)/2`. We can compute this incrementally: when we see the k-th occurrence, it forms pairs with all `k-1` previous ones.

---

## ⚡ Approach — Hash Map Counting

### 🧠 Idea
- For each domino, sort it to create a canonical key.
- Use a hash map to track the frequency of each canonical key.
- For each domino, add its current frequency to the answer (it pairs with all previously seen equivalent dominoes), then increment the frequency.

---

## 💻 Code

```cpp
class Solution {
public:
    int numEquivDominoPairs(vector<vector<int>>& dominoes) {
        unordered_map<string, int> freq;
        int ans = 0;

        for (auto& domino : dominoes) {
            // Sort the domino to avoid checking reversed pairs
            sort(domino.begin(), domino.end());
            string key = to_string(domino[0]) + "," + to_string(domino[1]);
            ans += freq[key]++;
        }

        return ans;
    }
};
```

---

## 🧠 Dry Run

### Input
```
dominoes = [[1,2],[2,1],[3,4],[5,6],[3,4]]
```

### Steps
```
domino [1,2] → key="1,2", freq["1,2"]=0 → ans+=0, freq["1,2"]=1
domino [2,1] → sorted [1,2] → key="1,2", freq["1,2"]=1 → ans+=1, freq["1,2"]=2
domino [3,4] → key="3,4", freq["3,4"]=0 → ans+=0, freq["3,4"]=1
domino [5,6] → key="5,6", freq["5,6"]=0 → ans+=0, freq["5,6"]=1
domino [3,4] → key="3,4", freq["3,4"]=1 → ans+=1, freq["3,4"]=2

Output: 2
```

---

## ⏱️ Time Complexity
```
O(n)
```
Each domino is processed in constant time (sorting 2 elements is O(1)).

---

## 💾 Space Complexity
```
O(n)
```
The hash map stores up to `n` unique keys.

---

## ⚠️ Edge Cases
- All dominoes are the same → answer is `n*(n-1)/2`.
- No two dominoes are equivalent → answer is 0.
- Single domino → answer is 0.

---

## 🎯 Interview Takeaways
- Normalizing (sorting) the key eliminates the need for two-way comparison.
- The `ans += freq[key]++` idiom elegantly counts pairs incrementally.
- Since values are 1-9, an integer key `min*10 + max` could replace string keys for better performance.
- This is a classic counting pairs pattern.

---

## 📌 Key Pattern
👉 **"Normalize + count — sort each element to a canonical form, then count pairs using a frequency map."**

---

## 🔁 Related Problems
- 1 - Two Sum (hash map pairing)
- 49 - Group Anagrams (normalize then group)
- 447 - Number of Boomerangs

---

## 🚀 Final Thoughts
A simple but instructive problem that teaches the normalize-and-count pattern. The incremental pairing trick (`ans += freq[key]++`) is worth memorizing.

---

✨ **Rule to remember:**
> "When order doesn't matter, normalize first — then counting pairs becomes a simple frequency problem."
