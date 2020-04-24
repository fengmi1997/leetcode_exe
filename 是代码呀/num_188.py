
class Solution:
    def maxProfit(self,k, prices) -> int:
        if prices == [] or k==0:
            return 0
        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(len(prices))]
        dp[0][1][1] = -prices[0]
        dp[0][1][0], dp[0][0][1] = float('-inf'), float('-inf')

        for i in range(2, k + 1):
            dp[0][i][0] = float('-inf')
            dp[0][i][1] = float('-inf')

        for i in range(1, len(prices)):
            for k in range(1, k + 1):
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
        res = 0
        for k in range(1, k + 1):
            res = max(res, dp[-1][k][0])
        return res


if __name__ =='__main__':
    prices = [1,3]
    k=0
    print(Solution().maxProfit(k,prices))