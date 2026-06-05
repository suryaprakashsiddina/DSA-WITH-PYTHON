class Solution:
    def numIdenticalPairs(self, nums):
        from collections import Counter
        
        count = Counter(nums)
        result = 0
        
        for freq in count.values():
            result += freq * (freq - 1) // 2
        
        return result
        