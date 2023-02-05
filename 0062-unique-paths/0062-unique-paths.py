class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        def helper(idx,jdx):
            if (m-1) == idx and (n-1) == jdx:
                return 1
            if idx + 1 > m or jdx + 1 > n:
                return 0
            if dp[idx][jdx] != -1:
                return dp[idx][jdx]
            dp[idx][jdx] = helper(idx+1,jdx) + helper(idx,jdx+1) 
            return dp[idx][jdx]
        path = helper(0,0)
        return path
                
        
        