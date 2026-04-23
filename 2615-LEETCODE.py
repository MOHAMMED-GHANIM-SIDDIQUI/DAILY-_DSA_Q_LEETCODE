class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        freq = defaultdict(list)
        
        # Step 1: Store indices
        for idx, val in enumerate(nums):
            freq[val].append(idx)
        
        ans = [0] * len(nums)
        
        # Step 2: Process each group
        for val, indices in freq.items():
            total_sum = sum(indices)
            prefix_sum = 0
            n = len(indices)
            
            for i, idx in enumerate(indices):
                # Left side
                left = idx * i - prefix_sum
                
                # Right side
                right = (total_sum - prefix_sum - idx) - (n - i - 1) * idx
                
                ans[idx] = left + right
                
                # Update prefix sum
                prefix_sum += idx
        
        return ans
