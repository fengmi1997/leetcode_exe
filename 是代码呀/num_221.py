# num_221
# 最大正方形
# 这个动态规划很难写
# 没想出来思路

class Solution:
    def maximalSquare(self, matrix):
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        res = 0
        if matrix == []:
            return 0
        # 初始第一行，只取决于左侧
        for j in range(len(matrix[0])):
            dp[0][j] = int(matrix[0][j])
            res = max(res, dp[0][j])
        for i in range(len(matrix)):
            dp[i][0] = int(matrix[i][0])
            res = max(res, dp[i][0])
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                    res = max(res, dp[i][j])
        return res * res


if __name__ == '__main__':
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    print(Solution().maximalSquare(matrix))

