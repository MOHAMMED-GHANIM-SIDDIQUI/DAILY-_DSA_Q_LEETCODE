# 2523. Closest Prime Numbers in Range

## 🔗 Problem Link
https://leetcode.com/problems/closest-prime-numbers-in-range/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Math, Number Theory

---

## 🧩 Problem Summary
Given two positive integers `left` and `right`, find the two prime numbers in the range `[left, right]` that are closest to each other (smallest difference). If there are ties, return the pair with the smallest first number. If fewer than 2 primes exist, return `[-1, -1]`.

### 📌 Constraints
- `1 <= left <= right <= 10^6`

---

## 💭 Intuition
👉 Generate all primes in the range, then scan consecutive pairs to find the minimum difference. Consecutive primes always have the smallest gaps.

---

## ⚡ Approach — Brute-Force Primality Check + Consecutive Pair Scan

### 🧠 Idea
- Iterate through `[left, right]`, check each number for primality using trial division.
- Collect all primes in a list.
- Scan consecutive primes to find the pair with the smallest difference.

---

## 💻 Code

```cpp
class Solution {
    bool isprime(int num)
    {
        if(num==1)
        return 0;
        for(int i=2;i*i<=num;i++)
        {
            if(num%i==0)
            return false;
        }
        return 1;
    }
public:
    vector<int> closestPrimes(int left, int right) {
        vector<int>prime;
        for(int i=left;i<=right;i++)
        {
            if(isprime(i))
            prime.push_back(i);
        }
        int smallest_diff=INT_MAX;
        int n=prime.size();
        vector<int>ans;
        if(n==0 || n==1)
        return {-1,-1};
        for(int i=0;i<n-1;i++)
        {
            if(smallest_diff>(prime[i+1]-prime[i]))
            {
                smallest_diff=prime[i+1]-prime[i];
                ans={prime[i],prime[i+1]};
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
left = 10, right = 19
```
### Steps
```
Check 10-19 for primality:
  10: not prime, 11: prime, 12: no, 13: prime, 14: no, 15: no, 16: no, 17: prime, 18: no, 19: prime
primes = [11, 13, 17, 19]

Consecutive diffs: 13-11=2, 17-13=4, 19-17=2
Smallest diff = 2, first pair = [11, 13]

Result: [11, 13]
```

---

## ⏱️ Time Complexity
```
O((right - left) * sqrt(right)) — primality check for each number in range.
```

## 💾 Space Complexity
```
O(number of primes in range) — storing primes list.
```

---

## ⚠️ Edge Cases
- Range contains 0 or 1 primes: return [-1, -1].
- `left = right`: at most one prime, return [-1, -1].
- Twin primes (difference = 2) in range.
- `left = 1`: 1 is not prime.

---

## 🎯 Interview Takeaways
- Trial division is O(sqrt(n)) per number — sufficient for n up to 10^6.
- Closest primes are always consecutive in the sorted list.
- A Sieve of Eratosthenes would be more efficient for larger ranges.

---

## 📌 Key Pattern
👉 **"Generate primes in range, then scan consecutive pairs for minimum gap."**

---

## 🔁 Related Problems
- 204. Count Primes
- 2614. Prime In Diagonal
- 866. Prime Palindrome

---

## 🚀 Final Thoughts
While this brute-force approach works within the constraints, using a Sieve of Eratosthenes up to `right` would reduce the time complexity to O(right * log(log(right))). For interview purposes, mentioning the sieve optimization is a good follow-up.

---

✨ **Rule to remember:**
> "Closest primes are always consecutive — generate primes first, then scan pairs."
