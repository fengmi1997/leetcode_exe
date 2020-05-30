# 参照别人的思路


class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort(reverse=False)
        path = []
        res = []
        self.huisu(candidates,target,path,res)
        return res

    def huisu(self, candidates, target, path,res):
        if target == 0:
            res.append(path[:])

        for index in range(0, len(candidates)):
            residue = target - candidates[index]
            if residue < 0:
                break
            path.append(candidates[index])
            self.huisu(candidates, residue, path, res)
            path.pop()


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    solution = Solution()
    result = solution.combinationSum(candidates, target)
    print(result)
