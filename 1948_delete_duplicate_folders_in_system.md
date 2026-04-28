# 1948. Delete Duplicate Folders in System

## 🔗 Problem Link
https://leetcode.com/problems/delete-duplicate-folders-in-system/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Hash Table, String, Trie, Design

---

## 🧩 Problem Summary
Given a list of folder paths in a file system, identify and delete all folders that have identical subtree structures. Two folders are "duplicates" if they contain the same subfolder structure. Return the remaining folder paths after deletion.

### 📌 Constraints
- `1 <= paths.length <= 2 * 10^4`
- `1 <= paths[i].length <= 500`
- `1 <= paths[i][j].length <= 10`
- Total folder names across all paths does not exceed `2 * 10^5`.

---

## 💭 Intuition
👉 Build a Trie from all paths, then serialize each subtree into a canonical string. If two or more nodes share the same subtree serialization, mark them for deletion. Finally, reconstruct the paths from the surviving nodes.

---

## ⚡ Approach — Trie + Subtree Serialization + Deletion

### 🧠 Idea
- Build a Trie from all paths.
- DFS to serialize each node's subtree into a canonical string representation.
- Group nodes by their serialization; if a group has 2+ nodes, mark all as deleted.
- DFS again to collect all remaining (non-deleted) paths.

---

## 💻 Code

```cpp
struct TrieNode {
  unordered_map<string, shared_ptr<TrieNode>> children;
  bool deleted = false;
};

class Solution {
 public:
  vector<vector<string>> deleteDuplicateFolder(vector<vector<string>>& paths) {
    vector<vector<string>> ans;
    vector<string> path;
    unordered_map<string, vector<shared_ptr<TrieNode>>> subtreeToNodes;

    ranges::sort(paths);

    for (const vector<string>& path : paths) {
      shared_ptr<TrieNode> node = root;
      for (const string& s : path) {
        if (!node->children.contains(s))
          node->children[s] = make_shared<TrieNode>();
        node = node->children[s];
      }
    }

    buildSubtreeToRoots(root, subtreeToNodes);

    for (const auto& [_, nodes] : subtreeToNodes)
      if (nodes.size() > 1)
        for (shared_ptr<TrieNode> node : nodes)
          node->deleted = true;

    constructPath(root, path, ans);
    return ans;
  }

 private:
  shared_ptr<TrieNode> root = make_shared<TrieNode>();

  string buildSubtreeToRoots(
      shared_ptr<TrieNode> node,
      unordered_map<string, vector<shared_ptr<TrieNode>>>& subtreeToNodes) {
    string subtree = "(";
    for (const auto& [s, child] : node->children)
      subtree += s + buildSubtreeToRoots(child, subtreeToNodes);
    subtree += ")";
    if (subtree != "()")
      subtreeToNodes[subtree].push_back(node);
    return subtree;
  }

  void constructPath(shared_ptr<TrieNode> node, vector<string>& path,
                     vector<vector<string>>& ans) {
    for (const auto& [s, child] : node->children)
      if (!child->deleted) {
        path.push_back(s);
        constructPath(child, path, ans);
        path.pop_back();
      }
    if (!path.empty())
      ans.push_back(path);
  }
};
```

---

## 🧠 Dry Run
### Input
```
paths = [["a"],["c"],["d"],["a","b"],["c","b"],["d","a","b"]]
```
### Steps
```
Trie structure:
  root -> a -> b
       -> c -> b
       -> d -> a -> b

Subtree serializations:
  b: "()" (leaf)
  a (under root): "(b())"
  c: "(b())"
  d: "(a(b()))"

"(b())" appears for both a and c -> mark both as deleted.

Remaining paths after deletion: [["d"],["d","a"],["d","a","b"]]
```

---

## ⏱️ Time Complexity
```
O(n * L * log(n * L)), where n is the number of paths and L is the average path length
```

## 💾 Space Complexity
```
O(n * L) for the Trie and serialization strings
```

---

## ⚠️ Edge Cases
- No duplicates: return all paths unchanged.
- All folders are duplicates: return empty.
- Nested duplicates: a deleted parent removes all its children too.

---

## 🎯 Interview Takeaways
- Trie is the natural data structure for file system problems.
- Subtree serialization for structural comparison is a powerful technique (also used in tree isomorphism).
- Three-phase approach: build, mark, reconstruct.

---

## 📌 Key Pattern
👉 **"Trie + subtree serialization for structural deduplication"**

---

## 🔁 Related Problems
- 652. Find Duplicate Subtrees
- 588. Design In-Memory File System
- 297. Serialize and Deserialize Binary Tree

---

## 🚀 Final Thoughts
This problem combines multiple advanced techniques: Trie construction, subtree serialization, and structural comparison. The serialization approach elegantly reduces the "structural equality" check to string equality. It is closely related to finding duplicate subtrees in binary trees.

---

✨ **Rule to remember:**
> "Serialize subtrees into canonical strings — identical strings mean identical structures, enabling deduplication."
