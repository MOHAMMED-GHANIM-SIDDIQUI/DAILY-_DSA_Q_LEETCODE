class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
      n = len(s)
      s = s + s      
      if goal in s and len(goal) == n:
        return True
      return False
      
        
