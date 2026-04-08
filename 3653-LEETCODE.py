class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
      for l , r , k , v in queries:
        for i in range(l,r+1,k):
          nums[i]=(nums[i] * v) % (10**9 + 7)
      ans = 0
      for val in nums:
        ans ^= val
      return ans 
