class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        tracker = defaultdict(list)
        min_good_dist = float('inf')
        for idx , val in enumerate(nums):
          tracker[val].append(idx)
        for key , idx_list in tracker.items():
          if len(idx_list) >= 3:
            n = len(idx_list)
            for i in range(n-2):
              cur_good_dist = (idx_list[i+1] - idx_list[i]) + (idx_list[i+2] - idx_list[i+1]) + (idx_list[i+2] - idx_list[i])
              if cur_good_dist < min_good_dist:
                min_good_dist = cur_good_dist
        return -1 if min_good_dist == float('inf') else min_good_dist
          
