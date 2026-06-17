class Solution:
    def processStr(self, s: str, k: int) -> str:
        # Compute final length
        length = 0

        for ch in s:
            if 'a' <= ch <= 'z':
                length += 1
            elif ch == '*':
                if length:
                    length -= 1
            elif ch == '#':
                length *= 2
            else:  # %
                pass

        if k >= length:
            return '.'

        # Reverse simulation
        for ch in reversed(s):
            if 'a' <= ch <= 'z':
                if k == length - 1:
                    return ch
                length -= 1

            elif ch == '*':
                length += 1

            elif ch == '#':
                half = length // 2
                if k >= half:
                    k -= half
                length = half

            else:  # %
                k = length - 1 - k

        return '.'
