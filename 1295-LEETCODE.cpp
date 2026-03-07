class Solution {
    int numofdig(int n)
    {
       return log10(n)+1;
    }
public:
    int findNumbers(vector<int>& nums) {
        int ans=0;
        for(int i:nums)
        {
            if(numofdig(i)%2==0)
            ans++;
        }
        return ans;
    }
};
