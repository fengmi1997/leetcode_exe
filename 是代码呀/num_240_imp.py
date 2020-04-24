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
        # 从右上角开始遍历，左边的总是小，下边的总是大
        if matrix == []:
            return False
        m, n = len(matrix), len(matrix[0])
        if m == 0 or n == 0:
            return False
        i, j = 0, n - 1
        while m > i > -1 and n > j > -1:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                j -= 1
            if matrix[i][j] < target:
                i += 1
        return False


if __name__ == '__main__':
    matrix =[[]]
    print(Solution().searchMatrix(matrix,target=30))