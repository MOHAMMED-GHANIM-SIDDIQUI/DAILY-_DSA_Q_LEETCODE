class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Flatten grid 
        all_nums = [num for row in grid for num in row]
        
        # Check if all elements have same remainder mod x
        rem = all_nums[0] % x
        for num in all_nums:
            if num % x != rem:
                return -1
        
        # Find median
        all_nums.sort()
        median = all_nums[len(all_nums) // 2]
        
        # Calculate operations
        ans = 0
        for num in all_nums:
            ans += abs(num - median) // x
        
        return ans
