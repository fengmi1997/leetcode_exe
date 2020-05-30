# ac
# 下一个序列
# 不会，看了别人的思路写的
# nums
# 从后往前找,找到索引最大的k,nums[k]<=nums[k+1]
# 然后找到索引最大的l,使得nums[l]>nums[k]
# 把k索引以后的颠倒顺序

class Solution(object):
    def nextPermutation(self, nums):
        if len(nums) == 2:
            if nums[0] >= nums[1]:
                return nums
            else:
                change_num = nums[0]
                nums[0] = nums[1]
                nums[1] = change_num
                return nums
        else:
            k = len(nums) - 2
            while k > 0 and nums[k] >= nums[k+1]:
                k -= 1

            l = k + 1
            while l < len(nums) and nums[l] > nums[k]:
                l += 1
            l -= 1
            change_num = nums[k]
            nums[k] = nums[l]
            nums[l] = change_num
            if k == l:
                i = 0
                j = len(nums) - 1
            else:
                j = len(nums) - 1
                i = k + 1
            while i < j:
                change_num2 = nums[i]
                nums[i] = nums[j]
                nums[j] = change_num2
                j -= 1
                i += 1
            return nums


if __name__ == '__main__':
    nums = [2,2,7,5,4,3,2,2,1]
    print(Solution().nextPermutation(nums))