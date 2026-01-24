class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l=0
        r=len(nums) - 1
        max_sum=-float('inf')
        while l<r:
            cur_sum = nums[l]+nums[r]
            if cur_sum>max_sum:
                max_sum = cur_sum
            l+=1
            r-=1
        return max_sum

        
