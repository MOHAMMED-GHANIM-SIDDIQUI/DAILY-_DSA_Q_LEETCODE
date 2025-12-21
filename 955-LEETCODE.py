class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        ans = 0
        # sorted[i] := True if strs[i] < strs[i + 1]
        sorted_ = [False] * (n - 1)

        for j in range(len(strs[0])):  # Loop through each character in the column
            i = 0
            while i + 1 < n:
                if not sorted_[i] and strs[i][j] > strs[i + 1][j]:
                    ans += 1
                    break
                i += 1
            
            # Update the sorted array after comparing all pairs for this column
            if i + 1 == n:
                for i in range(n - 1):
                    sorted_[i] = sorted_[i] or strs[i][j] < strs[i + 1][j]

        return ans
