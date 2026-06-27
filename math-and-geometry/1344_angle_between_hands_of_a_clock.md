# 1344. Angle Between Hands of a Clock

## 🔗 Problem Link
https://leetcode.com/problems/angle-between-hands-of-a-clock/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Math, Geometry

---

## 🧩 Problem Summary

Given two integers `hour` and `minutes`, return the smaller angle (in degrees) formed between the hour hand and the minute hand of an analog clock.

- The minute hand moves `6` degrees per minute (360 / 60).
- The hour hand moves `30` degrees per hour (360 / 12) **plus** `0.5` degrees per minute (30 / 60), because it drifts as the minutes pass.
- The final answer is the smaller of the two angles between the hands, i.e. `min(|diff|, 360 - |diff|)`.

### 📌 Constraints
- `1 <= hour <= 12`
- `0 <= minutes <= 59`

---

## 💭 Intuition

👉 A clock is just a circle of 360 degrees. Each hand sits at a fixed angular position. The minute hand depends only on the minutes; the hour hand depends on the hour **and** how far into the hour we are (the extra `minutes * 0.5`). Once we have both positions, the angle between them is the absolute difference — and since two angles always span the circle, we pick the smaller side.

---

## ⚡ Approach — Direct Angle Computation

### 🧠 Idea
- Compute `hour_angle = (hour % 12) * 30 + minutes * 0.5`. The `% 12` handles `12` o'clock wrapping to `0`, and the `minutes * 0.5` accounts for hour-hand drift.
- Compute `minute_angle = minutes * 6`.
- Take the absolute difference `diff = abs(hour_angle - minute_angle)`.
- The smaller angle is `min(diff, 360 - diff)`.

---

## 💻 Code

```python
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_angle = (hour % 12) * 30 + minutes * 0.5
        minute_angle = minutes * 6

        diff = abs(hour_angle - minute_angle)
        return min(diff, 360 - diff)
```

---

## 🧠 Dry Run

### Input
```
hour = 12, minutes = 30
```

### Steps
```
hour_angle   = (12 % 12) * 30 + 30 * 0.5 = 0 + 15 = 15.0
minute_angle = 30 * 6 = 180
diff         = abs(15.0 - 180) = 165.0
answer       = min(165.0, 360 - 165.0) = min(165.0, 195.0) = 165.0
```

At 12:30 the minute hand points straight down (180 deg) and the hour hand has crept halfway between 12 and 1 (15 deg), giving 165 degrees.

---

## ⏱️ Time Complexity
```
O(1)
```
Only a handful of arithmetic operations regardless of input.

---

## 💾 Space Complexity
```
O(1)
```
A few scalar variables, no extra data structures.

---

## ⚠️ Edge Cases
- `hour = 12`: the `% 12` maps it to `0` so the hour hand starts at the top.
- `minutes = 0`: hour hand sits exactly on the hour mark, no drift.
- Reflex angle: cases like 9:00 give `diff = 270`, and `360 - 270 = 90` correctly returns the smaller 90 degrees.
- Hands overlapping returns `0.0`.

---

## 🎯 Interview Takeaways
- Remember the hour hand is **not** static within the hour — the `minutes * 0.5` drift term is the most commonly missed detail.
- Always normalize the difference with `min(diff, 360 - diff)` to get the smaller arc.
- Using `% 12` cleanly handles the 12 → 0 wrap.

---

## 📌 Key Pattern
👉 **"Convert each hand to an absolute angular position, then take the smaller arc between them."**

---

## 🔁 Related Problems
- 1185. Day of the Week
- 2117. Abbreviating the Product of a Range
- 1979. Find Greatest Common Divisor of Array

---

## 🚀 Final Thoughts
This is a pure math problem with no algorithmic complexity — the whole challenge lies in correctly modeling the hour hand's continuous movement. Once you encode both hands as degrees on a 360-degree circle, the answer is a one-line min of the two complementary arcs.

---

✨ **Rule to remember:**
> "The hour hand moves 0.5 degrees every minute — never treat it as fixed on the hour mark."
