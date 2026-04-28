# 2081. Sum of k-Mirror Numbers

## 🔗 Problem Link
https://leetcode.com/problems/sum-of-k-mirror-numbers/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Math, Enumeration, String

---

## 🧩 Problem Summary
A k-mirror number is a positive integer that reads the same in base-10 AND in base-k. Given `k` and `n`, return the sum of the `n` smallest k-mirror numbers.

### 📌 Constraints
- `2 <= k <= 9`
- `1 <= n <= 30`

---

## 💭 Intuition
👉 Generate palindromes in base-k in ascending order (by incrementing the "first half" of the palindrome), convert to base-10, and check if the base-10 representation is also a palindrome.

---

## ⚡ Approach — Generate Base-k Palindromes

### 🧠 Idea
- Maintain a list `A` representing a palindrome in base-k.
- Implement `nextKMirror` to generate the next base-k palindrome by incrementing from the middle outward.
- For each base-k palindrome, convert to base-10 and check if it is also a palindrome.
- Accumulate the sum of the first `n` such numbers.

---

## 💻 Code

```python
class Solution:
  def kMirror(self, k: int, n: int) -> int:
    ans = 0
    A = ['0']

    def nextKMirror(A: list[str]) -> list[str]:
      for i in range(len(A) // 2, len(A)):
        nextNum = int(A[i]) + 1
        if nextNum < k:
          A[i] = str(nextNum)
          A[~i] = str(nextNum)
          for j in range(len(A) // 2, i):
            A[j] = '0'
            A[~j] = '0'
          return A
      return ['1'] + ['0'] * (len(A) - 1) + ['1']

    for _ in range(n):
      while True:
        A = nextKMirror(A)
        num = int(''.join(A), k)
        if str(num)[::-1] == str(num):
          break
      ans += num

    return ans
```

---

## 🧠 Dry Run
### Input
```
k = 2, n = 5
```
### Steps
```
Find k-mirror numbers (palindrome in both base-2 and base-10):
A=['0'] -> next: A=['1'] -> num=1, "1"=="1" palindrome -> ans+=1
A=['1'] -> next: A=['1','1'] -> num=3, "3"=="3" -> ans+=3
A=['1','1'] -> next: A=['1','0','1'] -> num=5, "5"=="5" -> ans+=5
A=['1','0','1'] -> next: A=['1','1','1'] -> num=7, "7"=="7" -> ans+=7
A=['1','1','1'] -> next: A=['1','0','0','1'] -> num=9, "9"=="9" -> ans+=9
Return 1+3+5+7+9 = 25
```

---

## ⏱️ Time Complexity
```
O(n * M), where M is the number of base-k palindromes checked before finding n valid ones
```

## 💾 Space Complexity
```
O(D), where D is the number of digits in the largest palindrome
```

---

## ⚠️ Edge Cases
- k = 2: binary palindromes that are also decimal palindromes
- n = 1: always returns 1
- Large k-mirror numbers may require many iterations to find

---

## 🎯 Interview Takeaways
- Generating palindromes by mirroring the first half is efficient.
- The `~i` trick in Python mirrors index `i` from the end.
- Converting between bases and checking palindrome properties are core building blocks.

---

## 📌 Key Pattern
👉 **"Generate palindromes in one base, verify palindrome in another base"**

---

## 🔁 Related Problems
- 906. Super Palindromes
- 564. Find the Closest Palindrome
- 479. Largest Palindrome Product

---

## 🚀 Final Thoughts
This problem requires generating palindromes in a given base efficiently. The `nextKMirror` function is elegant -- it increments from the center outward, maintaining the palindrome property throughout. The dual palindrome check makes this a unique challenge.

---

✨ **Rule to remember:**
> To enumerate palindromes, only increment the first half and mirror it; to check dual-base palindromes, generate in one base and verify in the other.
