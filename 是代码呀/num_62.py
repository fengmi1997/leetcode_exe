# num_62
# 不同路径,简单的动态规划


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[-1][-1]


if __name__ == '__main__':
    m,n =7,3
    print(Solution().uniquePaths(m,n))