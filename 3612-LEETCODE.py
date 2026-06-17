class Solution:
    def processStr(self, s: str) -> str:
        ans = ""
        for ch in s:
            if ch == '*':
                ans = ans[:-1]
            elif ch =='#':
                ans*=2
            elif ch=='%':
                ans=ans[::-1]
            else:
                ans+=ch
        return ans
