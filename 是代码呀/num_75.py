# ac
# 颜色分类
# 完全没思路，看了官方解答写的


class Solution(object):
    def sortColors(self, nums):
        l = 0
        r = len(nums) - 1
        k = 0
        while k <= r:
            if nums[k] == 2:
                nums[r], nums[k] = nums[k], nums[r]
                r -= 1
            elif nums[k] == 1:
                k += 1
            else:
                nums[k], nums[l] = nums[l], nums[k]
                k += 1
                l += 1
        return nums


if __name__ == '__main__':
    nums = [2,0,2,1,1,2]
    print(Solution().sortColors(nums))