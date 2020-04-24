# num_39
# 组合总和


class Solution:
    def combinationSum(self, candidates, target):
        def repeat(i, one_res):
            if sum(one_res) == target:
                res.append(one_res)
                return
            if sum(one_res) > target or i == len(candidates):
                return
            for j in range(i, len(candidates)):
                # 还可以优化一下
                if sum(one_res) > target:
                    break
                repeat(j, one_res+[candidates[j]])

        res = []
        one_res = []
        repeat(0, one_res)
        return res


if __name__ == '__main__':
    candidates = [2,3,6,7]
    target = 7
    print(Solution().combinationSum(candidates, target))