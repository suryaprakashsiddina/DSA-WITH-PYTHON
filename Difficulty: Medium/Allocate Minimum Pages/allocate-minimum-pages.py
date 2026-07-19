class Solution:
    def findPages(self, arr, k):
        # code here
        
        def CountStudents(arr, mid, n):
            students = 1
            pagecount = 0
            
            for i in range(n):
                if pagecount + arr[i] <= mid:
                    pagecount += arr[i]
                else:
                    students += 1
                    pagecount = arr[i]
            
            return students
        
        n = len(arr)
        
        if k > n:
            return -1
        
        low = max(arr)
        high = sum(arr)
        
        
        while low <= high:
            mid = (low + high) // 2
            students = CountStudents(arr, mid, n)
            
            if students > k:
                low = mid + 1
            else:
                high = mid - 1
        
        return low
