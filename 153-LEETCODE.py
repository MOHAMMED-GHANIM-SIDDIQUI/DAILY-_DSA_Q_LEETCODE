class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2

            # Minimum is in right half
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                # Minimum is at mid or in left half
                high = mid

        return nums[low]
