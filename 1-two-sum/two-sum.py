class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        arr_original = arr[:]
        arr.sort()
        left = 0
        right = len(arr) - 1

        while left < right:
            sum = arr[left] + arr[right]
            if sum == target:
                num1 = arr[left]
                num2 = arr[right]
                index1 = arr_original.index(num1)
                index2 = arr_original.index(num2) if num1 != num2 else arr_original.index(num2, index1 + 1)
                return [index1,index2]
            elif sum < target:
                left += 1
            else:
                right -= 1
        return []