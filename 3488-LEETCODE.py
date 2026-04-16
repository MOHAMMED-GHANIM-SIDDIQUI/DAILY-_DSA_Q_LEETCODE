class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        tracker = defaultdict(list)
        n = len(nums)
        
        # Step 1: group indices
        for i, val in enumerate(nums):
            tracker[val].append(i)
        
        # Step 2: precompute answers
        res = [-1] * n
        
        for val in tracker:
            positions = tracker[val]
            k = len(positions)
            
            if k == 1:
                continue  # stays -1
            
            for i in range(k):
                curr = positions[i]
                prev = positions[(i - 1) % k]
                next_ = positions[(i + 1) % k]
                
                d1 = abs(curr - prev)
                d2 = abs(curr - next_)
                
                d1 = min(d1, n - d1)
                d2 = min(d2, n - d2)
                
                res[curr] = min(d1, d2)
        
        # Step 3: answer queries in O(1)
        return [res[q] for q in queries]
