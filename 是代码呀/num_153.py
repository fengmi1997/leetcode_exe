# ac
# 寻找旋转排序数组中的最小值


class Solution(object):
    def findMin(self, nums):
        if len(nums) == 0:
            return False
        else:
            left = 0
            right = len(nums) - 1
            mid = int((left + right) / 2)
            while left <= right:
                if left == mid:
                    if nums[mid] < nums[right]:
                        return nums[mid]
                    else:
                        return nums[right]
                if right == mid:
                    if nums[mid] < nums[left]:
                        return nums[mid]
                    else:
                        return nums[left]
                else:
                    if nums[left] < nums[mid] < nums[right]:
                        return nums[left]
                    elif nums[left] < nums[mid]:
                        left = mid
                        mid = int((left + right) / 2)
                    else:
                        right = mid
                        mid = int((left + right) / 2)


if __name__ == '__main__':
    nums = [5,1,2,3,4]
    print(Solution().findMin(nums))