class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        gap = min(self.maxContinousGap(hBars), self.maxContinousGap(vBars))
        return gap * gap

    def maxContinousGap(self, bars: List[int]) -> int:
        if not bars:
            return 1  # no bars removed → no hole bigger than 1

        bars.sort()
        res = 2
        runningGap = 2

        for i in range(1, len(bars)):
            if bars[i] == bars[i - 1] + 1:
                runningGap += 1
            else:
                runningGap = 2
            res = max(res, runningGap)

        return res
