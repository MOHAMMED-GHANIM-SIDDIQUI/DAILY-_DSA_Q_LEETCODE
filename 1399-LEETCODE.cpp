class Solution {
    int sumofdigs(int num)
    {
        int sum=0;
        while(num)
        {
            sum+=num%10;
            num/=10;
        }
        return sum;
    }
public:
    int countLargestGroup(int n) {
        unordered_map<int,int>mpp;
        int maxi=INT_MIN;
        int ans=0;
        for(int i=1;i<=n;i++)
        {
            mpp[sumofdigs(i)]++;
            if(maxi<mpp[sumofdigs(i)])
            {
                maxi=mpp[sumofdigs(i)];
               
            }
        }
        for(auto it:mpp)
        {
            if(it.second==maxi)
            ans++;
        }
        return ans;
    }
};
