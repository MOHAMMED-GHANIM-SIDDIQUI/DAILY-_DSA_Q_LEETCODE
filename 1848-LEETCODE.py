class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n = len(nums)
        
        for d in range(n):
            if start - d >= 0 and nums[start - d] == target:
                return d
            if start + d < n and nums[start + d] == target:
                return d
