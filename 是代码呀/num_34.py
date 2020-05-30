# ac
# 在排序数组中查找元素的第一个和最后一个位置


class Solution(object):
    def searchRange(self, nums, target):
        if len(nums) == 0:
            return [-1, -1]
        else:
            left = 0
            right = len(nums) - 1
            mid = int((left + right)/2)
            while left <= right:
                if nums[left] == nums[right] == target:
                    return [left, right]
                elif left == mid:
                    if nums[left] == target:
                        return [left, mid]
                    elif nums[right] == target:
                        return [right, right]
                    else:
                        return [-1, -1]
                elif right == mid:
                    if nums[right] == target:
                        return [right, mid]
                    elif nums[left] == target:
                        return [left, left]
                    else:
                        return [-1, -1]
                else:
                    if nums[mid] < target:
                        left = mid
                        mid = int((left + right) / 2)
                    elif nums[mid] > target:
                        right = mid
                        mid = int((left + right) / 2)
                    else:
                        if nums[left] == target:
                            right -= 1
                            mid = int((left + right) / 2)
                        elif nums[right] == target:
                            left += 1
                            mid = int((left + right) / 2)
                        else:
                            left += 1
                            right -= 1
                            mid = int((left + right) / 2)


if __name__ == '__main__':
    nums = [1,2,2]
    target = 2
    print(Solution().searchRange(nums, target))