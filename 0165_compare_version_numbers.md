# 165. Compare Version Numbers

## 🔗 Problem Link
https://leetcode.com/problems/compare-version-numbers/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Two Pointers, String

---

## 🧩 Problem Summary

Given two version strings `version1` and `version2`, compare them. Version strings consist of revision numbers separated by dots. Compare revision by revision from left to right. If a version has fewer revisions, treat missing revisions as `0`. Return `-1` if `version1 < version2`, `1` if `version1 > version2`, and `0` if they are equal.

### 📌 Constraints
- `1 <= version1.length, version2.length <= 500`
- `version1` and `version2` only contain digits and `'.'`
- `version1` and `version2` are valid version numbers
- All given revisions can be stored in a 32-bit integer

---

## 💭 Intuition

👉 Use string streams to parse each revision number separated by dots. Compare them one by one. If one string runs out of revisions, default to 0. This approach handles unequal revision counts naturally (e.g., "1.0" vs "1").

---

## ⚡ Approach — Stream Parsing

### 🧠 Idea

- Use `istringstream` to read integers from each version string, separated by dots.
- In each iteration, extract one revision from each stream (defaulting to 0 if exhausted).
- Compare the two revisions; return -1 or 1 on mismatch.
- If all revisions match, return 0.

---

## 💻 Code

```cpp
class Solution {
 public:
  int compareVersion(string version1, string version2) {
    istringstream iss1(version1);
    istringstream iss2(version2);
    int v1;
    int v2;
    char dotChar;

    while (bool(iss1 >> v1) + bool(iss2 >> v2)) {
      if (v1 < v2)
        return -1;
      if (v1 > v2)
        return 1;
      iss1 >> dotChar;
      iss2 >> dotChar;
      v1 = 0;
      v2 = 0;
    }

    return 0;
  };
};
```

---

## 🧠 Dry Run

### Input
```
version1 = "1.01", version2 = "1.001"
```

### Steps
```
Iteration 1:
  iss1 >> v1 → v1=1 (success), iss2 >> v2 → v2=1 (success)
  v1 == v2, continue
  Read dot from both streams
  Reset v1=0, v2=0

Iteration 2:
  iss1 >> v1 → v1=1 (reads "01"), iss2 >> v2 → v2=1 (reads "001")
  v1 == v2, continue
  Read dot fails (end of stream)
  Reset v1=0, v2=0

Iteration 3:
  Both streams exhausted, bool(iss1>>v1)=0, bool(iss2>>v2)=0
  0 + 0 = 0 → loop ends

Return 0
```

---

## ⏱️ Time Complexity

```
O(n + m)
```

Where n and m are the lengths of the two version strings. Each character is processed once.

---

## 💾 Space Complexity

```
O(n + m)
```

For the two `istringstream` objects.

---

## ⚠️ Edge Cases

- **Trailing zeros:** `"1.0"` vs `"1"` → equal (return 0)
- **Leading zeros in revisions:** `"1.01"` vs `"1.1"` → equal (01 is parsed as 1)
- **Different lengths:** `"1.0.0"` vs `"1"` → equal

---

## 🎯 Interview Takeaways

- String stream parsing elegantly handles variable-length dot-separated tokens.
- Defaulting to 0 when one version runs out simplifies unequal-length comparisons.
- The `bool(stream >> var)` idiom checks success and extracts in one expression.
- This problem tests careful handling of edge cases more than algorithm design.

---

## 📌 Key Pattern

👉 **"Parse dot-separated tokens with streams, compare pairwise, default missing parts to zero."**

---

## 🔁 Related Problems

- 8. String to Integer (atoi)
- 43. Multiply Strings
- 67. Add Binary
- 415. Add Strings

---

## 🚀 Final Thoughts

Compare Version Numbers is a string-parsing problem where the trick is handling different revision counts and leading zeros. Stream-based parsing in C++ makes the solution clean and concise.

---

✨ **Rule to remember:**
> "Version comparison = tokenize by dots, compare integers pairwise, pad the shorter one with zeros."
