#User function Template for python3

class Solution:
    def findStepKeyIndex(self, arr, k, x):
        # code here
        for i in range(len(arr)):
            if x == arr[i]:
                return i
        return -1
