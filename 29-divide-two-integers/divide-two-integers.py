class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) != (divisor < 0)

        a = abs(dividend)
        b = abs(divisor)
        result = 0

        while a >= b:
            temp = b
            multiple = 1

            while temp + temp <= a:
                temp += temp
                multiple += multiple

            a -= temp
            result += multiple

        return -result if negative else result