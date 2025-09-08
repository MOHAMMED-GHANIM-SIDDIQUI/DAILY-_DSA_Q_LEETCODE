class Solution {
public:
    vector<int> getNoZeroIntegers(int n) {
        int fno = n / 2;
        int sno = n - fno;

        // Adjust until both are valid
        while (!isValid(fno) || !isValid(sno)) {
            fno--;
            sno++;
        }

        return {fno, sno};
    }

private:
    bool isValid(int num) {
        while (num > 0) {
            if (num % 10 == 0) return false;
            num /= 10;
        }
        return true;
    }
};
