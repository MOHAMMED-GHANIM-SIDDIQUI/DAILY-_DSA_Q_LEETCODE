class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
      m , n = len(grid) , len(grid[0])
      row_sum = list(map(lambda row: sum(row),grid))
      col_sum = list(map(lambda col: sum(col),zip(*grid)))
      total_sum = sum(row_sum)
      if total_sum % 2 != 0:
        return False
      else:
        target = total_sum // 2
        cum_sum = 0 
        for val in row_sum:
          cum_sum +=val
          if cum_sum == target:
            return True
        cum_sum = 0
        for val in col_sum:
          cum_sum +=val
          if cum_sum == target:
            return True
      return False
