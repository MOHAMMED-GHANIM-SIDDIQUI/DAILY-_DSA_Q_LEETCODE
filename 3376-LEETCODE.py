class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
      tracker = {} 
      min_dist = float('inf')
      for idx , val in enumerate(nums):
        if val in tracker:
          cur_dist = abs(tracker[val] - idx )
          min_dist = min(min_dist , cur_dist)
        rev = int(str(val)[::-1])
        tracker[rev] = idx
      return min_dist if min_dist != float('inf') else -1

        
