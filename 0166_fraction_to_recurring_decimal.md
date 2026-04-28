# 166. Fraction to Recurring Decimal

## 🔗 Problem Link
https://leetcode.com/problems/fraction-to-recurring-decimal/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Hash Table, Math, String

---

## 🧩 Problem Summary

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format. If the fractional part is repeating, enclose the repeating part in parentheses. For example, `1/3 = "0.(3)"` and `2/1 = "2"`.

### 📌 Constraints
- `-2^31 <= numerator, denominator <= 2^31 - 1`
- `denominator != 0`

---

## 💭 Intuition

👉 Long division by hand reveals the pattern: a repeating decimal occurs when the same remainder appears again during division. By tracking remainders and their positions in a hash map, we can detect the start of the repeating cycle and insert parentheses accordingly.

---

## ⚡ Approach — Long Division with Remainder Tracking

### 🧠 Idea

- Handle the sign separately using XOR on the signs of numerator and denominator.
- Compute the integer part using `n / d`.
- Perform long division for the fractional part: multiply remainder by 10, divide, track the new remainder.
- Use a hash map to record each remainder and its position in the result string.
- When a previously seen remainder appears, insert `(` at the stored position and append `)`.

---

## 💻 Code

```cpp
#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {
        if (numerator == 0) return "0";

        string result;

        // Handle sign
        if ((numerator < 0) ^ (denominator < 0)) result += "-";

        // Convert to long to avoid overflow
        long n = labs((long)numerator);
        long d = labs((long)denominator);

        // Integer part
        result += to_string(n / d);
        long remainder = n % d;

        if (remainder == 0) return result; // no fractional part

        result += ".";

        unordered_map<long, int> seen; // remainder -> position in result

        while (remainder != 0) {
            if (seen.count(remainder)) {
                // Insert "(" at the first occurrence
                result.insert(seen[remainder], "(");
                result += ")";
                break;
            }

            seen[remainder] = result.size();

            remainder *= 10;
            result += to_string(remainder / d);
            remainder %= d;
        }

        return result;
    }
};
```

---

## 🧠 Dry Run

### Input
```
numerator = 1, denominator = 6
```

### Steps
```
Sign: positive
Integer part: 1/6 = 0, remainder = 1
Result so far: "0."

Iteration 1: remainder=1, not seen, seen={1:2}
  1*10=10, 10/6=1, remainder=10%6=4
  result = "0.1"

Iteration 2: remainder=4, not seen, seen={1:2, 4:3}
  4*10=40, 40/6=6, remainder=40%6=4
  result = "0.16"

Iteration 3: remainder=4, seen at position 3!
  Insert "(" at position 3: "0.1(6"
  Append ")": "0.1(6)"

Return "0.1(6)"
```

---

## ⏱️ Time Complexity

```
O(d)
```

Where d is the denominator. The number of unique remainders is at most `d-1`, so the loop runs at most `d` times before a repeat is found.

---

## 💾 Space Complexity

```
O(d)
```

The hash map stores at most `d-1` remainders.

---

## ⚠️ Edge Cases

- **Zero numerator:** `0 / 5` → `"0"`
- **Negative result:** `-1 / 2` → `"-0.5"`
- **Integer overflow:** `numerator = -2^31, denominator = 1` — handled by converting to `long`
- **No fractional part:** `4 / 2` → `"2"`

---

## 🎯 Interview Takeaways

- This is essentially simulating long division — a process everyone learned in school but rarely codes.
- Remainder tracking with a hash map is the key to detecting repeating cycles.
- Watch out for integer overflow when `numerator = INT_MIN` — always cast to `long` first.
- XOR trick for sign handling: `(a < 0) ^ (b < 0)` detects mixed signs.

---

## 📌 Key Pattern

👉 **"Simulate long division, track remainders in a hash map to detect repeating cycles."**

---

## 🔁 Related Problems

- 29. Divide Two Integers
- 2. Add Two Numbers
- 592. Fraction Addition and Subtraction
- 972. Equal Rational Numbers

---

## 🚀 Final Thoughts

Fraction to Recurring Decimal is a great math simulation problem. The remainder-tracking technique is the core idea and has applications beyond this specific problem, such as detecting cycles in sequences.

---

✨ **Rule to remember:**
> "A decimal repeats when the same remainder appears twice — track remainders to find the cycle."
