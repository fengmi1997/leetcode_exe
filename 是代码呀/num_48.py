# ac
# 旋转图像


class Solution(object):
    def rotate(self, matrix):
        for i in range(0, len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(0, len(matrix)):
            for j in range(0, int(len(matrix)/2)):
                matrix[i][j], matrix[i][len(matrix)-j-1] = matrix[i][len(matrix)-j-1], matrix[i][j]
        return matrix


if __name__ == '__main__':
    matrix = [[5, 1, 9,11],[2, 4, 8,10],[13, 3, 6, 7],[15,14,12,16]]
    print(Solution().rotate(matrix))