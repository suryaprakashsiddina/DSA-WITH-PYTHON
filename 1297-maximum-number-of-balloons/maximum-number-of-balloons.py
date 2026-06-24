class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dict1 = {'b': 0, 'a': 0, 'l': 0, 'o':0, 'n': 0}

        for ch in text:
            if ch in dict1:
                dict1[ch] += 1

        res = min(
            dict1['b'], dict1['a'], dict1['l'] // 2, dict1['o'] // 2, dict1['n']
        )

        return res