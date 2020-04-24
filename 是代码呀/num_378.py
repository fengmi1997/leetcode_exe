class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        tmp=[]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                tmp.append(matrix[i][j])
        tmp=sorted(tmp)
        return tmp[k-1]


print(Solution().kthSmallest(matrix=[[1,2],[1,3]],k=2))