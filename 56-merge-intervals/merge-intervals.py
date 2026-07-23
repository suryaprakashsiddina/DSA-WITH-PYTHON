class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        i = 0
        ans = []

        while i < n:
            start = intervals[i][0]
            end = intervals[i][1]

            j = i + 1
            while j < n and intervals[j][0] <= end:
                end = max(end, intervals[j][1])
                j += 1
            
            ans.append([start, end])
            i = j
        
        return ans
        