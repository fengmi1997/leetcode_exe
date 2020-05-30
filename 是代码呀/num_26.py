# ac
# 删除排序数组中的重复项
# 用了两个指针，自己写的


class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        j = 1
        while i < len(nums):
            while j < len(nums) and nums[j] == nums[i]:
                nums.remove(nums[j])
            i += 1
            j = i + 1
        return len(nums)


if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(Solution().removeDuplicates(nums))