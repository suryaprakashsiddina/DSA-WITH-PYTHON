class Solution:
    def subarraySum(self, arr, target):
        # code here
        n = len(arr)
        left = 0
        cur_sum = 0
        
        for right in range(n):
            cur_sum += arr[right]
            
            while cur_sum > target:
                cur_sum -= arr[left]
                left += 1
            
            if cur_sum == target:
                return [left + 1, right + 1]
        
        return [-1]