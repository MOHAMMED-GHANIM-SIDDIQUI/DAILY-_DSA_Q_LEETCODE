class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()

        # Store every prefix from arr1
        for x in arr1:
            while x:
                prefixes.add(x)
                x //= 10

        ans = 0

        # Check prefixes of arr2 numbers
        for x in arr2:
            while x:
                if x in prefixes:
                    ans = max(ans, len(str(x)))
                    break
                x //= 10

        return ans
