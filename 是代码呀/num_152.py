# num_152
# 乘积最大子序列
# 暴力法超时

class Solution:
    def maxProduct(self, nums) -> int:
        res = nums[0]
        for i in range(0, len(nums)):
            L = [1] * (len(nums)-i)
            L[0] = nums[i]
            for j in range(1, len(L)):
                L[j] = L[j-1]*nums[i+j]
            res = max(res, max(L))
        return res


if __name__ == "__main__":
    nums=[-2]
    print(Solution().maxProduct(nums))