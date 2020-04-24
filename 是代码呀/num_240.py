# num_240

"""
用栈的方法超时了
"""
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == []:
            return False
        m, n = len(matrix), len(matrix[0])
        if m == 0 or n == 0:
            return False
        stack = []
        stack.append([0, 0])
        while stack:
            ele = stack.pop(0)
            ele_x, ele_y = ele[0], ele[1]
            if matrix[ele_x][ele_y] == target:
                return True
            if matrix[ele_x][ele_y] < target:
                if ele_y + 1 < n:
                    if matrix[ele_x][ele_y + 1] <= target:
                        stack.append([ele_x, ele_y + 1])
                if ele_x + 1 < m:
                    if matrix[ele_x + 1][ele_y] <= target:
                        stack.append([ele_x + 1, ele_y])
            if matrix[ele_x][ele_y] > target:
                return False
        return False


if __name__ == '__main__':
    matrix =[[]]
    print(Solution().searchMatrix(matrix,target=30))