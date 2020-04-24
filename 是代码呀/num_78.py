# num_78
# 子集
# 自己写出来了,可以看成是39+46的组合题


class Solution:
    def subsets(self, nums):
        def repeat(j, one_res):
            set_one_res = set(one_res)
            # 没有重复元素
            if len(one_res) == len(set_one_res):
                res.append(one_res)
                if len(one_res) == len(nums):
                    return
            for i in range(j, len(nums)):
                if nums[i] not in one_res:
                    repeat(i, one_res+[nums[i]])

        res = []
        one_res = []
        repeat(0, one_res)
        return res


if __name__ == '__main__':
    nums = [1,2,3]
    print(Solution().subsets(nums))