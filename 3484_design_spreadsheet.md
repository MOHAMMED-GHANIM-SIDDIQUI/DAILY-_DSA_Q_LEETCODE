# 3484. Design Spreadsheet

## 🔗 Problem Link
https://leetcode.com/problems/design-spreadsheet/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Hash Map, Design, String Parsing

---

## 🧩 Problem Summary
Design a spreadsheet that supports setting a cell to a value, resetting a cell to 0, and evaluating a formula of the form `=X+Y` where X and Y can be cell references or integer values.

### 📌 Constraints
- `1 <= rows <= 10^3`
- Cell references are valid column-row strings (e.g., "A1", "B2")
- Formulas are always of the form `=X+Y`

---

## 💭 Intuition
👉 Use a hash map to store cell values. For formula evaluation, split at the `+` sign and resolve each token — either parse it as an integer or look it up in the map.

---

## ⚡ Approach — HashMap with Formula Parsing

### 🧠 Idea
- Store cell values in an `unordered_map<string, int>`.
- `setCell` inserts/updates the value.
- `resetCell` sets the value to 0.
- `getValue` strips the `=`, splits on `+`, and resolves each token.

---

## 💻 Code

```cpp
class Spreadsheet {
 public:
  Spreadsheet(int rows) {}

  void setCell(string cell, int value) {
    spreadsheet[cell] = value;
  }

  void resetCell(string cell) {
    spreadsheet[cell] = 0;
  }

  int getValue(string formula) {
    const int i = formula.find('+');
    return getToken(formula.substr(1, i - 1)) + getToken(formula.substr(i + 1));
  }

 private:
  unordered_map<string, int> spreadsheet;

  int getToken(const string& token) {
    return isdigit(token[0])
               ? stoi(token)
               : (spreadsheet.contains(token) ? spreadsheet[token] : 0);
  }
};
```

---

## 🧠 Dry Run
### Input
```
["Spreadsheet","setCell","setCell","getValue","resetCell","getValue"]
[[3],["A1",10],["B2",5],["=A1+B2"],["A1"],["=A1+B2"]]
```
### Steps
```
Spreadsheet(3): initialize empty map
setCell("A1", 10): map = {"A1": 10}
setCell("B2", 5): map = {"A1": 10, "B2": 5}
getValue("=A1+B2"): getToken("A1")=10, getToken("B2")=5 -> 15
resetCell("A1"): map = {"A1": 0, "B2": 5}
getValue("=A1+B2"): getToken("A1")=0, getToken("B2")=5 -> 5
```

---

## ⏱️ Time Complexity
```
O(1) — for each operation (hash map lookups and string parsing are constant)
```

## 💾 Space Complexity
```
O(n) — where n is the number of cells that have been set
```

---

## ⚠️ Edge Cases
- Accessing a cell that was never set → returns 0
- Formula with two integer literals (e.g., `=5+3`)
- Resetting a cell and then using it in a formula

---

## 🎯 Interview Takeaways
- Design problems benefit from simplicity — a hash map is often the right choice for sparse storage.
- Parsing formulas by finding delimiters is cleaner than regex for simple formats.
- Default values (0 for unset cells) simplify boundary logic.

---

## 📌 Key Pattern
👉 **"Hash map for sparse cell storage with simple formula parsing by delimiter splitting."**

---

## 🔁 Related Problems
- 631. Design Excel Sum Formula
- 1603. Design Parking System
- 146. LRU Cache

---

## 🚀 Final Thoughts
A clean design problem where the key is choosing the right data structure (hash map for sparse storage) and keeping formula parsing simple. The `getToken` helper elegantly handles both cell references and literals.

---

✨ **Rule to remember:**
> For design problems with sparse data, use a hash map and keep parsing logic minimal with helper functions.
