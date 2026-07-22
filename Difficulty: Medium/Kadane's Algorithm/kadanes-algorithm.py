class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        n = len(arr)
        maxi = float('-inf')
        sum = 0
        
        for i in range(n):
            sum += arr[i]
            
            if sum > maxi:
                maxi = sum
            
            if sum < 0:
                sum = 0
        
        return maxi