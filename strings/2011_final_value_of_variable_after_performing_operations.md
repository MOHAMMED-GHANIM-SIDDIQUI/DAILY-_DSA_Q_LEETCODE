# 2011. Final Value of Variable After Performing Operations

## 🔗 Problem Link
https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, String, Simulation

---

## 🧩 Problem Summary
Given an array of string operations (`"++X"`, `"X++"`, `"--X"`, `"X--"`), start with `X = 0` and apply each operation. Return the final value of `X`.

### 📌 Constraints
- `1 <= operations.length <= 100`
- `operations[i]` is one of `"++X"`, `"X++"`, `"--X"`, `"X--"`

---

## 💭 Intuition
👉 All four operations have the `+` or `-` character at index 1. We only need to check `op[1]` to determine whether to increment or decrement.

---

## ⚡ Approach — Check Middle Character

### 🧠 Idea
- Initialize `ans = 0`.
- For each operation, check if the character at index 1 is `'+'` or `'-'`.
- Add 1 or subtract 1 accordingly.

---

## 💻 Code

```cpp
class Solution {
 public:
  int finalValueAfterOperations(vector<string>& operations) {
    int ans = 0;

    for (const string& op : operations)
      ans += op[1] == '+' ? 1 : -1;

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
operations = ["--X", "X++", "X++"]
```
### Steps
```
op="--X": op[1]='-' → ans = 0 - 1 = -1
op="X++": op[1]='+' → ans = -1 + 1 = 0
op="X++": op[1]='+' → ans = 0 + 1 = 1
return 1
```

---

## ⏱️ Time Complexity
```
O(n), where n is the number of operations
```

## 💾 Space Complexity
```
O(1)
```

---

## ⚠️ Edge Cases
- All increments → result equals the length of the array
- All decrements → result equals the negative of the array length
- Mixed operations cancel out

---

## 🎯 Interview Takeaways
- Exploiting string structure (the middle character always determines the operation) leads to clean code.
- Ternary operators make simple branching concise.

---

## 📌 Key Pattern
👉 **"Exploit string structure — the middle character determines the operation"**

---

## 🔁 Related Problems
- 1920. Build Array from Permutation
- 1929. Concatenation of Array
- 2469. Convert the Temperature

---

## 🚀 Final Thoughts
A straightforward simulation problem. The clever observation that `op[1]` is always the sign character eliminates the need for multiple string comparisons.

---

✨ **Rule to remember:**
> In `"++X"`, `"X++"`, `"--X"`, `"X--"`, the character at index 1 is always the sign.
