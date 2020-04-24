# num_516
# 最长回文子序列

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # 使用dp思想
        n = len(s)
        dp = [[0] * n for i in range(n)]
        # 注意basecase
        for i in range(n):
            dp[i][i] = 1
        # 倒着遍历
        for i in range(n, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]


if __name__ == '__main__':
    s = 'bbbab'
    print(Solution().longestPalindromeSubseq(s))
