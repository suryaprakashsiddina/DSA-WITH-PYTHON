class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = "".join([ch for ch in s if self.is_alnum(ch)])
        new_str = self.to_lower(new_str)
        n = len(new_str)
        for i in range(n):
            if new_str[i] == new_str[n - i - 1]:
                continue
            else:
                return False
        return True
    
    def is_alnum(self, ch):
        return (
            ('a' <= ch <= 'z') or
            ('A' <= ch <= 'Z') or
            ('0' <= ch <= '9')
        )

    def to_lower(self, temp_str):
        result = ""
        for ch in temp_str:
            if 'A' <= ch <= 'Z':
                result += chr(ord(ch) + 32) 
            else:
                result += ch
        return result