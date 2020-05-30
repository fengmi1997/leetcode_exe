# ac
# 搜索插入位置
# 其实并不是二分查找


class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        if nums[left] >= target:
            return 0
        elif nums[right] < target:
            return len(nums)
        elif nums[right] == target:
            return len(nums) - 1
        else:
            while left <= right:
                if left == right:
                    return left
                elif right - left == 1:
                    if nums[right] == target:
                        return right
                    elif nums[right] < target:
                        return right+1
                    elif nums[left] < target < nums[right]:
                        return right
                    else:
                        return left
                else:
                    if target < nums[right]:
                        right -= 1
                    else:
                        left += 1


if __name__ == '__main__':
    nums = [1,3,5,6]
    target = 2
    print(Solution().searchInsert(nums, target))