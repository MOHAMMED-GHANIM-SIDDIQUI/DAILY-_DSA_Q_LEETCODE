import math
from typing import List

class Solution:
    def check(self, mid: int, workerTimes: List[int], mH: int) -> bool:
        h = 0

        for t in workerTimes:
            h += int(math.sqrt(2.0 * mid / t + 0.25) - 0.5)

            if h >= mH:
                return True

        return h >= mH

    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        maxTime = max(workerTimes)

        l = 1
        r = maxTime * mountainHeight * (mountainHeight + 1) // 2

        result = 0

        while l <= r:
            mid = l + (r - l) // 2

            if self.check(mid, workerTimes, mountainHeight):
                result = mid
                r = mid - 1
            else:
                l = mid + 1

        return result
