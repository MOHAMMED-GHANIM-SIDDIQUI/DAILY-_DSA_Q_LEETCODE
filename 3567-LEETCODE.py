class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = []
        
        for i in range(m - k + 1):
            temp = []
            for j in range(n - k + 1):
                sub_mat = set()
                
                # collect elements
                for r in range(i, i + k):
                    for c in range(j, j + k):
                        sub_mat.add(grid[r][c])
                
                arr = sorted(sub_mat)
                
                # compute min difference
                if len(arr) < 2:
                    min_diff = 0
                else:
                    min_diff = float('inf')
                    for t in range(len(arr) - 1):
                        min_diff = min(min_diff, arr[t+1] - arr[t])
                
                temp.append(min_diff)
            ans.append(temp)

        return ans
