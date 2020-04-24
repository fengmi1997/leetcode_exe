# num_198
# 打家劫舍
# 我的第一个动态规划，简单题

import json
class Solution:
    def rob(self, nums) -> int:
        dp = [0] * (len(nums) +2)
        k = 2
        for i in nums:
            dp[k] = max(dp[k-1],dp[k-2]+i)
            k+=1
        return dp[k-1]


def stringToIntegerList(input):
    return json.loads(input)


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            nums = [2,7,9,3,1];

            ret = Solution().rob(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()