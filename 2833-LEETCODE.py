class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
      ans = 0
      cnt_of_underscore = 0
      for move in moves:
        if move == 'L':
          ans-=1
        elif move == 'R':
          ans+=1
        else :
          cnt_of_underscore+=1
      return cnt_of_underscore + abs(ans) 
      

        
