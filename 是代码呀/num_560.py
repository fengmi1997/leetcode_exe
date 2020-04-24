# num_560
# 和为K的子数组

"""
暴力法，超时
"""
# class Solution:
#     def subarraySum(self, nums, k: int) -> int:
#         res = 0
#         for i in range(len(nums)):
#             sum = nums[i]
#             if sum == k:
#                 res += 1
#             for j in range(i+1,len(nums)):
#                 sum = sum + nums[j]
#                 if sum == k:
#                     res += 1
#         return res
"""
python还是超时
"""
class Solution:
    def subarraySum(self, nums, k: int) -> int:
        res = 0
        sum_list = [0]*len(nums)
        sum_list[0] = nums[0]
        for i in range(1,len(nums)):
            sum_list[i] = sum_list[i-1] + nums[i]

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                sum = sum_list[j] - sum_list[i] + nums[i]
                if sum == k:
                    res += 1
        return res


if __name__ == '__main__':
    nums = [1,1,1]
    k = 2
    print(Solution().subarraySum(nums,k))