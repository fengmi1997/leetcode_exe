# 超时
# class Solution:
#     def numSquares(self, n: int) -> int:
#         # import functools
#         # @functools.lru_cache(None)
#         def repeat(n, one_res):
#             if n == 0:
#                 res.append(len(one_res))
#                 return
#             num = int(pow(n, 1 / 2))
#             for i in range(num, 0, -1):
#                 repeat(n - i*i, one_res+[i * i])
#         res = []
#         one_res = []
#         repeat(n, one_res)
#         return min(res)

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]*(n+1)
        for i in range(0,n+1):
            dp[i] = i
        for i in range(1,n+1):
            for j in range(int(pow(i,1/2)),0,-1):
                dp[i] = min(dp[i-j*j]+1,dp[i])
        return dp[-1]


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            n = int(line);

            ret = Solution().numSquares(n)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()