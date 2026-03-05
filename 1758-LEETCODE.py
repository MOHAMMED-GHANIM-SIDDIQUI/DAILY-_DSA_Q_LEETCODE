class Solution:
    def minOperations(self, s: str) -> int:
        diff1 = diff2 = 0

        for i, ch in enumerate(s):
            if ch != ('1' if i % 2 == 0 else '0'):
                diff1 += 1
            if ch != ('0' if i % 2 == 0 else '1'):
                diff2 += 1

        return min(diff1, diff2)
