class Solution {
public:
    int totalMoney(int n) {
        int cur_week=28;
        int how_many_week=n/7;
        int how_many_rem_day=n%7;
        int cur_day=how_many_week+1;
        int ans=0;
        for(int i=0;i<how_many_week;i++)
        {
            ans+=cur_week;
            cur_week+=7;
        }        
        for(int i=0;i<how_many_rem_day;i++)
        {
            ans+=cur_day;
            cur_day++;
        }
        return ans;
    }
};
