class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        my_list = []
        for i in nums:
            if i in my_list:

                return i
            my_list.append(i)
        
        
