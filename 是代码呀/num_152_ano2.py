# num_152
# 乘积最大子序列
# 还是超时

class Solution:
    def maxProduct(self, nums) -> int:
        if len(nums) == 1:
            return max(nums)
        else:
            dp = [0]*(len(nums)-1)
            for j in range(len(dp)):
                dp[j] = nums[j] * nums[j+1]
            maxer = max(dp)
            i = 1
            while i < len(dp):
                for j in range(0, len(dp)-i):
                    dp[j] = nums[j] * dp[j+1]
                maxer = max(maxer, max(dp))
                i += 1
            return max(maxer, max(nums))


if __name__ == "__main__":
    nums=[1,-2,3,-4,-3,-4,-3]
    print(Solution().maxProduct(nums))