# 2138. Divide a String Into Groups of Size k

## 🔗 Problem Link
https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/

## ⚡ Difficulty
Easy

## 🏷️ Topics
String, Simulation

---

## 🧩 Problem Summary
Given a string `s`, an integer `k`, and a character `fill`, divide the string into groups of size `k`. If the last group has fewer than `k` characters, pad it with the `fill` character. Return the array of groups.

### 📌 Constraints
- `1 <= s.length <= 100`
- `s` consists of lowercase English letters only
- `1 <= k <= 100`
- `fill` is a lowercase English letter

---

## 💭 Intuition
👉 Simply iterate through the string in chunks of size `k`, padding the last chunk if needed.

---

## ⚡ Approach — Chunking with Padding

### 🧠 Idea
- Iterate through the string with step size `k`.
- Extract substrings of length `k`.
- If the last substring is shorter than `k`, append fill characters.

---

## 💻 Code

```cpp
class Solution {
public:
    vector<string> divideString(string s, int k, char fill) {
        vector<string> ans;
        int n = s.size();

        for (int i = 0; i < n; i += k) {
            string chunk = s.substr(i, k);
            if (chunk.size() < k) {
                chunk += string(k - chunk.size(), fill);
            }
            ans.push_back(chunk);
        }

        return ans;
    }
};
```

---

## 🧠 Dry Run
### Input
```
s = "abcdefghi", k = 3, fill = 'x'
```
### Steps
```
i=0: chunk = "abc" (size 3, no padding) -> ans = ["abc"]
i=3: chunk = "def" (size 3, no padding) -> ans = ["abc","def"]
i=6: chunk = "ghi" (size 3, no padding) -> ans = ["abc","def","ghi"]
Return ["abc","def","ghi"]
```

---

## ⏱️ Time Complexity
```
O(n), where n is the length of s
```

## 💾 Space Complexity
```
O(n) for the output array
```

---

## ⚠️ Edge Cases
- String length is a multiple of k: no padding needed
- String length < k: single group with padding
- k = 1: each character is its own group
- k >= string length: single padded group

---

## 🎯 Interview Takeaways
- Simple string manipulation problem.
- `substr` with a length parameter handles the boundary naturally.
- Padding with `string(count, char)` is clean and concise.

---

## 📌 Key Pattern
👉 **"Chunk a string with step size k, pad the last chunk"**

---

## 🔁 Related Problems
- 68. Text Justification
- 6. Zigzag Conversion
- 1816. Truncate Sentence

---

## 🚀 Final Thoughts
A straightforward simulation problem. The key is handling the last chunk correctly when the string length is not divisible by k.

---

✨ **Rule to remember:**
> When chunking a string, always check if the last chunk needs padding.
