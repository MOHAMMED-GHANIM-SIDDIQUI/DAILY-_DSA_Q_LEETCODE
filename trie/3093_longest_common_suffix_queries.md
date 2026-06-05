# 3093. Longest Common Suffix Queries

## 🔗 Problem Link
https://leetcode.com/problems/longest-common-suffix-queries/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, String, Trie

---

## 🧩 Problem Summary
You are given `wordsContainer` and `wordsQuery`. For each query string `wordsQuery[i]`, find the string in `wordsContainer` that shares the **longest common suffix** with it. If several strings tie on suffix length, pick the **shortest** such string; if still tied, pick the one with the **smallest index**. Return an array of the chosen container indices, one per query.

### 📌 Constraints
- `1 <= wordsContainer.length, wordsQuery.length <= 10^4`
- Total characters across each list up to `~5 * 10^5`.

---

## 💭 Intuition
"Longest common **suffix**" is "longest common **prefix** of the reversed strings." That immediately suggests a **Trie built on reversed words**: insert every container word reversed; to answer a query, reverse it (conceptually) and walk the trie as far as the characters match — the depth reached is the longest common suffix length.

The tie-breaking (shortest word, then smallest index) is handled by storing, **at every trie node**, the best container index seen on the path through that node — where "best" means **smallest length, then smallest index**. As we insert each word, we update this "best" along its entire reversed path **and** at the root (the root represents the empty suffix, the fallback when nothing matches).

When a query walks the trie and stops (either it runs out of characters or hits a missing branch), the `best_idx` stored at the **deepest node it reached** is the answer — it already encodes the correct tie-breaks for that suffix length.

---

## ⚡ Approach — Reversed Trie carrying best (length, index)

### 🧠 Idea
**Build:**
1. Root holds the global fallback (shortest/smallest-index word overall) — update it for every word, since every query at minimum shares the empty suffix.
2. For each container word (with index `idx`, length `wlen`), walk its characters in **reverse**, creating nodes as needed. At **each node on the path**, if `wlen < node.best_len`, overwrite `(best_len, best_idx)`.

**Query:**
1. Start at root. Walk the query's characters in **reverse**.
2. As long as the next character exists as a child, descend.
3. Stop at the first missing child (or when the query ends). Append the **current node's** `best_idx`.

### 🔑 Why store best at every node
A query may match a suffix of length `k` — it lands on the node at depth `k`. That node must already know the optimal container word among **all** words passing through it (i.e. all words sharing that `k`-suffix). Updating `best` on every node during insertion guarantees this, with ties resolved by the `wlen < best_len` comparison (strict `<` keeps the earlier/smaller index on equal length).

### 🔑 Why the root matters
The root is depth 0 — the empty suffix. If a query shares **no** suffix with anything, it stops at the root, and the root's `best_idx` (overall shortest, smallest index) is the correct answer.

---

## 💻 Code

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_idx = -1
        self.best_len = float("inf")


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        root = TrieNode()

        # Build reversed trie
        for idx, word in enumerate(wordsContainer):
            node = root
            wlen = len(word)

            # Update root best match
            if wlen < node.best_len:
                node.best_len = wlen
                node.best_idx = idx

            for ch in reversed(word):
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

                # Store shortest word index at each node
                if wlen < node.best_len:
                    node.best_len = wlen
                    node.best_idx = idx

        ans = []

        # Query
        for word in wordsQuery:
            node = root

            for ch in reversed(word):
                if ch not in node.children:
                    break
                node = node.children[ch]

            ans.append(node.best_idx)

        return ans
```

---

## 🧠 Dry Run
### Input
```
wordsContainer = ["abcd", "bcd", "xbcd"]
wordsQuery     = ["cd", "bcd", "xyz"]
```

### Build (reversed words: "dcba", "dcb", "dcbx")
```
root.best = (len 3, idx 1)   # "bcd" is shortest overall
path d → c → b nodes get best updated; "bcd" (len3) wins ties on the d,c,b chain
node[d][c][b] best → idx 1 (len 3)
```

### Queries
```
"cd" → reversed "dc": walk d, c → node[d][c].best_idx
        among {abcd,bcd,xbcd} all end in "cd"; shortest is "bcd" → 1
"bcd" → reversed "dcb": walk d,c,b → best_idx 1 ("bcd", len 3, shortest)
"xyz" → reversed "zyx": 'z' not a child of root → stop at root → root.best_idx = 1
```
Answer: `[1, 1, 1]`.

---

## ⏱️ Time Complexity
```
Build:  O(sum of |container[i]|)   — each char inserts/updates one node.
Query:  O(sum of |query[i]|)       — each char descends at most one node.
Total:  O(total characters).
```

## 💾 Space Complexity
```
O(sum of |container[i]| · Σ)   — trie nodes; Σ = alphabet (dict-backed, so sparse).
```

---

## ⚠️ Edge Cases
- **No common suffix** → query stops at the root → returns the global shortest/smallest-index word.
- **Empty query string** → loop never runs → root's best (correct fallback).
- **Empty container word `""`** → updates only the root with `len 0`, making it the universal fallback.
- **Length ties** → strict `<` in the update keeps the first (smaller index) word, satisfying the tie-break order exactly.
- **Duplicate container words** → earlier index wins via the strict comparison.

---

## 🎯 Interview Takeaways
- "Longest common **suffix**" → reverse everything → "longest common **prefix**" → **Trie**. That reframe is the unlock.
- Push the answer's selection logic **into the trie nodes**: store the best `(length, index)` at every node so queries are pure descents with `O(1)` answer extraction — no post-processing.
- The root-as-empty-suffix fallback is the easy-to-miss case; seeding `best` at the root during every insert handles "no match" for free.
- Strict `<` (not `<=`) is what enforces "smallest index on length ties" — a deliberate, load-bearing choice.

---

## 📌 Key Pattern
👉 **"Suffix queries ⇒ reversed-prefix Trie. Precompute the tie-broken best answer at every node so each query is a single descent."**

---

## 🔁 Related Problems
- 208. Implement Trie (Prefix Tree)
- 3043. Find the Length of the Longest Common Prefix
- 14. Longest Common Prefix
- 745. Prefix and Suffix Search
- 1233. Remove Sub-Folders from the Filesystem

---

## 🚀 Final Thoughts
The elegance is moving all the tie-breaking off the query path and into node metadata computed once at build time. After that, every query is just "walk the reversed string as deep as you can and read off the stored answer." The reversed-trie reframe and the root fallback are the two ideas that make it click.

---

✨ **Rule to remember:**
> Suffix problems become prefix problems by reversing. Build a Trie and bake the (tie-broken) best answer into each node during insertion — queries then reduce to a single walk that reads the precomputed result.
