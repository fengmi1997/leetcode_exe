# num_200
# 岛屿数量
# 用栈写出来了


class Solution:
    def numIslands(self, grid) -> int:
        count = 2
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    # 找到一个为1的数字后，设置一个栈
                    stack = []
                    stack.append([i, j])
                    while stack:
                        # ele_x,ele_y是栈顶对应的位置
                        ele = stack.pop(0)
                        ele_x, ele_y = ele[0], ele[1]
                        if grid[ele_x][ele_y] != '1':
                            continue
                        grid[ele_x][ele_y] = count
                        if ele_y + 1 < len(grid[0]):
                            if grid[ele_x][ele_y + 1] == '1':
                                stack.append([ele_x, ele_y + 1])
                        if ele_x + 1 < len(grid):
                            if grid[ele_x + 1][ele_y] == '1':
                                stack.append([ele_x + 1, ele_y])
                        if ele_x - 1 > -1:
                            if grid[ele_x - 1][ele_y] == '1':
                                stack.append([ele_x - 1, ele_y])
                        if ele_y - 1 > -1:
                            if grid[ele_x][ele_y - 1] == '1':
                                stack.append([ele_x, ele_y - 1])
                    count += 1
        return count - 2


if __name__=='__main__':
    grid = [["1","1","1"],["0","1","0"],["1","1","1"]]
    print(Solution().numIslands(grid))