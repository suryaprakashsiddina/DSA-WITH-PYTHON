class Solution:
    def isPalindrome(self, n: int) -> bool:
        temp = n
        res = 0
        while n > 0:
            last = n % 10
            res = res * 10 + last
            n = n // 10
        
        # if temp == res:
        #     return True
        # else:
        #     return False
        return temp == res
        