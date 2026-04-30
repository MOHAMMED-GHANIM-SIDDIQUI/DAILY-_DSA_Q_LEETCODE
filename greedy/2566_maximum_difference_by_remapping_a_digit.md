# 2566. Maximum Difference by Remapping a Digit

## 🔗 Problem Link
https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Math, Greedy, String

---

## 🧩 Problem Summary
Given an integer `num`, you can remap exactly one digit `d` to another digit `d'` (all occurrences of `d` become `d'`). You perform two remappings: one to maximize and one to minimize the resulting number. Return the difference between the maximum and minimum values.

### 📌 Constraints
- `1 <= num <= 10^8`

---

## 💭 Intuition
👉 To maximize: find the first digit that isn't 9 and remap it to 9. To minimize: remap the first digit to 0 (leading zeros are allowed for minimum).

---

## ⚡ Approach — Greedy Digit Remapping

### 🧠 Idea
- Convert `num` to string.
- For maximum: find the first non-9 digit, remap all occurrences of that digit to 9.
- For minimum: remap all occurrences of the first digit to 0.
- Return `max - min`.

---

## 💻 Code

```cpp
class Solution {
 public:
  int minMaxDifference(int num) {
    const string s = to_string(num);
    const char to9 = s[firstNotNineIndex(s)];
    const char to0 = s[0];
    return getMax(s, to9) - getMin(s, to0);
  }

 private:
  int firstNotNineIndex(const string& s) {
    for (int i = 0; i < s.length(); ++i)
      if (s[i] != '9')
        return i;
    return 0;
  }

  int getMax(string s, char to9) {
    for (char& c : s)
      if (c == to9)
        c = '9';
    return stoi(s);
  }

  int getMin(string s, char to0) {
    for (char& c : s)
      if (c == to0)
        c = '0';
    return stoi(s);
  }
};
```

---

## 🧠 Dry Run
### Input
```
num = 11891
```
### Steps
```
s = "11891"
firstNotNineIndex: s[0]='1' != '9', return 0 => to9 = '1'
to0 = s[0] = '1'

getMax("11891", '1'): replace '1' with '9' => "99899" => 99899
getMin("11891", '1'): replace '1' with '0' => "00890" => 890

Answer = 99899 - 890 = 99009
```

---

## ⏱️ Time Complexity
```
O(log(num)) — proportional to the number of digits
```

## 💾 Space Complexity
```
O(log(num))
```

---

## ⚠️ Edge Cases
- `num` is already all 9s (e.g., 999): max = 999, min = 0, diff = 999
- Single digit number
- All digits are the same

---

## 🎯 Interview Takeaways
- Greedy choice for maximizing: remap the first non-9 digit to 9.
- Greedy choice for minimizing: remap the leading digit to 0.
- Leading zeros are handled naturally by `stoi`.

---

## 📌 Key Pattern
👉 **"Greedy digit manipulation — remap to extremes (9 for max, 0 for min)"**

---

## 🔁 Related Problems
- 1432. Max Difference You Can Get From Changing an Integer
- 2578. Split With Minimum Sum

---

## 🚀 Final Thoughts
A straightforward greedy problem. The key observation is that remapping a digit affects all its occurrences, so targeting the most impactful digit (first non-9 for max, first digit for min) gives optimal results.

---

✨ **Rule to remember:**
> To maximize a number by digit remapping, turn the first non-9 digit into 9; to minimize, turn the leading digit into 0.
