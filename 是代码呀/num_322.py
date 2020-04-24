class Solution:
    def coinChange(self, coins, amount: int) -> int:
        dp = [[-1] * len(coins) for _ in range(amount + 1)]
        # 第一列的初始化
        for i in range(amount + 1):
            if coins[0] < i:
                new_i = i - coins[0]
                while new_i > 0:
                    dp[i][0] = dp[new_i][0] + 1
                    new_i = new_i - coins[0]
                if new_i <= 0:
                    dp[i][0] = -1
            elif coins[0] == i:
                dp[i][0] = 1
            else:
                dp[i][0] = -1
        for i in range(amount + 1):
            for j in range(1, len(coins)):
                if coins[j] < i:
                    new_i = i - coins[j]
                    if new_i < 0:
                        return -1
                    dp[i][j] = dp[new_i][j] + 1
                elif coins[j] == i:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[-1][-1]


if __name__ =='__main__':
    coins = [1,2,5]
    amount = 11
    print(Solution().coinChange(coins,amount))