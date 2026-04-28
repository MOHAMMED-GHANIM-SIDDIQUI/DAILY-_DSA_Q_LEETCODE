# 2115. Find All Possible Recipes from Given Supplies

## 🔗 Problem Link
https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Hash Table, String, Graph, Topological Sort

---

## 🧩 Problem Summary
You have `recipes` with their required `ingredients` and a list of `supplies` (infinite quantity). A recipe can be an ingredient of another recipe. Return all recipes that can be created.

### 📌 Constraints
- `n == recipes.length == ingredients.length`
- `1 <= n <= 100`
- `1 <= ingredients[i].length, supplies.length <= 100`
- `1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10`
- All values are unique strings

---

## 💭 Intuition
👉 Model recipes and their ingredient dependencies as a directed graph. Recipes with all ingredients available (supplies or already-made recipes) have in-degree 0. Use topological sort (BFS) to find all makeable recipes.

---

## ⚡ Approach — Topological Sort (Kahn's Algorithm)

### 🧠 Idea
- Build a dependency graph: for each recipe, edges go from non-supply ingredients to the recipe.
- Track in-degree for each recipe (count of non-supply ingredients).
- Initialize the BFS queue with recipes that have in-degree 0 (all ingredients are supplies).
- Process the queue: when a recipe is made, it may reduce the in-degree of other recipes that depend on it.

---

## 💻 Code

```cpp
class Solution {
 public:
  vector<string> findAllRecipes(vector<string>& recipes,
                                vector<vector<string>>& ingredients,
                                vector<string>& supplies) {
    vector<string> ans;
    unordered_set<string> suppliesSet(supplies.begin(), supplies.end());
    unordered_map<string, vector<string>> graph;
    unordered_map<string, int> inDegrees;
    queue<string> q;

    // Build the graph.
    for (int i = 0; i < recipes.size(); ++i)
      for (const string& ingredient : ingredients[i])
        if (!suppliesSet.contains(ingredient)) {
          graph[ingredient].push_back(recipes[i]);
          ++inDegrees[recipes[i]];
        }

    // Perform topological sorting.
    for (const string& recipe : recipes)
      if (!inDegrees.contains(recipe))
        q.push(recipe);

    while (!q.empty()) {
      const string u = q.front();
      q.pop();
      ans.push_back(u);
      if (!graph.contains(u))
        continue;
      for (const string& v : graph[u])
        if (--inDegrees[v] == 0)
          q.push(v);
    }

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
recipes = ["bread", "sandwich"], ingredients = [["yeast","flour"], ["bread","meat"]], supplies = ["yeast","flour","meat"]
```
### Steps
```
suppliesSet = {"yeast", "flour", "meat"}
Build graph:
  bread: "yeast" in supplies, "flour" in supplies -> inDegree[bread]=0
  sandwich: "bread" not in supplies -> graph["bread"]=["sandwich"], inDegree[sandwich]=1
            "meat" in supplies -> skip
Queue: ["bread"]
Process "bread": ans=["bread"], graph["bread"]=["sandwich"], --inDegree["sandwich"]=0 -> push
Process "sandwich": ans=["bread","sandwich"]
Return ["bread", "sandwich"]
```

---

## ⏱️ Time Complexity
```
O(n * m), where n = number of recipes and m = average number of ingredients
```

## 💾 Space Complexity
```
O(n * m) for the graph and in-degree map
```

---

## ⚠️ Edge Cases
- Circular dependencies: recipes in a cycle will never reach in-degree 0
- Recipe requires another recipe that cannot be made
- All ingredients are supplies: all recipes can be made
- A recipe is an ingredient of itself (self-loop)

---

## 🎯 Interview Takeaways
- Topological sort naturally handles dependency resolution.
- Using a set for supplies enables O(1) lookups.
- Only non-supply ingredients create edges in the dependency graph.

---

## 📌 Key Pattern
👉 **"Dependency resolution via topological sort"**

---

## 🔁 Related Problems
- 207. Course Schedule
- 210. Course Schedule II
- 802. Find Eventual Safe States

---

## 🚀 Final Thoughts
This is a classic topological sort problem dressed up as a cooking scenario. The key insight is that supplies are "given" nodes with no dependencies, and recipes form a DAG of dependencies.

---

✨ **Rule to remember:**
> When items depend on other items, model it as a DAG and use topological sort to find what can be produced.
