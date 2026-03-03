class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # s1 = 0
        # s2 = s1 + 1 + ~ s1[::-1]
        # S3 = S2 + 1 + ~s2[::-1]
        # s4 ----> 15-----> 7 (s3) + 1 [8th idx] + 7 (~s3[::-1]) 
        # k- half
        if n == 1 :
            return '0'
        total_len = (1<<n) - 1
        half_len = ( total_len // 2 ) + 1
        if k == half_len:
            return '1'
        elif k < half_len:
            return self.findKthBit(n-1,k)
        else:
            k = half_len - ( k - half_len )
            d=self.findKthBit(n-1,k)
            return  '0' if d == '1' else '1'
       
