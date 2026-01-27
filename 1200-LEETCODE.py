class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff= float('inf')
        for i in range(len(arr)-1):
            cur_diff = arr[i+1] - arr[i]
            if cur_diff < min_diff:
                min_diff = cur_diff
        ans = []
        for i in range(len(arr)-1):
            cur_diff = arr[i+1] - arr[i]
            if cur_diff == min_diff:
                ans.append([arr[i] , arr[i+1]]) 
        return ans       
