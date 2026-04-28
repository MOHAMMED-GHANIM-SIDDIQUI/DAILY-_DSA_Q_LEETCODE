# 1733. Minimum Number of People to Teach

## 🔗 Problem Link
https://leetcode.com/problems/minimum-number-of-people-to-teach/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Hash Table, Greedy

---

## 🧩 Problem Summary
Given `n` languages, a list of languages each person speaks, and a list of friendships, find the minimum number of people you need to teach a single language so that every pair of friends can communicate (share at least one common language).

### 📌 Constraints
- `2 <= n <= 500`
- `languages.length == m` (number of people)
- `1 <= m <= 500`
- `1 <= friendships.length <= 500`
- Each person speaks at least one language.

---

## 💭 Intuition
👉 Only friend pairs who currently cannot communicate need attention. Among those people, find the language already spoken by the most of them — teaching that language to the rest minimises the number of people to teach.

---

## ⚡ Approach — Greedy Language Selection

### 🧠 Idea
- Identify all friend pairs that share no common language.
- Collect all people involved in such pairs into a set `needTeach`.
- Count how many people in `needTeach` already know each language.
- The best language is the one known by the most people in `needTeach`.
- Answer = `|needTeach| - maxCount`.

---

## 💻 Code

```cpp
class Solution {
 public:
  int minimumTeachings(int n, vector<vector<int>>& languages,
                       vector<vector<int>>& friendships) {
    vector<unordered_set<int>> languageSets;
    unordered_set<int> needTeach;
    unordered_map<int, int> languageCount;

    for (const vector<int>& language : languages)
      languageSets.push_back({language.begin(), language.end()});

    // Find friends that can't communicate.
    for (const vector<int>& friendship : friendships) {
      const int u = friendship[0] - 1;
      const int v = friendship[1] - 1;
      if (cantTalk(languageSets, u, v)) {
        needTeach.insert(u);
        needTeach.insert(v);
      }
    }

    // Find the most popular language.
    for (const int u : needTeach)
      for (const int language : languageSets[u])
        ++languageCount[language];

    // Teach the most popular language to people who don't understand.
    int maxCount = 0;
    for (const auto& [_, freq] : languageCount)
      maxCount = max(maxCount, freq);

    return needTeach.size() - maxCount;
  }

 private:
  // Returns true if u can't talk with v.
  bool cantTalk(const vector<unordered_set<int>>& languageSets, int u, int v) {
    for (const int language : languageSets[u])
      if (languageSets[v].contains(language))
        return false;
    return true;
  }
};
```

---

## 🧠 Dry Run
### Input
```
n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]]
```
### Steps
```
languageSets: [{1}, {2}, {1,2}]

Friendship (0,1): {1} ∩ {2} = ∅ → can't talk → needTeach = {0,1}
Friendship (0,2): {1} ∩ {1,2} = {1} → can talk
Friendship (1,2): {2} ∩ {1,2} = {2} → can talk

needTeach = {0, 1}
Person 0 speaks {1} → languageCount[1]++
Person 1 speaks {2} → languageCount[2]++
maxCount = 1

Answer: 2 - 1 = 1
```

---

## ⏱️ Time Complexity
```
O(m * n + f * n) where m = people, n = languages, f = friendships
```

## 💾 Space Complexity
```
O(m * n) — for language sets
```

---

## ⚠️ Edge Cases
- All friends already share a language → answer is 0.
- Everyone speaks a different language → teach the most common one.
- A person appears in multiple non-communicating friendships → counted only once in `needTeach`.

---

## 🎯 Interview Takeaways
- Focus only on people involved in broken communication pairs.
- Among those people, leverage existing language knowledge to minimise teachings.
- Converting language lists to sets enables O(1) lookup for common language checks.

---

## 📌 Key Pattern
👉 **"Identify broken pairs, collect affected people, pick the most popular existing language among them"**

---

## 🔁 Related Problems
- 547. Number of Provinces
- 1319. Number of Operations to Make Network Connected
- 839. Similar String Groups

---

## 🚀 Final Thoughts
The greedy insight is to only consider people who are part of non-communicating friendships, then pick the language that minimises the teaching effort. Converting to sets and counting frequencies makes this efficient.

---

✨ **Rule to remember:**
> To minimise teachings, focus on broken pairs and teach the language that the most affected people already know.
