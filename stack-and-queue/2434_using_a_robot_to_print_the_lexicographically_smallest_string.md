# 2434. Using a Robot to Print the Lexicographically Smallest String

## 🔗 Problem Link
https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Hash Table, String, Stack, Greedy

---

## 🧩 Problem Summary
A robot has string `s` on paper and an empty string `t`. It can take the first character of `s` and push it onto `t`, or pop the top of `t` and write it. Return the lexicographically smallest string the robot can write.

### 📌 Constraints
- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters.

---

## 💭 Intuition
👉 Use a stack for `t`. Push characters from `s` onto the stack. Pop from the stack whenever the top is <= the smallest remaining character in `s`. This ensures we never hold back a character that should be output first.

---

## ⚡ Approach — Greedy Stack with Remaining Character Count

### 🧠 Idea
- Count the frequency of each character in `s`.
- Push characters from `s` onto a stack, decrementing their count.
- After each push, compute the smallest character still remaining in `s`.
- Pop from the stack while the top <= that smallest remaining character.

---

## 💻 Code

```cpp
class Solution {
 public:
  string robotWithString(string s) {
    string ans;
    vector<int> count(26);
    stack<char> stack;

    for (const char c : s)
      ++count[c - 'a'];

    for (const char c : s) {
      stack.push(c);
      --count[c - 'a'];
      const char minChar = getMinChar(count);
      while (!stack.empty() && stack.top() <= minChar)
        ans += stack.top(), stack.pop();
    }

    while (!stack.empty())
      ans += stack.top(), stack.pop();

    return ans;
  }

 private:
  char getMinChar(const vector<int>& count) {
    for (int i = 0; i < 26; ++i)
      if (count[i])
        return 'a' + i;
    return 'a';
  }
};
```

---

## 🧠 Dry Run
### Input
```
s = "zza"
```
### Steps
```
count = {z:2, a:1}
Push 'z', count={z:1,a:1}, minChar='a'. stack=['z'], 'z'>'a' → don't pop.
Push 'z', count={z:0,a:1}, minChar='a'. stack=['z','z'], 'z'>'a' → don't pop.
Push 'a', count={z:0,a:0}, minChar='a'. stack=['z','z','a'].
  top='a'<='a' → pop 'a'. ans="a". stack=['z','z'].
  top='z'<='a'? No. Stop.
Empty stack: pop 'z','z'. ans="azz".

Result: "azz"
```

---

## ⏱️ Time Complexity
```
O(n * 26) = O(n) — each character pushed/popped once, getMinChar is O(26).
```

## 💾 Space Complexity
```
O(n) — stack can hold all characters.
```

---

## ⚠️ Edge Cases
- Already sorted string: output directly.
- Reverse sorted string: all pushed to stack, then popped.
- All same characters.

---

## 🎯 Interview Takeaways
- Greedy with a stack: pop when the stack top is "safe" (no smaller character coming later).
- Tracking remaining character frequencies enables O(1) decisions on when to pop.
- This pattern appears in many "lexicographically smallest result" problems.

---

## 📌 Key Pattern
👉 **"Greedy stack: pop when the top is <= the smallest character still to come."**

---

## 🔁 Related Problems
- 316. Remove Duplicate Letters
- 402. Remove K Digits
- 321. Create Maximum Number

---

## 🚀 Final Thoughts
This problem is a clever application of the greedy stack pattern. The key insight is that you should pop from the stack whenever the top character is no worse than anything remaining in the input.

---

✨ **Rule to remember:**
> "Pop the stack greedily when its top is <= the smallest remaining character."
