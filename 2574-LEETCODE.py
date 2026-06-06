class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        result = []
        left_sum = 0
        right_sum = sum(nums)

        for num in nums:
            right_sum -= num
            result.append(abs(left_sum - right_sum))
            left_sum += num

        return result
