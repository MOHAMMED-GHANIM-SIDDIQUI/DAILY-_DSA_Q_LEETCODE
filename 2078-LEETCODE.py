class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        maxi = 0
        
        for i in range(n):
            if colors[i] != colors[0]:
                maxi = max(maxi, i)
            if colors[i] != colors[n - 1]:
                maxi = max(maxi, n - 1 - i)
        
        return maxi
