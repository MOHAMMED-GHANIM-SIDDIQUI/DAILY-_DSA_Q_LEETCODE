class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        L = 1
        i = 0

        for j in range(n):
            maxEl = nums[j]

            while i < j and maxEl > k * nums[i]:
                i += 1

            L = max(L, j - i + 1)

        return n - L
