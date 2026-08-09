import heapq

class Solution:
    def minCost(self, arr):
        # code here
        heapq.heapify(arr)
        
        min_cost = 0
        
        while len(arr) > 1:
            cost1 = heapq.heappop(arr)
            cost2 = heapq.heappop(arr)
            
            cost = cost1 + cost2
            
            min_cost += cost
            
            heapq.heappush(arr, cost)
        
        return min_cost
        