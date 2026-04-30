# 2043. Simple Bank System

## 🔗 Problem Link
https://leetcode.com/problems/simple-bank-system/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Hash Table, Design, Simulation

---

## 🧩 Problem Summary
Design a bank system that supports deposit, withdraw, and transfer operations. Each operation must validate that the account number exists and that the account has sufficient funds for withdrawals. Return `true` if the operation succeeds, `false` otherwise.

### 📌 Constraints
- `n == balance.length`
- `1 <= n, account, account1, account2 <= 10^5`
- `0 <= balance[i], money <= 10^12`
- At most `10^4` calls to each function

---

## 💭 Intuition
👉 This is a straightforward design problem. Validate account indices and balance constraints, then perform the operation.

---

## ⚡ Approach — Direct Simulation

### 🧠 Idea
- Store the balance array.
- For each operation, validate the account number(s) are in range [1, n].
- For withdraw and transfer, check sufficient balance.
- Transfer is a withdraw from one account followed by a deposit to another.

---

## 💻 Code

```cpp
class Bank {
 public:
  Bank(vector<long long>& balance) : balance(std::move(balance)) {}

  bool transfer(int account1, int account2, long long money) {
    if (!isValid(account2))
      return false;
    return withdraw(account1, money) && deposit(account2, money);
  }

  bool deposit(int account, long long money) {
    if (!isValid(account))
      return false;
    balance[account - 1] += money;
    return true;
  }

  bool withdraw(int account, long long money) {
    if (!isValid(account))
      return false;
    if (balance[account - 1] < money)
      return false;
    balance[account - 1] -= money;
    return true;
  }

 private:
  vector<long long> balance;

  bool isValid(int account) {
    return 1 <= account && account <= balance.size();
  }
};
```

---

## 🧠 Dry Run
### Input
```
Bank bank([10, 100, 20, 50, 30])
bank.transfer(3, 1, 20)   -> withdraw(3, 20): 20>=20 yes, deposit(1, 20): valid -> [30,100,0,50,30], true
bank.deposit(2, 10)       -> valid, [30,110,0,50,30], true
bank.withdraw(3, 10)      -> balance[2]=0 < 10 -> false
```
### Steps
```
transfer(3,1,20): isValid(1)=true, withdraw(3,20): isValid(3)=true, 20>=20 -> balance[2]=0, deposit(1,20): balance[0]=30 -> true
deposit(2,10): isValid(2)=true, balance[1]=110 -> true
withdraw(3,10): isValid(3)=true, balance[2]=0 < 10 -> false
```

---

## ⏱️ Time Complexity
```
O(1) per operation
```

## 💾 Space Complexity
```
O(n) for storing the balance array
```

---

## ⚠️ Edge Cases
- Account number out of range (0 or > n)
- Transfer to invalid account (check destination first)
- Withdraw more than balance
- Transfer to the same account
- Money = 0

---

## 🎯 Interview Takeaways
- Design problems require clean separation of validation and logic.
- Using 1-indexed accounts requires careful index conversion.
- `std::move` for the constructor avoids unnecessary copies.

---

## 📌 Key Pattern
👉 **"Validate-then-execute with clean helper methods"**

---

## 🔁 Related Problems
- 1845. Seat Reservation Manager
- 146. LRU Cache
- 155. Min Stack

---

## 🚀 Final Thoughts
A clean design problem that tests the ability to structure code with proper validation. The transfer operation elegantly reuses withdraw and deposit methods.

---

✨ **Rule to remember:**
> In design problems, extract validation into helper methods and compose complex operations from simple ones.
