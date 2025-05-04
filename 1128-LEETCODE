class Solution {
public:
    int numEquivDominoPairs(vector<vector<int>>& dominoes) {
        unordered_map<string, int> freq;
        int ans = 0;
        
        for (auto& domino : dominoes) {
            // Sort the domino to avoid checking reversed pairs
            sort(domino.begin(), domino.end());
            string key = to_string(domino[0]) + "," + to_string(domino[1]);
            ans += freq[key]++;
        }
        
        return ans;
    }
};
