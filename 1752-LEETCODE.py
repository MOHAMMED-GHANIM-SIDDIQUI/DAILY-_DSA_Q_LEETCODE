class Solution:
    def check(self, nums):
        n = len(nums)
        mistakes = 0

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                mistakes += 1

            if mistakes > 1:
                return False

        return True
