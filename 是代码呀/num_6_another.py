# num_6
# Z字形变换
# 大神


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1: flag = -flag
            i += flag
        return "".join(res)


if __name__ == '__main__':
    s = 'LEETCOD'
    numRows = 3
    print(Solution().convert(s,numRows))