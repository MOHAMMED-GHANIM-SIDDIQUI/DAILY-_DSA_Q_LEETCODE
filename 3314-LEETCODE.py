class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            Flag = False
            for j in range(1,num):
                if j | (j+1) == num:
                    ans.append(j)
                    Flag= True
                    break
            if Flag == False:
                ans.append(-1)
        return ans
            

        
