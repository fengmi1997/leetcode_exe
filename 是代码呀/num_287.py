# num_287
# 寻找重复数


# 超时，O(n^2)
# class Solution:
#     def findDuplicate(self, nums) -> int:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[j] == nums[i]:
#                     return nums[i]

class Solution:
    def findDuplicate(self, nums) -> int:
        for i in range(1, len(nums)):
            if nums[i] in nums[:i]:
                return nums[i]



if __name__ == '__main__':
    nums = [2,1,3,4,2]
    print(Solution().findDuplicate(nums))