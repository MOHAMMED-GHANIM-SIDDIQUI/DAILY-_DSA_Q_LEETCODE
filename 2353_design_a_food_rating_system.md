# 2353. Design a Food Rating System

## 🔗 Problem Link
https://leetcode.com/problems/design-a-food-rating-system/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Hash Table, Design, Ordered Set, Heap (Priority Queue)

---

## 🧩 Problem Summary
Design a food rating system that supports modifying the rating of a food item and querying the highest-rated food for a given cuisine. On ties, return the lexicographically smallest food name.

### 📌 Constraints
- `1 <= n <= 2 * 10^4`
- `n == foods.length == cuisines.length == ratings.length`
- `1 <= foods[i].length, cuisines[i].length <= 10`
- `1 <= ratings[i] <= 10^8`
- At most `2 * 10^4` calls to `changeRating` and `highestRated`.

---

## 💭 Intuition
👉 Use an ordered set (std::set) per cuisine storing `(-rating, food)` pairs. Negative rating ensures highest rating comes first, and lexicographic ordering breaks ties naturally.

---

## ⚡ Approach — Ordered Set with Hash Maps

### 🧠 Idea
- Map each cuisine to a `set<pair<int, string>>` of `(-rating, food)`.
- Map each food to its cuisine and current rating.
- On `changeRating`: remove old `(-oldRating, food)`, insert new `(-newRating, food)`.
- On `highestRated`: return the second element of the set's first entry (smallest `-rating` = highest rating).

---

## 💻 Code

```cpp
class FoodRatings {
 public:
  FoodRatings(vector<string>& foods, vector<string>& cuisines,
              vector<int>& ratings) {
    for (int i = 0; i < foods.size(); ++i) {
      cuisineToRatingAndFoods[cuisines[i]].insert({-ratings[i], foods[i]});
      foodToCuisine[foods[i]] = cuisines[i];
      foodToRating[foods[i]] = ratings[i];
    }
  }

  void changeRating(string food, int newRating) {
    const string cuisine = foodToCuisine[food];
    const int oldRating = foodToRating[food];
    auto& ratingAndFoods = cuisineToRatingAndFoods[cuisine];
    ratingAndFoods.erase({-oldRating, food});
    ratingAndFoods.insert({-newRating, food});
    foodToRating[food] = newRating;
  }

  string highestRated(string cuisine) {
    return cuisineToRatingAndFoods[cuisine].begin()->second;
  }

 private:
  // {cuisine: {(-rating, food)}} stores negative rating for smarter comparison
  unordered_map<string, set<pair<int, string>>> cuisineToRatingAndFoods;
  unordered_map<string, string> foodToCuisine;
  unordered_map<string, int> foodToRating;
};
```

---

## 🧠 Dry Run
### Input
```
["FoodRatings","highestRated","changeRating","highestRated"]
[[["kimchi","miso","sushi"],["korean","japanese","japanese"],[9,12,8]],["japanese"],["sushi",16],["japanese"]]
```
### Steps
```
Init: korean={(-9,"kimchi")}, japanese={(-12,"miso"),(-8,"sushi")}
highestRated("japanese") → begin()=(-12,"miso") → "miso"
changeRating("sushi",16): remove (-8,"sushi"), insert (-16,"sushi")
  japanese={(-16,"sushi"),(-12,"miso")}
highestRated("japanese") → begin()=(-16,"sushi") → "sushi"
```

---

## ⏱️ Time Complexity
```
Constructor: O(n log n)
changeRating: O(log n)
highestRated: O(1)
```

## 💾 Space Complexity
```
O(n) — storing all food entries in maps and sets.
```

---

## ⚠️ Edge Cases
- Multiple foods with same rating in same cuisine: return lexicographically smallest.
- Rating changes that don't change the top food.
- Single food in a cuisine.

---

## 🎯 Interview Takeaways
- Negating ratings in an ordered set elegantly handles "max first, then lex smallest" ordering.
- `std::set` provides O(log n) insert/erase and O(1) access to the first element.
- Hash maps for reverse lookups (food → cuisine, food → rating) enable efficient updates.

---

## 📌 Key Pattern
👉 **"Negate values in an ordered set to simulate a max-heap with lexicographic tie-breaking."**

---

## 🔁 Related Problems
- 1845. Seat Reservation Manager
- 1882. Process Tasks Using Servers
- 2349. Design a Number Container System

---

## 🚀 Final Thoughts
The negative-rating trick in an ordered set is a classic technique. Combined with hash maps for O(1) lookups, this design achieves optimal time complexity for all operations.

---

✨ **Rule to remember:**
> "Negate the priority in an ordered set to get max-first ordering with natural tie-breaking."
