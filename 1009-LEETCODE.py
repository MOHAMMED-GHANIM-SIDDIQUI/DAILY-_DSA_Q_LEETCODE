class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1        
        ans = 0
        power = 0        
        while n:
            if (n & 1) == 0:
                ans += (1 << power)
            power += 1
            n >>= 1
        
        return ans
