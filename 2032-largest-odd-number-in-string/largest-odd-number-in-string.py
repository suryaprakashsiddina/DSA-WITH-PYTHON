class Solution:
    def largestOddNumber(self, s: str) -> str:
        idx = 0
        n = len(s)
        for i in range(n):
            if s[i] != '0':
                break
            idx += 1

        for i in range(n - 1, idx - 1, -1):
            if int(s[i]) % 2 == 1:
                return str(s[idx: i + 1])
        return ""
        