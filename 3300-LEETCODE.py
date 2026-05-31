class Solution:
    def minElement(self, nums: List[int]) -> int:
        
        min_res = float('inf')

        for n in nums:
            cur = 0
            while n:
                cur += n % 10
                n //= 10
            min_res = min(min_res, int(cur))
        return min_res
