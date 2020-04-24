# num_448
# 找到所有数组中消失的数字

# 超时
# class Solution:
#     def findDisappearedNumbers(self, nums):
#         res = list(range(1, len(nums)+1))
#         nums = set(nums)
#         for num in nums:
#             if num in res:
#                 res.remove(num)
#         return res

# another 超时
# class Solution:
#     def findDisappearedNumbers(self, nums):
#         res = []
#         for i in range(1,len(nums)+1):
#             if i not in nums:
#                 res.append(i)
#         return res

"""
这是一个不超时的办法，直接在set元素上进行相减
"""
class Solution:
    def findDisappearedNumbers(self, nums):
        res = set(list(range(1, len(nums) + 1)))
        nums = set(nums)
        return list(res-nums)


if __name__ == '__main__':
    nums = [4,3,2,7,8,2,3,1]
    print(Solution().findDisappearedNumbers(nums))