class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        total = 0

        for i in range(len(timeSeries) - 1):
            # add minimum of duration or gap between attacks
            total += min(duration, timeSeries[i + 1] - timeSeries[i])

        # add last attack duration
        total += duration

        return total
        