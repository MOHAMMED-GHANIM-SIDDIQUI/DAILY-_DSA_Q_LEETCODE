class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
      prev = 0 
      n = len(nums)
      num_sum = sum(nums)
      for idx , val in enumerate(nums):
        prev+=(idx*val)
      ans = prev 

      for i in range(n-1 , 0 , -1):
        prev = prev + num_sum - (n ) * nums[i]
        ans = max(ans , prev)
      return ans

        
