class Solution:
    def numSpecial(self, grid: List[List[int]]) -> int:
        
        row_sum_LC = [sum(row) for row in grid]

        col_sum_LC = [sum(col) for col in (zip(*grid))]
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and row_sum_LC[i] == 1 and col_sum_LC[j] == 1:
                    ans +=1
        return ans
