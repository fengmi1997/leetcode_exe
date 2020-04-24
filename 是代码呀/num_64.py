# num_64
# 最小路径和
# 简单的动态规划

# 另外用了存储空间
class Solution:
    def minPathSum(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        # 这是浅拷贝
        d = [(n)*[0]]*m
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    d[i][j] = grid[i][j]
                elif i == 0 and j > 0:
                    d[i][j] = grid[i][j] + d[i][j-1]
                elif j == 0 and i > 0:
                    d[i][j] = grid[i][j] + d[i-1][j]
                else:
                    d[i][j] = grid[i][j] + min(d[i-1][j], d[i][j-1])
        return d[-1][-1]


# class Solution:
#     def minPathSum(self, grid) -> int:
#         m = len(grid)
#         n = len(grid[0])
#         for i in range(m):
#             for j in range(n):
#                 if i == 0 and j == 0:
#                     continue
#                 elif i == 0 and j > 0:
#                     grid[i][j] = grid[i][j] + grid[i][j-1]
#                 elif j == 0 and i > 0:
#                     grid[i][j] = grid[i][j] + grid[i-1][j]
#                 else:
#                     grid[i][j] = grid[i][j] + min(grid[i-1][j], grid[i][j-1])
#         return grid[-1][-1]


if __name__ == '__main__':
    grid =[[1,3,1],[1,5,1],[4,2,1]]
    print(Solution().minPathSum(grid))