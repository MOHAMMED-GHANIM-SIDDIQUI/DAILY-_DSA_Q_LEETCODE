class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)

        for i in range(n):
            target = (i + nums[i]) % n
            res.append(nums[target])

        return res
