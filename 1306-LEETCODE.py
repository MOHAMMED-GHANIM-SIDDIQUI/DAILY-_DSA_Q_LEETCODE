class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)

        def solve(idx):
            if idx < 0 or idx >= n or arr[idx] < 0:
                return False

            if arr[idx] == 0:
                return True

            jump = arr[idx]
            arr[idx] = -arr[idx]   # mark visited

            return solve(idx + jump) or solve(idx - jump)

        return solve(start)
