# num_238
# 除自身以外数组的乘积

# 没有节省空间
# class Solution:
#     def productExceptSelf(self, nums):
#         L = [1]*len(nums)
#         R = [1]*len(nums)
#         res = [1] * len(nums)
#         for i in range(1,len(nums)):
#             L[i] = L[i-1]*nums[i-1]
#         for j in range(len(nums)-2, -1, -1):
#             R[j] = R[j+1]*nums[j+1]
#         for i in range(len(nums)):
#             res[i]=L[i]*R[i]
#         return res


class Solution:
    def productExceptSelf(self, nums):
        L = [1]*len(nums)
        res = [1] * len(nums)
        for i in range(1,len(nums)):
            L[i] = L[i-1]*nums[i-1]
        r = 1
        for j in range(len(nums)-1, -1, -1):
            res[j] = r*L[j]
            r = r*nums[j]
        return res


if __name__ == '__main__':
    nums = [1,2,3,4]
    print(Solution().productExceptSelf(nums))