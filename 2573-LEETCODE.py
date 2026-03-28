class Solution:
    def longest_common_prefix_matrix(self, s: str):
        n = len(s)
        result = [[0] * n for _ in range(n)]

        # Fill last row and column
        for j in range(n):
            result[n - 1][j] = 1 if s[j] == s[n - 1] else 0
            result[j][n - 1] = 1 if s[j] == s[n - 1] else 0

        # Fill rest
        for i in range(n - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if s[i] == s[j]:
                    result[i][j] = 1 + result[i + 1][j + 1]
                else:
                    result[i][j] = 0

        return result

    def findTheString(self, lcp):
        n = len(lcp)
        result = ['a'] * n

        for i in range(1, n):
            not_equal = [False] * 26
            matched = False

            for j in range(i):
                if lcp[j][i] == 0:
                    not_equal[ord(result[j]) - ord('a')] = True
                else:
                    result[i] = result[j]
                    matched = True
                    break

            if matched:
                continue

            for c in range(26):
                if not not_equal[c]:
                    result[i] = chr(ord('a') + c)
                    break

        result_str = ''.join(result)

        if self.longest_common_prefix_matrix(result_str) == lcp:
            return result_str
        return ""
