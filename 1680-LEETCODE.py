class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans = 0
        MOD = 10**9 + 7
        
        for i in range(1, n + 1):
            # number of bits in i
            bits = i.bit_length()
            
            # shift ans left and add i
            ans = ((ans << bits) | i) % MOD
        
        return ans
