class Solution:
    def longestCommonPrefix(self, arr: List[str]) -> str:
        n = len(arr)
        res = ""
        if n == 0:
            return res
        if n == 1:
            return arr[0]
        
        # Use the length of the shortest string
        min_len = min(len(word) for word in arr)
        
        for i in range(min_len):
            temp = arr[0][i]
            cnt = 1
            for j in range(1, n):
                if arr[j][i] == temp:
                    cnt += 1
                else:
                    return res
            if cnt == n:
                res += temp
        return res
        