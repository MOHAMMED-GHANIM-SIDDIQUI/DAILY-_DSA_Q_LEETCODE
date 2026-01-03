class Solution:
    def numOfWays(self, n: int) -> int:
        kMod = 1_000_000_007
        
        color2 = 6   # patterns like 121, 131, ...
        color3 = 6   # patterns like 123, 132, ...
        
        for _ in range(1, n):
            nextColor2 = color2 * 3 + color3 * 2
            nextColor3 = color2 * 2 + color3 * 2
            
            color2 = nextColor2 % kMod
            color3 = nextColor3 % kMod
        
        return (color2 + color3) % kMod
