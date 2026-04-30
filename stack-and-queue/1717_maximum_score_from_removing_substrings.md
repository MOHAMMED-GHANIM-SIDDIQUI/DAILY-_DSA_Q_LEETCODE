# 1717. Maximum Score From Removing Substrings

## 🔗 Problem Link
https://leetcode.com/problems/maximum-score-from-removing-substrings/

## ⚡ Difficulty
Medium

## 🏷️ Topics
String, Stack, Greedy

---

## 🧩 Problem Summary
Given a string `s` and two integers `x` and `y`, you gain `x` points for removing substring `"ab"` and `y` points for removing `"ba"`. You can apply these operations any number of times. Return the maximum score.

### 📌 Constraints
- `1 <= s.length <= 10^5`
- `1 <= x, y <= 10^4`
- `s` consists of lowercase English letters.

---

## 💭 Intuition
👉 Greedily remove the higher-value substring first. After removing all instances of the more valuable pair, remove the remaining instances of the less valuable pair. A stack efficiently simulates this removal process.

---

## ⚡ Approach — Greedy Two-Pass Stack

### 🧠 Idea
- If `x > y`, remove all `"ab"` first (higher value), then remove `"ba"` from the leftovers.
- If `y >= x`, remove all `"ba"` first, then `"ab"`.
- Use a stack for each pass: push characters, and whenever the top of the stack plus the current character forms the target pair, pop and add points.

---

## 💻 Code

```cpp
class Solution {
 public:
  int maximumGain(string s, int x, int y) {
    // The assumption that gain("ab") > gain("ba") while removing "ba" first is
    // optimal is contradicted. Only "b(ab)a" satisfies the condition of
    // preventing two "ba" removals, but after removing "ab", we can still
    // remove one "ba", resulting in a higher gain. Thus, removing "ba" first is
    // not optimal.
    return x > y ? gain(s, "ab", x, "ba", y) : gain(s, "ba", y, "ab", x);
  }

 private:
  // Returns the points gained by first removing sub1 ("ab" | "ba") from s with
  // point1, then removing sub2 ("ab" | "ba") from s with point2.
  int gain(const string& s, const string& sub1, int point1, const string& sub2,
           int point2) {
    int points = 0;
    vector<char> stack1;
    vector<char> stack2;

    // Remove "sub1" from s with point1 gain.
    for (const char c : s)
      if (!stack1.empty() && stack1.back() == sub1[0] && c == sub1[1]) {
        stack1.pop_back();
        points += point1;
      } else {
        stack1.push_back(c);
      }

    // Remove "sub2" from s with point2 gain.
    for (const char c : stack1)
      if (!stack2.empty() && stack2.back() == sub2[0] && c == sub2[1]) {
        stack2.pop_back();
        points += point2;
      } else {
        stack2.push_back(c);
      }

    return points;
  }
};
```

---

## 🧠 Dry Run
### Input
```
s = "cdbcbbaaabab", x = 4, y = 5
```
### Steps
```
Since y > x, remove "ba" first (5 pts each), then "ab" (4 pts each).

Pass 1 — remove "ba":
Stack processes: c,d,b→c,d then 'a' matches 'b' → pop, +5
Continue... collect remaining characters.

Pass 2 — remove "ab" from leftovers:
Match remaining "ab" pairs, +4 each.

Total: maximized score.
```

---

## ⏱️ Time Complexity
```
O(n) — two linear passes through the string
```

## 💾 Space Complexity
```
O(n) — stack can hold up to n characters
```

---

## ⚠️ Edge Cases
- String contains no `'a'` or no `'b'` → score is 0.
- `x == y` → order doesn't matter, either pair first works.
- String with only `'a'` and `'b'` characters → maximum possible removals.

---

## 🎯 Interview Takeaways
- Greedy ordering matters: always process the higher-value operation first.
- Stack-based string reduction is a versatile pattern for pair-removal problems.
- The proof that greedy works here: removing the cheaper pair first can block more expensive removals, but not vice versa.

---

## 📌 Key Pattern
👉 **"Greedy two-pass stack: remove the higher-value pair first, then the lower-value pair from leftovers"**

---

## 🔁 Related Problems
- 1653. Minimum Deletions to Make String Balanced
- 1003. Check If Word Is Valid After Substitutions
- 2000. Reverse Prefix of Word

---

## 🚀 Final Thoughts
The greedy insight is the core challenge: prioritise the more valuable removal. The stack makes the actual removal process linear and elegant. A great example of combining greedy strategy with stack-based simulation.

---

✨ **Rule to remember:**
> When two competing pair-removals have different values, always greedily remove the more valuable pair first — it never hurts.
