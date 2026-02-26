class Solution:
    def numSteps(self, s: str) -> int:
        ops = 0
        carry = 0
        # Traverse from right to left (ignore first bit)
        for i in range(len(s) - 1, 0, -1):

            if int(s[i]) + carry == 1:
                # odd → add 1 + divide
                ops += 2
                carry = 1
            else:
                # even → divide only
                ops += 1

        # if carry remains at MSB, one extra operation
        return ops + carry
