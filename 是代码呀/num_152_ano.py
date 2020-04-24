# num_152
# 乘积最大子序列
# 超出内存限制

class Solution:
    def maxProduct(self, nums) -> int:
        if len(nums) == 1:
            return max(nums)
        else:
            dp = [[0]*(len(nums)-1) for _ in range(len(nums)-1)]
            for j in range(len(dp)):
                dp[0][j] = nums[j] * nums[j+1]
            maxer = max(dp[0])
            for i in range(1, len(dp)):
                for j in range(0,len(dp)-i):
                    dp[i][j] = nums[j] * dp[i-1][j+1]
                maxer = max(maxer, max(dp[i]))
            return max(maxer,max(nums))


if __name__ == "__main__":
    nums=[1,-2,3,-4,-3,-4,-3]
    print(Solution().maxProduct(nums))