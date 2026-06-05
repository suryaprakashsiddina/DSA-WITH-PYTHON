class Solution:
    def triangularSum(self, arr: List[int]) -> int:
        n = len(arr)-1
        res = arr[0]
        c = 1
        for k in range(1, n+1):
            c = c * (n - k + 1) // k
            res = (res + arr[k] * c) % 10
        return res 

