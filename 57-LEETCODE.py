class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idx = 0
        n = len(intervals)
        ans = []
        while idx<n and intervals[idx][1]<newInterval[0]:
            ans.append(intervals[idx])
            idx+=1
        while idx<n and newInterval[1]>=intervals[idx][0]:
            newInterval[0] = min(intervals[idx][0],newInterval[0])
            newInterval[1] = max(intervals[idx][1],newInterval[1])
            idx+=1
        ans.append(newInterval)
        while idx<n:
            ans.append(intervals[idx])
            idx+=1
        return ans
