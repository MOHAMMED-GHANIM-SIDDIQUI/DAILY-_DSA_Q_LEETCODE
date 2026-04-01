class Solution {
public:
    int findLucky(vector<int>& arr) {
        unordered_map<int,int>mpp;
        for(int i:arr)
        {
            mpp[i]++;
        }
        int ans=-1;
        for(auto it:mpp)
        {
            if(mpp[it.first]==it.first)
            {
                ans=max(ans,it.first);
            }
        }
        return ans;
        
    }
};
