# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

A daily LeetCode problem-solving journal. Every solved problem is documented as a standalone markdown file with a fixed journal layout (problem link, difficulty, topics, intuition, approach, code, dry run, complexity, edge cases, takeaways, related problems). There is no build system, shared library, or inter-file dependency — each file stands alone.

## Folder Layout

Solutions live in topic / approach folders, not in the repo root:

```
arrays-and-hashing/   two-pointers/         sliding-window/
stack-and-queue/      binary-search/        linked-list/
trees/                trie/                 heap/
intervals/            greedy/               backtracking/
graphs/               union-find/           dynamic-programming/
bit-manipulation/     math-and-geometry/    strings/
matrix/               design/
```

The root keeps only `README.md` (the topic-grouped index) and `CLAUDE.md` (this file).

## File Naming Convention

`{folder}/{4-digit-problem-number}_{snake_case_problem_name}.md`

Examples:
- `dynamic-programming/3225_maximum_score_from_grid_operations.md`
- `two-pointers/0011_container_with_most_water.md`
- `trees/0110_balanced_binary_tree.md`

A second approach for the same problem is suffixed with `_v2`, e.g. `2033_minimum_operations_to_make_a_uni_value_grid_v2.md`.

## Markdown Journal Template

Every problem file follows this structure (copy from any existing file as a template):

```
# {number}. {Title}

## 🔗 Problem Link
https://leetcode.com/problems/{slug}/

## ⚡ Difficulty
Easy | Medium | Hard

## 🏷️ Topics
{comma-separated topic tags from LeetCode}

---

## 🧩 Problem Summary
…

### 📌 Constraints
…

---

## 💭 Intuition
…

---

## ⚡ Approach — {short name}

### 🧠 Idea
…

---

## 💻 Code

```python   (or ```cpp)
class Solution:
    …
```

---

## 🧠 Dry Run
…

## ⏱️ Time Complexity
…

## 💾 Space Complexity
…

## ⚠️ Edge Cases
…

## 🎯 Interview Takeaways
…

## 📌 Key Pattern
👉 **"…"**

## 🔁 Related Problems
- …

## 🚀 Final Thoughts
…

✨ **Rule to remember:**
> …
```

Code inside the markdown is reference-only — it is the same `Solution` class shape LeetCode expects (no `main()`, no imports for LeetCode-provided types like `List`, `Optional`, `ListNode`).

## When Adding a New Solution

1. **Pick the folder** by the problem's primary topic / approach. Priority order when multiple tags apply:
   `design > backtracking > trie > union-find > trees > linked-list > graphs (Graph/Topological/Dijkstra/Floyd-Warshall) > heap > stack-and-queue > sliding-window > two-pointers > binary-search > dynamic-programming > greedy > bit-manipulation > intervals > matrix (incl. grid BFS/DFS) > strings > math-and-geometry > arrays-and-hashing (default)`.
2. **Create the file** at `{folder}/{NNNN}_{snake_name}.md` using the template above.
3. **Update `README.md`** by inserting one row in the corresponding `### {Topic}` table, sorted by problem number, and bumping the total count at the bottom of the index.

## Running Solutions

There is no test framework. The code in each markdown is meant to be pasted into the LeetCode editor — no local execution harness is provided.
