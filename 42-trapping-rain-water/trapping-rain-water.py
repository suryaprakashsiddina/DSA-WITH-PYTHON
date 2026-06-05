class Solution:
    def trap(self, arr: List[int]) -> int:
        n = len(arr)
        left = 0
        right = n - 1
        Leftmax = 0
        Rightmax = 0
        res = 0

        while left <= right:
            if arr[left] <= arr[right]:
                if arr[left] >= Leftmax:
                    Leftmax = arr[left]
                else:
                    res += Leftmax - arr[left]
                left += 1
            else:
                if arr[right] >= Rightmax:
                    Rightmax = arr[right]
                else:
                    res += Rightmax - arr[right]
                right -= 1
        return res


        