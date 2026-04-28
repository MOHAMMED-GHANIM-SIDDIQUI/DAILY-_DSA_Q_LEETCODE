# 1912. Design Movie Rental System

## 🔗 Problem Link
https://leetcode.com/problems/design-movie-rental-system/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Hash Table, Design, Heap (Priority Queue), Ordered Set

---

## 🧩 Problem Summary
Design a movie rental system that supports: searching for the cheapest 5 unrented copies of a movie, renting a movie from a shop, dropping (returning) a rented movie, and reporting the cheapest 5 currently rented movies. All results must be sorted by price, then shop, then movie.

### 📌 Constraints
- `1 <= n <= 3 * 10^5`
- `1 <= entries.length <= 10^5`
- At most `10^5` total calls to `search`, `rent`, `drop`, and `report`.

---

## 💭 Intuition
👉 Use ordered sets (sorted containers) to maintain both unrented and rented movies in sorted order. A hash map maps `(shop, movie)` to price for O(1) price lookups during rent/drop operations.

---

## ⚡ Approach — Ordered Sets with Hash Map

### 🧠 Idea
- `unrented[movie]`: a sorted set of `(price, shop)` for each movie's unrented copies.
- `rented`: a sorted set of `(price, (shop, movie))` for all rented movies.
- `shopAndMovieToPrice`: hash map from `(shop, movie)` to `price`.
- `search`: return first 5 from `unrented[movie]`.
- `rent`: remove from `unrented`, add to `rented`.
- `drop`: remove from `rented`, add back to `unrented`.
- `report`: return first 5 from `rented`.

---

## 💻 Code

```cpp
class MovieRentingSystem {
 public:
  MovieRentingSystem(int n, vector<vector<int>>& entries) {
    for (const vector<int>& e : entries) {
      const int shop = e[0];
      const int movie = e[1];
      const int price = e[2];
      unrented[movie].insert({price, shop});
      shopAndMovieToPrice[{shop, movie}] = price;
    }
  }

  vector<int> search(int movie) {
    vector<int> ans;
    int i = 0;

    for (const auto& [price, shop] : unrented[movie]) {
      ans.push_back(shop);
      if (++i >= 5)
        break;
    }

    return ans;
  }

  void rent(int shop, int movie) {
    const int price = shopAndMovieToPrice[{shop, movie}];
    unrented[movie].erase({price, shop});
    rented.insert({price, {shop, movie}});
  }

  void drop(int shop, int movie) {
    const int price = shopAndMovieToPrice[{shop, movie}];
    unrented[movie].insert({price, shop});
    rented.erase({price, {shop, movie}});
  }

  vector<vector<int>> report() {
    vector<vector<int>> ans;
    int i = 0;

    for (const auto& [_, shopAndMovie] : rented) {
      ans.push_back({shopAndMovie.first, shopAndMovie.second});
      if (++i >= 5)
        break;
    }

    return ans;
  }

 private:
  struct PairHash {
    size_t operator()(const pair<int, int>& p) const {
      return p.first ^ p.second;
    }
  };

  // {movie: (price, shop)}
  unordered_map<int, set<pair<int, int>>> unrented;

  // {(shop, movie): price}
  unordered_map<pair<int, int>, int, PairHash> shopAndMovieToPrice;

  // (price, (shop, movie))
  set<pair<int, pair<int, int>>> rented;
};
```

---

## 🧠 Dry Run
### Input
```
MovieRentingSystem(3, [[0,1,5],[0,2,6],[0,3,7],[1,1,4],[1,2,7],[2,1,5]])
search(1) -> [1, 0, 2]  (prices: 4, 5, 5; shops: 1, 0, 2)
rent(0, 1)
search(1) -> [1, 2]
report() -> [[0, 1]]
```
### Steps
```
After init: unrented[1] = {(4,1), (5,0), (5,2)}
search(1): return shops [1, 0, 2] (sorted by price, then shop)
rent(0,1): remove (5,0) from unrented[1], add (5,(0,1)) to rented
search(1): unrented[1] = {(4,1), (5,2)} -> return [1, 2]
report(): rented = {(5,(0,1))} -> return [[0,1]]
```

---

## ⏱️ Time Complexity
```
search: O(log n) for set access, O(5) for iteration = O(log n)
rent/drop: O(log n) for set insertion/deletion
report: O(5) = O(1) for iteration
```

## 💾 Space Complexity
```
O(n) for all data structures
```

---

## ⚠️ Edge Cases
- No copies of a searched movie: return empty list.
- No rented movies for report: return empty list.
- Same movie at same price in different shops: sorted by shop ID.

---

## 🎯 Interview Takeaways
- Ordered sets (BSTs) are ideal when you need sorted access with efficient insert/delete.
- A price-lookup hash map avoids redundant storage and enables O(1) price retrieval.
- System design questions often combine multiple data structures.

---

## 📌 Key Pattern
👉 **"Ordered sets for maintaining sorted collections with efficient insert/delete/top-K queries"**

---

## 🔁 Related Problems
- 355. Design Twitter
- 1146. Snapshot Array
- 380. Insert Delete GetRandom O(1)

---

## 🚀 Final Thoughts
This is a complex design problem that requires carefully choosing data structures. The combination of ordered sets for sorted access and hash maps for O(1) lookups makes all operations efficient. The key insight is separating unrented (per-movie) and rented (global) into different sorted containers.

---

✨ **Rule to remember:**
> "For top-K with dynamic inserts and deletes, use ordered sets (sorted containers) instead of heaps."
