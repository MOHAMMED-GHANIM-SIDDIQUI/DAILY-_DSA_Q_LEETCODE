class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            cnt_target = 0
            for j in range(i,n):
                if nums[j] == target:
                    cnt_target +=1
                if cnt_target > (j-i+1)//2:
                    ans+=1
        return ans

        
