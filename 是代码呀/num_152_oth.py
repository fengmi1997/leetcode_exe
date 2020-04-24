# num_152
# 乘积最大子序列
# 参考了别人的思路

class Solution:
    def maxProduct(self, nums) -> int:
        max_res = nums[0]
        imax,imin = 1,1
        for i in range(len(nums)):
            if nums[i] < 0:
                imax,imin = imin,imax
            imax = max(imax*nums[i],nums[i])
            imin = min(imin*nums[i],nums[i])
            max_res = max(imax,max_res)
        return max_res


if __name__ == "__main__":
    nums=[1,0]
    print(Solution().maxProduct(nums))