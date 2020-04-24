# num_70
# 爬楼梯

# 动态规划
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0, 1]
        for i in range(1, n+1):
            dp[0], dp[1] = dp[1], dp[0] + dp[1]
        return dp[1]


if __name__ == '__main__':
    n = 35
    print(Solution().climbStairs(n))