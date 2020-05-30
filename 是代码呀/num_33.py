# ac
# 搜索旋转排序数组
# 没有思路，参考别人的，但是分类好复杂，写完自己都有点蒙蔽了
# still have question
# 左侧代表[left,mid],右侧代表的是[mid+1,right]

class Solution(object):
    def search(self, nums, target):
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        else:
            left = 0
            right = len(nums) - 1
            mid = int((left + right) / 2)
            while right > left:
                if nums[mid] == target:
                    return mid
                else:
                    # 在最后，left == mid
                    if left == mid:
                        if nums[right] == target:
                            return right
                        else:
                            return -1
                    # 在最后，right == mid
                    elif right == mid:
                        if nums[left] == target:
                            return left
                        else:
                            return -1
                    elif right > mid or left < mid:
                        # target在左侧且左侧有序
                        if (nums[left] <= target) and (target < nums[mid]):
                            right = mid
                            mid = int((left + right) / 2)
                        # target在左侧且左无序
                        elif nums[left] > nums[mid] and (nums[right] < target or target < nums[mid]):
                            right = mid
                            mid = int((left + right) / 2)
                        # target在右侧且右侧有序
                        elif nums[mid+1] <= target <= nums[right]:
                            left = mid
                            mid = int((left + right) / 2)
                        # target在右侧且右侧无序
                        elif nums[left] < nums[mid+1] and (target < nums[left] or target > nums[mid]):
                            left = mid
                            mid = int((left + right) / 2)
                        # target不在整个序列里面
                        else:
                            return -1


if __name__ == '__main__':
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(Solution().search(nums, target))