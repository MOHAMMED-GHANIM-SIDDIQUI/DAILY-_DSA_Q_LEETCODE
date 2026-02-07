class Solution:
    def minimumDeletions(self, s: str) -> int:
        stack = []
        ans = 0

        for c in s:
            if stack and stack[-1] == 'b' and c == 'a':
                ans += 1
                stack.pop()   # delete the 'b'
                # skip pushing 'a'
            else:
                stack.append(c)

        return ans
