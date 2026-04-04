class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
      n = len(encodedText) 
      cols = n // rows
      ans = ''
      for i in range(cols):
        j=i
        while j<n:
          ans+=encodedText[j]
          j+=(cols+1)
      return ans.rstrip()


        
