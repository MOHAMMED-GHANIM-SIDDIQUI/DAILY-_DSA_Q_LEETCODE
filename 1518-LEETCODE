class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int ans = numBottles;
        int empty = numBottles;
        
        while (empty >= numExchange) {
            int newBottles = empty / numExchange;
            ans += newBottles;
            empty = empty % numExchange + newBottles; // leftover + new empty bottles
        }
        
        return ans;
    }
};
