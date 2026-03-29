class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
      even_s1 = set([s1[0],s1[2]])
      even_s2 = set([s2[0],s2[2]])
      odd_s1  = set([s1[1],s1[3]])
      odd_s2  = set([s2[1],s2[3]])
      return even_s1 == even_s2 and odd_s1 == odd_s2
