class Solution:
    def search(self, arr: List[int], target: int) -> int:
        low , high = 0, len(arr) - 1

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            # the left side is sorted
            if arr[low] <= arr[mid]:
                if target >= arr[low] and target <= arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # right half is sorted
            else:
                if target >= arr[mid] and target <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1