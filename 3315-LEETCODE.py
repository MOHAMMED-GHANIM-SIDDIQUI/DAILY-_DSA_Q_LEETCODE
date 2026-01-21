class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for num in nums:
            found = False
            if num==2:
                ans.append(-1)
                continue

            for i in range(32):
                if (num & (1 << i)) == 0:
                    if i > 0:
                        num = num & ~(1 << (i - 1))
                    ans.append(num)
                    found = True
                    break

            if not found:
                ans.append(-1)

        return ans
