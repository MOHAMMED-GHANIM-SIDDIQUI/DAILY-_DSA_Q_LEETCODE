class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        # nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]
        #           i                          j
        ans = 0
        if nums1[-1]>nums2[0]:
            return 0
        i , j =0 , 0
        while i < n and j < m:
          if nums1[i] <= nums2[j]:
            ans = max(ans, j-i)
            j+=1
          else:
            i+=1
        return ans

