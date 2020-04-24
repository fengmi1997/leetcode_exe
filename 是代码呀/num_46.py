# num_46
# 全排列
# 自己写出来了

class Solution:
    def permute(self, nums):
        def repeat(one_res):
            if len(one_res) == len(nums):
                res.append(one_res)
                return
            for i in range(0, len(nums)):
                if nums[i] not in one_res:
                    repeat(one_res+[nums[i]])

        res = []
        one_res = []
        repeat(one_res)
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().permute(nums))