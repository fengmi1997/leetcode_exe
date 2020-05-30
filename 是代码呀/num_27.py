# ac
# 移除元素


class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        nums.sort(reverse=False)
        while i < len(nums) and nums[i] != val:
            i += 1
        j = i
        while j < len(nums) and nums[j] == val:
            nums.remove(nums[j])
            j = i
        return len(nums)


if __name__ == '__main__':
    nums = [3, 2,2, 3]
    val = 3
    print(Solution().removeElement(nums, val))