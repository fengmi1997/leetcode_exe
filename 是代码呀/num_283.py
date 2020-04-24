# num_283
# 移动零
# 简单题


class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i, j = 0, 0
        while (j < len(nums)-1) and (i < len(nums)-1):
            if i > j:
                break
            # 如果i对应的元素为0，j对应的元素不为0，就交换
            if i <= j and nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[i] != 0:
                i += 1
                j += 1
            else:
                j += 1

        if (i <= j) and (j <= len(nums)-1) and (i <= len(nums)-1):
            if nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
        return nums


if __name__ == '__main__':
    nums = [1,0,1]
    print(Solution().moveZeroes(nums))