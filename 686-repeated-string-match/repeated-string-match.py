class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        s = a
        cnt = 1

        while len(s) < len(b):
            s += a
            cnt += 1

        if b in s:
            return cnt
        if b in s + a:
            return cnt + 1

        return -1 
        