class Solution:
    def trapRainWater(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        R = len(grid)
        C = len(grid[0])
        vis = [[False] * C for _ in range(R)]

        pq = []
        vol = 0

        for i in range(R):
            for j in range(C):
                if i == 0 or i == R - 1 or j == 0 or j == C - 1:
                    heapq.heappush(pq, (grid[i][j], i ,j))
                    vis[i][j] = True
        
        minBdht = 0

        while pq:
            currHt, r, c = heapq.heappop(pq)
            minBdht = max(currHt, minBdht)

            dr = [0,0,-1,1]
            dc = [1,-1,0,0]

            for i in range(4):
                rr = r + dr[i]
                cc = c + dc[i]

                if 0 <= rr < R and 0 <= cc < C and not vis[rr][cc]:
                    heapq.heappush(pq, (grid[rr][cc], rr, cc))
                    vis[rr][cc] = True

                    if grid[rr][cc] < minBdht:
                        vol += minBdht - grid[rr][cc]
        return vol



        