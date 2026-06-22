class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur_sum = 0
        ans = 0
        for cur in gain:
            cur_sum +=cur
            ans=max(ans , cur_sum)
        return ans
