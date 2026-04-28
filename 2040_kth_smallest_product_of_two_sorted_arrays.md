# 2040. Kth Smallest Product of Two Sorted Arrays

## 🔗 Problem Link
https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Binary Search, Two Pointers

---

## 🧩 Problem Summary
Given two sorted arrays `nums1` and `nums2`, and an integer `k`, return the k-th smallest product `nums1[i] * nums2[j]`. The arrays may contain negative numbers, zero, and positive numbers.

### 📌 Constraints
- `1 <= nums1.length, nums2.length <= 5 * 10^4`
- `-10^5 <= nums1[i], nums2[j] <= 10^5`
- `1 <= k <= nums1.length * nums2.length`
- `nums1` and `nums2` are sorted in non-decreasing order

---

## 💭 Intuition
👉 Binary search on the answer. For a given value `m`, count how many products are <= `m`. Separate negative and positive numbers to handle sign changes correctly.

---

## ⚡ Approach — Binary Search + Two Pointers with Sign Separation

### 🧠 Idea
- Separate each array into negatives (absolute values, reversed) and non-negatives.
- Count total negative products. If `k <= negCount`, search for the k-th negative product (by finding the (negCount - k + 1)-th absolute value of negative products).
- Otherwise, search for the (k - negCount)-th positive product.
- Binary search on the answer value `m`, using a two-pointer count function.

---

## 💻 Code

```cpp
class Solution {
 public:
  long long kthSmallestProduct(vector<int>& nums1, vector<int>& nums2,
                               long long k) {
    vector<int> A1;
    vector<int> A2;
    vector<int> B1;
    vector<int> B2;

    seperate(nums1, A1, A2);
    seperate(nums2, B1, B2);

    const long negCount = A1.size() * B2.size() + A2.size() * B1.size();
    int sign = 1;

    if (k > negCount) {
      k -= negCount;  //  Find the (k - negCount)-th positive.
    } else {
      k = negCount - k + 1;  // Find the (negCount - k + 1)-th abs(negative).
      sign = -1;
      swap(B1, B2);
    }

    long l = 0;
    long r = 1e10;

    while (l < r) {
      const long m = (l + r) / 2;
      if (numProductNoGreaterThan(A1, B1, m) +
              numProductNoGreaterThan(A2, B2, m) >=
          k)
        r = m;
      else
        l = m + 1;
    }

    return sign * l;
  }

 private:
  void seperate(const vector<int>& arr, vector<int>& A1, vector<int>& A2) {
    for (const int a : arr)
      if (a < 0)
        A1.push_back(-a);
      else
        A2.push_back(a);
    ranges::reverse(A1);  // Reverse to sort ascending
  }

  long numProductNoGreaterThan(const vector<int>& A, const vector<int>& B,
                               long m) {
    long count = 0;
    int j = B.size() - 1;
    // For each a, find the first index j s.t. a * B[j] <= m
    // So numProductNoGreaterThan m for this row will be j + 1
    for (const long a : A) {
      while (j >= 0 && a * B[j] > m)
        --j;
      count += j + 1;
    }
    return count;
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums1 = [-4, -2, 0, 3], nums2 = [2, 4], k = 6
```
### Steps
```
Separate nums1: A1(negatives abs)=[2,4], A2(non-neg)=[0,3]
Separate nums2: B1(negatives abs)=[], B2(non-neg)=[2,4]
negCount = 4*2 + 2*0 = 8 (A1 x B2 produces negative products)
k=6 <= 8 -> searching negative: k = 8-6+1 = 3, sign = -1, swap B1<->B2
Now find 3rd smallest product of (A1=[2,4] x B1=[2,4]) and (A2=[0,3] x B2=[])
Binary search finds l=8 -> answer = -1 * 8 = -8
```

---

## ⏱️ Time Complexity
```
O((m + n) * log(10^10)), where m and n are array lengths
```

## 💾 Space Complexity
```
O(m + n) for the separated arrays
```

---

## ⚠️ Edge Cases
- Arrays with zeros: products with zero are 0
- All negative times all positive: all products negative
- `k = 1`: smallest product
- Single element arrays

---

## 🎯 Interview Takeaways
- Binary search on the answer is powerful for "k-th smallest" problems.
- Separating negatives and positives simplifies counting when products can be negative.
- Two-pointer technique efficiently counts products <= a threshold.

---

## 📌 Key Pattern
👉 **"Binary search on answer + two-pointer counting with sign separation"**

---

## 🔁 Related Problems
- 378. Kth Smallest Element in a Sorted Matrix
- 786. K-th Smallest Prime Fraction
- 668. Kth Smallest Number in Multiplication Table

---

## 🚀 Final Thoughts
This hard problem requires careful handling of negative numbers. The key insight is separating arrays by sign and reducing the problem to counting non-negative products via two pointers, then wrapping it in binary search.

---

✨ **Rule to remember:**
> For k-th smallest product with mixed signs, separate by sign, count negatives, and binary search on the absolute value.
