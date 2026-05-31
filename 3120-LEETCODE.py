class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans = 0
        for c in set(word):
            if c.upper() in word and c.lower() in word:
                ans+=1
        return ans//2

        
