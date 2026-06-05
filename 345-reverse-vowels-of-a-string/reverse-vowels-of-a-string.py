class Solution:
    def reverseVowels(self, s: str) -> str:
        temp = ['a','e','i','o','u','A','E','I','O','U']
        dict1 = {}

        for i in range(len(s)):
            if s[i] in temp:
                dict1[i] = s[i]
        
        vowels_reversed = list(dict1.values())[::-1]

        s_list = list(s)
        idx = 0
        for key in dict1:
          s_list[key] = vowels_reversed[idx]
          idx += 1

        return ''.join(s_list)