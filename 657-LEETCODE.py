class Solution:
    def judgeCircle(self, moves: str) -> bool:
        vertical_bal = 0
        horizontal_bal = 0
        for move in moves:
          if move =='L':
            horizontal_bal-=1
          elif move =='R':
            horizontal_bal+=1
          elif move =='U':
            vertical_bal+=1
          else:
            vertical_bal-=1
        return vertical_bal ==  horizontal_bal == 0

