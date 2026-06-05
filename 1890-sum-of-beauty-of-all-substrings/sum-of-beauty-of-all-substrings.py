class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        res = 0

        for i in range(n):
            freq = {}

            for j in range(i, n):
                freq[s[j]] = freq.get(s[j], 0) + 1

                if len(freq) > 1:
                    values = freq.values()
                    res += max(values) - min(values)

        return res