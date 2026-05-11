class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
      ans = []
      for num in nums:
        str_num = str(num)
        for c in str_num:
          ans.append(int(c))
      return ans
        
