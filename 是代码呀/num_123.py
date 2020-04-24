
class Solution:
    def maxProfit(self, prices) -> int:
        dp = [[[0]*2 for _ in range(3)] for _ in range(len(prices))]
        dp[0][1][1] = -prices[0]
        dp[0][1][0],dp[0][2][0],dp[0][2][1],dp[0][0][1] =float('-inf'),float('-inf'),float('-inf'),float('-inf')
        for i in range(1, len(prices)):
            for k in range(1, 3):
                dp[i][k][0] = max(dp[i-1][k][0],dp[i-1][k][1]+prices[i])
                dp[i][k][1] = max(dp[i-1][k][1],dp[i-1][k-1][0]-prices[i])
        return max(dp[-1][2][0],dp[-1][1][0])


if __name__ =='__main__':
    prices = [3,3,5,0,0,3,1,4]
    print(Solution().maxProfit(prices))