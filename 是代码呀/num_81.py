# ac
# 搜索旋转排序数组2
# nums = [1,3,1,1,1]
# target = 3
# 很特殊的例子
# nums[left]=nums[mid]=nums[right],此时根本无法判断哪边是完全的升序，就left+1,right-1


class Solution(object):
    def search(self, nums, target):
        if len(nums) == 0:
            return False
        else:
            left = 0
            right = len(nums) - 1
            mid = int((left + right) / 2)
            while left <= right:
                if nums[mid] == target:
                    return True
                else:
                    if left == mid:
                        if nums[right] == target:
                            return True
                        else:
                            return False
                    elif right == mid:
                        if nums[left] == target:
                            return True
                        else:
                            return False
                    else:
                        if nums[left] == nums[mid] == nums[right]:
                            left += 1
                            right -= 1
                        # 左侧相等或升序
                        elif nums[left] <= nums[mid]:
                            if nums[left] <= target <= nums[mid]:
                                right = mid
                                mid = int((left + right) / 2)
                            else:
                                left = mid
                                mid = int((left + right) / 2)
                        # 右侧相等或升序
                        else:
                            if nums[mid+1] <= target <= nums[right]:
                                left = mid
                                mid = int((left + right) / 2)
                            else:
                                right = mid
                                mid = int((left + right) / 2)


if __name__ == '__main__':
    nums = [1,3,1,1,1]
    target = 1
    print(Solution().search(nums, target))