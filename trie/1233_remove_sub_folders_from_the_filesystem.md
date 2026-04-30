# 1233. Remove Sub-Folders from the Filesystem

## 🔗 Problem Link
https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, String, Sorting, Trie

---

## 🧩 Problem Summary

Given a list of folder paths, remove all sub-folders and return the remaining folders in any order. A folder `b` is a sub-folder of `a` if `b` starts with `a` followed by a `/`.

### 📌 Constraints
- `1 <= folder.length <= 4 * 10^4`
- `2 <= folder[i].length <= 100`
- `folder[i]` starts with `/` and contains only lowercase letters and `/`.

---

## 💭 Intuition

👉 If we sort the folders lexicographically, any sub-folder will immediately follow its parent. We just need to track the last "kept" folder and skip anything that starts with it + `/`.

---

## ⚡ Approach — Sort and Prefix Check

### 🧠 Idea
- Sort the folder list lexicographically.
- Iterate through the sorted list, maintaining the last accepted parent folder.
- If the current folder starts with `prev + "/"`, it's a sub-folder — skip it.
- Otherwise, accept it and update `prev`.

---

## 💻 Code

```cpp
class Solution {
 public:
  vector<string> removeSubfolders(vector<string>& folder) {
    vector<string> ans;
    string prev;

    ranges::sort(folder);

    for (const string& f : folder) {
      if (!prev.empty() && f.find(prev) == 0 && f[prev.length()] == '/')
        continue;
      ans.push_back(f);
      prev = f;
    }

    return ans;
  }
};
```

---

## 🧠 Dry Run

### Input
```
folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
```

### Steps
```
After sort: ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]

"/a"    → prev is empty → accept, prev="/a", ans=["/a"]
"/a/b"  → starts with "/a" + "/" → skip (sub-folder)
"/c/d"  → doesn't start with "/a/" → accept, prev="/c/d", ans=["/a","/c/d"]
"/c/d/e"→ starts with "/c/d" + "/" → skip (sub-folder)
"/c/f"  → starts with "/c/" but not "/c/d/" → accept, prev="/c/f", ans=["/a","/c/d","/c/f"]

Output: ["/a","/c/d","/c/f"]
```

---

## ⏱️ Time Complexity
```
O(n * m * log n)
```
Where `n` is the number of folders and `m` is the maximum folder path length. Sorting dominates.

---

## 💾 Space Complexity
```
O(1)
```
Excluding the output, only one string variable `prev` is used.

---

## ⚠️ Edge Cases
- No sub-folders → return all folders.
- All folders are sub-folders of one root → return only the root.
- Similar prefixes like `/a` and `/ab` — the `/` check prevents false matches.

---

## 🎯 Interview Takeaways
- Sorting makes parent folders appear before their sub-folders.
- Checking for `/` after the prefix prevents false positives (e.g., `/a` vs `/ab`).
- This is simpler and more space-efficient than a Trie-based approach.
- The `find(prev) == 0` idiom checks for prefix matching.

---

## 📌 Key Pattern
👉 **"Sort + prefix tracking — after sorting, sub-folders always follow their parents, so one pass suffices."**

---

## 🔁 Related Problems
- 14 - Longest Common Prefix
- 588 - Design In-Memory File System
- 1166 - Design File System

---

## 🚀 Final Thoughts
An elegant sorting-based solution that avoids building a Trie. The crucial detail is the `/` boundary check to distinguish genuine sub-folders from similarly named folders.

---

✨ **Rule to remember:**
> "Sort folder paths lexicographically — sub-folders always come right after their parent, making one-pass filtering possible."
