class Solution:
    def binaryGap(self, n: int) -> int:
        ans = 0 
        prev = -1
        idx=0 
        while n:
            if n&1==1 :
                if prev!=-1:
                    ans=max(ans,idx-prev)
                prev=idx
            n>>=1
            idx+=1

        return ans
