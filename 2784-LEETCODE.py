class Solution:
    def isGood(self, nums: List[int]) -> bool:
        set_num = set(nums)
        real_set = set([i for i in range(1,len(nums))])
        if set_num == real_set and nums.count(len(nums)-1) == 2:
            return True
        return False
        
