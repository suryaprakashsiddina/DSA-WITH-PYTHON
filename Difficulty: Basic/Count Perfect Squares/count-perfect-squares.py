#User function Template for python3

class Solution:
    def countSquares(self, n):
        # code here 
        cnt = 0
        for i in range(1,n):
            temp = i ** 2
            if temp < n:
                cnt += 1
            else:
                return cnt