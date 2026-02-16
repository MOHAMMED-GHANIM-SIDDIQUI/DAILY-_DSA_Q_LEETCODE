class Solution:
    def reverseBits(self, n: int) -> int:

        ans = 0
        count = 0

        while count < 32:
            ans = ans | (n & 1)
            ans <<= 1
            n >>= 1
            count += 1

        ans >>= 1   # undo the extra final shift

        return ans

# 101
# 1 ----> missu [my median] my cutu ---> my love ---> i am sorry


