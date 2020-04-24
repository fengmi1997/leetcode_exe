class Solution:
    def numWays(self, n: int, relation, k: int) -> int:
        map_relation = [[0] * n for _ in range(n)]
        for rel in relation:
            i, j = rel[0], rel[1]
            map_relation[i][j] = 1
        # 表示当前步的结果
        res = [0]
        new_res = []
        for num in range(k+1):
            if num == k:
                return res.count(n - 1)
            for ele in res:
                for j in range(n):
                    if map_relation[ele][j] == 1:
                        new_res.append(j)
            res = new_res
            new_res = []

n=5
relation=[[0,2],[2,1],[3,4],[2,3],[1,4],[2,0],[0,4]]
k=3
print(Solution().numWays(n,relation,k))