class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)        
        s = ['a'] * (n + m - 1) # s is the ans
        fixed = [False] * (n + m - 1)
        
        # Handle 'T'
        for i in range(n): #str1
            if str1[i] == 'T':
                for j in range(m):
                    pos = i + j
                    if fixed[pos] and s[pos] != str2[j]: # collison
                        return ""
                    s[pos] = str2[j]
                    fixed[pos] = True
        
        # Handle 'F'
        for i in range(n):
            if str1[i] == 'F':
                diff = False                
                # Check if already different
                for j in range(m):
                    if s[i + j] != str2[j]:
                        diff = True
                        break
                
                if diff:
                    continue
                
                # Try to force difference
                changed = False
                for j in range(m - 1, -1, -1): # win where we need to change is s[i:i+m]
                    pos = i + j
                    if not fixed[pos]:
                        s[pos] = 'b'
                        changed = True
                        break
                
                if not changed:
                    return ""
        
        return "".join(s)
