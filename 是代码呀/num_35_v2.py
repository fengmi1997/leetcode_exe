# ac
# 搜索插入位置
# 别人的版本


class Solution(object):
    def searchInsert(self, nums, target):
        low = 0
        high = len(nums)
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > target:
                high = mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid
        return low


if __name__ == '__main__':
    nums = [1,3,5,6]
    target = 2
    print(Solution().searchInsert(nums, target))