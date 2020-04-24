# num_516
# 最长回文子序列

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)-1):
            dp[i][i] = 1
            if s[i] == s[i+1]:
                dp[i][i+1] = 2
            else:
                dp[i][i+1] = 1
        dp[len(s)-1][len(s)-1] = 1
        for i in range(len(s)-3, -1, -1):
            for j in range(i+2, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]+2
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])
        return dp[0][len(s)-1]


if __name__ == '__main__':
    s = 'cbba'
    print(Solution().longestPalindromeSubseq(s))
