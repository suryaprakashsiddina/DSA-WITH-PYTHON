class Solution:
    def findMaxConsecutiveOnes(self, arr: List[int]) -> int:
        cnt = 0
        maxi = 0
        for i in range(len(arr)):
            if arr[i] == 1:
                cnt += 1
            else:
                cnt = 0
            maxi = max(maxi,cnt)
        return maxi
        