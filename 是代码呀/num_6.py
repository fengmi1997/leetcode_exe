# num_6
# Z字形变换
# 二维数组写出来了，代码质量不高


class Solution:
    def convert(self, s, numRows):
        if s == '' or numRows==1:
            return s
        else:
            # 定义块的个数为num,向上取整
            num = -(-len(s)//(2*numRows-2))
            # 总的列数可以表示为num*(numRows-1)
            # 定义一个二维的列表
            newlist = [['/' for t in range(num*(numRows-1))]for t in range(numRows)]
            str = s
            for i in range(num):
                index = numRows - 2
                for j in range(numRows-1):
                    if j == 0:
                        for t in range(numRows):
                            if str:
                                newlist[t][i*(numRows-1)] = str[0]
                                str = str[1:]
                    if j != 0:
                        if str:
                            newlist[index][i*(numRows-1)+j] = str[0]
                            str = str[1:]
                            index -= 1
            result = ''
            for i in range(numRows):
                for j in range(num*(numRows-1)):
                    if newlist[i][j] != '/':
                        result += newlist[i][j]

            return result


if __name__ == '__main__':
    s = ''
    numRows = 1
    print(Solution().convert(s,numRows))