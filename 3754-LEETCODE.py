class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0

        digit_sum = 0
        digits = []

        while n:
            digit = n % 10
            digit_sum += digit
            if digit:
                digits.append(digit)
            n //= 10

        x = 0
        while digits:
            x = x * 10 + digits.pop()

        return x * digit_sum
