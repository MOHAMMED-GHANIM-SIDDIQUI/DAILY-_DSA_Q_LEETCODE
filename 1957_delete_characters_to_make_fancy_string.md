# 1957. Delete Characters to Make Fancy String

## 🔗 Problem Link
https://leetcode.com/problems/delete-characters-to-make-fancy-string/

## ⚡ Difficulty
Easy

## 🏷️ Topics
String

---

## 🧩 Problem Summary
A "fancy" string has no three consecutive equal characters. Given a string `s`, delete the minimum number of characters to make it fancy, and return the result.

### 📌 Constraints
- `1 <= s.length <= 10^5`
- `s` consists only of lowercase English letters.

---

## 💭 Intuition
👉 Simply iterate through the string, tracking consecutive character counts. Only append a character to the result if the consecutive count is less than 3. This ensures no three identical characters appear in a row.

---

## ⚡ Approach — Greedy Single Pass

### 🧠 Idea
- Track the previous character and a running count of consecutive occurrences.
- For each character, if it matches the previous, increment the count; otherwise reset to 1.
- Only add the character to the result if the count is less than 3.

---

## 💻 Code

```cpp
class Solution {
public:
    string makeFancyString(string s) {
        int n=s.size();
        if(n==0)
        return "";
        string ans="";
        ans+=s[0];
        char prev=s[0];
        int cnt=1;
        for(int i=1;i<n;i++)
        {

            if(s[i]==prev)
            {
                cnt++;
                if(cnt<3)
                ans+=s[i];

            }
            else
            {
                prev=s[i];
                ans+=s[i];
                cnt=1;
            }
            if(cnt==3)
            {
                 cnt--;
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
s = "leeetcode"
```
### Steps
```
i=0: ans="l", prev='l', cnt=1
i=1: 'e'!='l' -> ans="le", prev='e', cnt=1
i=2: 'e'=='e' -> cnt=2, cnt<3 -> ans="lee"
i=3: 'e'=='e' -> cnt=3, cnt>=3 -> skip. cnt reset to 2
i=4: 't'!='e' -> ans="leet", prev='t', cnt=1
i=5: 'c'!='t' -> ans="leetc", cnt=1
i=6: 'o'!='c' -> ans="leetco", cnt=1
i=7: 'd'!='o' -> ans="leetcod", cnt=1
i=8: 'e'!='d' -> ans="leetcode", cnt=1

Result: "leetcode"
```

---

## ⏱️ Time Complexity
```
O(n), single pass through the string
```

## 💾 Space Complexity
```
O(n) for the result string
```

---

## ⚠️ Edge Cases
- Empty string: return `""`.
- All same characters (e.g., "aaaa"): return "aa".
- Already fancy: return unchanged.
- Length 1 or 2: always already fancy.

---

## 🎯 Interview Takeaways
- Consecutive-character problems are naturally solved with a running count.
- Greedy approach works because we only need to limit runs to length 2.
- Building a new string is cleaner than in-place deletion for this type of problem.

---

## 📌 Key Pattern
👉 **"Cap consecutive runs at a maximum length using a counter during single-pass construction"**

---

## 🔁 Related Problems
- 1047. Remove All Adjacent Duplicates In String
- 1209. Remove All Adjacent Duplicates in String II
- 26. Remove Duplicates from Sorted Array

---

## 🚀 Final Thoughts
This is a simple greedy string problem. The key is maintaining a count of consecutive identical characters and skipping any character that would create a run of three or more. It is a good warm-up problem for string manipulation.

---

✨ **Rule to remember:**
> "Track consecutive count; skip the character when it would create three in a row."
