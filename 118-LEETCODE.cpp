class Solution {
    vector<int> nrow(int n)
    {
        vector<int>row;
        row.push_back(1);
        int cur=1;
        for(int i=0;i<n;i++)
        {
            cur*=(n-i);
            cur/=(i+1);
            row.push_back(cur);
        }
        return row;
    }
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>>ans;
        for(int i=0;i<numRows;i++)
        {
            ans.push_back(nrow(i));
        }
        return ans;
    }
};
