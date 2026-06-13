class Solution:
    def getFinalState(self, arr: List[int], k: int, multiplier: int) -> List[int]:
        n = len(arr)
        for _ in range(k):
            mini = min(arr)
            idx = arr.index(mini)

            arr[idx] = multiplier * mini

        return arr
            
        