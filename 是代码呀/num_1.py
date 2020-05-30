# ac
# 两数之和


class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            aim_number = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == aim_number:
                    return i, j


if __name__ == '__main__':
    nums = [3, 2, 3]
    target = 6
    print(Solution().twoSum(nums, target))