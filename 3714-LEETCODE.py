class Solution:
    def helper(self, s: str, ch1: str, ch2: str) -> int:
        diffMap = {}
        maxL = 0
        count1 = count2 = 0

        for i, ch in enumerate(s):
            if ch != ch1 and ch != ch2:
                diffMap.clear()
                count1 = count2 = 0
                continue

            if ch == ch1:
                count1 += 1
            if ch == ch2:
                count2 += 1

            if count1 == count2:
                maxL = max(maxL, count1 + count2)

            diff = count1 - count2
            if diff in diffMap:
                maxL = max(maxL, i - diffMap[diff])
            else:
                diffMap[diff] = i

        return maxL

    def longestBalanced(self, s: str) -> int:
        n = len(s)
        maxL = 0

        # ---------- Case 1: Single character ----------
        count = 1
        for i in range(1, n):
            if s[i] == s[i - 1]:
                count += 1
            else:
                maxL = max(maxL, count)
                count = 1
        maxL = max(maxL, count)

        # ---------- Case 2: Two characters ----------
        maxL = max(maxL, self.helper(s, 'a', 'b'))
        maxL = max(maxL, self.helper(s, 'a', 'c'))
        maxL = max(maxL, self.helper(s, 'b', 'c'))

        # ---------- Case 3: Three characters ----------
        countA = countB = countC = 0
        diffMap = {}

        for i, ch in enumerate(s):
            if ch == 'a':
                countA += 1
            elif ch == 'b':
                countB += 1
            else:
                countC += 1

            if countA == countB == countC:
                maxL = max(maxL, countA + countB + countC)

            diffAB = countA - countB
            diffAC = countA - countC
            key = (diffAB, diffAC)  # tuple faster than string

            if key in diffMap:
                maxL = max(maxL, i - diffMap[key])
            else:
                diffMap[key] = i

        return maxL
