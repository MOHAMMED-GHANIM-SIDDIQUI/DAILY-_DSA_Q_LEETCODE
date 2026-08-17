class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        cur_max=nums[0]
        gcd_arr=[]
        for i   in  nums:
            cur_max=max(cur_max,i)
            gcd_arr.append(gcd(cur_max,i))
        gcd_arr.sort()
        n=len(gcd_arr)
        res=0
        for i   in  range(n//2):
            res+=gcd(gcd_arr[i],gcd_arr[n-1-i])
        return  res
