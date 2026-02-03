class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 4:
            return False

        count = 0
        prev_diff = nums[1] - nums[0]

        if prev_diff <= 0:
            return False  # must start increasing

        for i in range(1, n - 1):
            cur_diff = nums[i + 1] - nums[i]
            if cur_diff == 0:
                return False

            if prev_diff * cur_diff < 0:
                count += 1

            prev_diff = cur_diff

        return count == 2
