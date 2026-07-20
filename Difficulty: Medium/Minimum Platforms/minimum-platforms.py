class Solution:    
    def minPlatform(self, arr, dep):
        # code here
        n = len(arr)
        
        arr.sort()
        dep.sort()
        
        cnt = 1
        res = 1
        
        i = 1
        j = 0
        
        while i < n and j < n:
            if arr[i] <= dep[j]:
                cnt += 1
                i += 1
            else:
                cnt -= 1
                j += 1
            
            res = max(res, cnt)
        
        return res
        