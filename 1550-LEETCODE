class Solution {
public:
    bool threeConsecutiveOdds(vector<int>& arr) {
        
        int cnt=3;
        for(int i:arr)
        {
            if(i%2)
            {
                cnt--;
            }
            else
            {
                cnt=3;
            }
            if(cnt==0)
            return true;
        }
        return false;
    }
};
