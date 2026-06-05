class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        cnt = 0
        result = ''

        for i in range(len(s)):
            if s[i] == '(':
                cnt += 1
                if cnt > 1:
                    result += s[i]
            else:
                cnt -= 1
                if cnt > 0:
                    result += s[i]
        return result