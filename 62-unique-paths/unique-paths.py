class Solution:
    def CountPaths(self,i: int,j: int,m: int,n: int,dp: List[List[int]]) -> int:
        if i == (m-1) and j == (n-1):
            return 1
        if i >= m or j >= n: #when exceeds
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        else:
            dp[i][j] = self.CountPaths(i+1,j,m,n,dp) + self.CountPaths(i,j+1,m,n,dp)
            return dp[i][j]

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]

        num = self.CountPaths(0,0,m,n,dp)
        if m == 1 and n == 1:
            return num
        return num





        