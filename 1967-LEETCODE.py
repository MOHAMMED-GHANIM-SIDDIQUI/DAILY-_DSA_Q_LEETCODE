class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum([1 if x in word else 0 for x in patterns])
        
