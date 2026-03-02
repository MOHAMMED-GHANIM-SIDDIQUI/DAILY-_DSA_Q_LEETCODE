class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        trail_zeros = []
        for r in range(n):# 0 , 1 , 2
            zeroCnt= 0
            for e in range(n-1,-1,-1):
                if grid[r][e]==0:
                 zeroCnt+=1
                else:
                    break
            trail_zeros.append(zeroCnt)
        swap = 0
        for i in range(n):  # current row 
            req_zero = n-1-i
            j = i 
            while j<n and req_zero > trail_zeros[j]:
                j+=1
            if j == n:
                return -1
            else:
                for k in range(j,i,-1):
                    swap+=1
                    trail_zeros[k],trail_zeros[k-1]=trail_zeros[k-1],trail_zeros[k]
        return swap
        
