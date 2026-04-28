# 2379. Minimum Recolors to Get K Consecutive Black Blocks

## 🔗 Problem Link
https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

## ⚡ Difficulty
Easy

## 🏷️ Topics
String, Sliding Window

---

## 🧩 Problem Summary
Given a string `blocks` of 'W' (white) and 'B' (black) characters and an integer `k`, find the minimum number of white blocks that need to be recolored to get `k` consecutive black blocks.

### 📌 Constraints
- `n == blocks.length`
- `1 <= n <= 100`
- `1 <= k <= n`
- `blocks[i]` is either 'W' or 'B'

---

## 💭 Intuition
👉 Use a sliding window of size `k`. Count the number of 'W' characters in each window — the minimum count across all windows is the answer.

---

## ⚡ Approach — Fixed-Size Sliding Window

### 🧠 Idea
- Count 'W' in the first window of size `k`.
- Slide the window: add the incoming character, remove the outgoing character.
- Track the minimum 'W' count across all windows.

---

## 💻 Code

```cpp
class Solution {
public:
    int minimumRecolors(string blocks, int k) {
        int mini = INT_MAX, curlen = 0;
        int n = blocks.size();

        // First window (from index 0 to k-1)
        for (int i = 0; i < k; i++) {
            if (blocks[i] == 'W') {
                curlen++;
            }
        }

        mini = min(mini, curlen); // Store the result for the first window

        // Slide the window over the string
        for (int i = k; i < n; i++) {
            if (blocks[i] == 'W') {
                curlen++;
            }
            if (blocks[i - k] == 'W') {
                curlen--;
            }

            mini = min(mini, curlen); // Track the minimum recolors
        }

        return mini;
    }
};
```

---

## 🧠 Dry Run
### Input
```
blocks = "WBBWWBBWBW", k = 7
```
### Steps
```
First window "WBBWWBB": W count = 3, mini = 3
Slide to "BBWWBBW": W count = 3, mini = 3
Slide to "BWWBBWB": W count = 3, mini = 3
Slide to "WWBBWBW": W count = 4, mini = 3

Result: 3
```

---

## ⏱️ Time Complexity
```
O(n) — single pass through the string.
```

## 💾 Space Complexity
```
O(1) — only a few variables.
```

---

## ⚠️ Edge Cases
- All blocks are 'B': answer is 0.
- All blocks are 'W': answer is k.
- `k == n`: only one window to check.

---

## 🎯 Interview Takeaways
- Fixed-size sliding window is the go-to for "best window of size k" problems.
- Incrementally update the window count instead of recounting.
- Simple and efficient for constraint sizes up to 10^5+.

---

## 📌 Key Pattern
👉 **"Fixed-size sliding window to find the optimal window of length k."**

---

## 🔁 Related Problems
- 1456. Maximum Number of Vowels in a Substring of Given Length
- 643. Maximum Average Subarray I
- 1052. Grumpy Bookstore Owner

---

## 🚀 Final Thoughts
A textbook sliding window problem. The key observation is that minimizing recolors is equivalent to finding the window of size k with the fewest 'W' characters.

---

✨ **Rule to remember:**
> "Slide a fixed window, track the count, and keep the minimum."
