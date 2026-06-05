class Solution:
    def findShortestSubArray(self, nums):
        count = {}
        first = {}
        last = {}

        for i in range(len(nums)):
            num = nums[i]

            if num not in first:
                first[num] = i

            last[num] = i
            count[num] = count.get(num, 0) + 1

        degree = max(count.values())
        ans = len(nums)

        for num in count:
            if count[num] == degree:
                ans = min(ans, last[num] - first[num] + 1)

        return ans
        
        