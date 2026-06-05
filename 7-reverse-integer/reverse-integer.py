class Solution:
    def reverse(self, n: int) -> int:
        if n < 0:
            sign = -1
        else:
            sign = 1
        n = abs(n)

        res = 0
        while n > 0:
            last = n % 10
            res = res * 10 + last
            n = n // 10
        
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 -1
        if res < INT_MIN:
            return 0
        if res > INT_MAX:
            return 0

        return res * sign
        