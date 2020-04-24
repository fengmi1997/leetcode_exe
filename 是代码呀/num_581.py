# num_581
# 最短无序连续子数组
# ac


class Solution:
    def findUnsortedSubarray(self, nums) -> int:
        new = sorted(nums)
        i, j = 0, len(nums)-1
        while i < j:
            if new[i] != nums[i] and new[j] != nums[j]:
                return j-i+1
            if new[i] == nums[i]:
                i += 1
            if new[j] == nums[j]:
                j -= 1
        return 0


if __name__ == '__main__':
    nums = [2, 6, 4, 8, 10, 9, 15]
    print(Solution().findUnsortedSubarray(nums))