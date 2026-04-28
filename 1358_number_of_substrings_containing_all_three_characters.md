# 1358. Number of Substrings Containing All Three Characters

## 🔗 Problem Link
https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Hash Table, String, Sliding Window

---

## 🧩 Problem Summary
Given a string `s` consisting only of characters `a`, `b`, and `c`, return the number of substrings that contain at least one occurrence of all three characters.

### 📌 Constraints
- `3 <= s.length <= 5 * 10^4`
- `s` only consists of `a`, `b`, or `c` characters.

---

## 💭 Intuition
👉 Use a sliding window: once a window `[left, right]` contains all three characters, every extension to the right (i.e., substrings ending at indices `right` to `n-1`) is also valid. So we add `n - right` valid substrings and shrink from the left.

---

## ⚡ Approach — Sliding Window

### 🧠 Idea
- Maintain a count array for `a`, `b`, `c`.
- Expand the window by moving `right`.
- When all three counts are positive, add `n - right` to the answer (all extensions are valid).
- Shrink from `left` to find the next minimal valid window.

---

## 💻 Code

```cpp
class Solution {
public:
    int numberOfSubstrings(string s) {
        int n = s.size();
        int ans = 0;
        vector<int> count(3, 0);  // Count for 'a', 'b', and 'c'
        int left = 0;  // Left pointer of the window

        // Iterate through the string with the right pointer
        for (int right = 0; right < n; right++) {
            // Update the count of the current character
            count[s[right] - 'a']++;

            // Check if the current window contains at least one 'a', 'b', and 'c'
            while (count[0] > 0 && count[1] > 0 && count[2] > 0) {
                // Count all valid substrings from 'left' to 'right'
                ans += (n - right);

                // Move the left pointer to reduce the window size
                count[s[left] - 'a']--;
                left++;
            }
        }

        return ans;
    }
};
```

---

## 🧠 Dry Run
### Input
```
s = "abcabc"
```
### Steps
```
right=0: count=[1,0,0] → not valid
right=1: count=[1,1,0] → not valid
right=2: count=[1,1,1] → valid → ans += 6-2=4, shrink left=0→1, count=[0,1,1]
right=3: count=[1,1,1] → valid → ans += 6-3=3, shrink left=1→2, count=[1,0,1]
right=4: count=[1,1,1] → valid → ans += 6-4=2, shrink left=2→3, count=[1,1,0]
right=5: count=[1,1,1] → valid → ans += 6-5=1, shrink left=3→4, count=[0,1,1]
Total ans = 4+3+2+1 = 10
```

---

## ⏱️ Time Complexity
```
O(n) — each character is visited at most twice (once by right, once by left)
```

## 💾 Space Complexity
```
O(1) — only a fixed-size count array of 3
```

---

## ⚠️ Edge Cases
- `s = "abc"` → only 1 valid substring
- All same characters like `"aaa"` → 0 valid substrings
- Very long string with all three characters appearing frequently

---

## 🎯 Interview Takeaways
- The "at least" condition is handled by counting extensions: `n - right`.
- Sliding window with shrink-on-valid is the standard pattern for "at least K distinct" problems.
- Fixed alphabet size means O(1) auxiliary space.

---

## 📌 Key Pattern
👉 **"Sliding window — when the window is valid, count all extensions to the right with `n - right`."**

---

## 🔁 Related Problems
- 992. Subarrays with K Different Integers
- 76. Minimum Window Substring
- 3. Longest Substring Without Repeating Characters

---

## 🚀 Final Thoughts
A clean sliding window problem. The critical trick is realizing that once `[left, right]` is valid, all substrings `[left, right..n-1]` are valid too, so add `n - right` at once.

---

✨ **Rule to remember:**
> When a window satisfies "at least" conditions, count all rightward extensions as valid.
