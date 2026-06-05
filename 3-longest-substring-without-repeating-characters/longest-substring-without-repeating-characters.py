class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        st = set()
        l = 0
        maxans = float('-inf')

        for r in range(n):
            if s[r] in st:
                while l < r and s[r] in st:
                    st.remove(s[l])
                    l += 1
            st.add(s[r])
            maxans = max(maxans, r - l + 1)
        return maxans
        