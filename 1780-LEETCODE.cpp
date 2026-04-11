class Solution {
public:
    bool checkPowersOfThree(int n) {
        while (n > 0) {
            if (n % 3 == 2) {
                return false;  // If the remainder is 2, it's not a valid sum of powers of 3
            }
            n /= 3;  // Divide n by 3 to move to the next power of 3
        }
        return true;
    }
};
