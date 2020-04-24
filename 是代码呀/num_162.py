# num_162
# 寻找峰值
# 主要的思路就是看峰值的趋势

class Solution:
    def findPeakElement(self, nums) -> int:
        left, right = 0, len(nums) - 1
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return nums.index(max(nums))
        while left <= right:
            mid = left + (right - left) // 2
            if mid == 0 and nums[mid] > nums[mid + 1]:
                return mid
            if mid == len(nums)-1 and nums[mid]>nums[mid-1]:
                return mid
            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid
            if nums[mid + 1] > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

print(Solution().findPeakElement([1,2,3]))