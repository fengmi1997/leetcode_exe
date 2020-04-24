# num_96
# 不同的二叉搜索树
# 代码好写，思路不好想


class Solution:
    def numTrees(self, n: int) -> int:
        g = [0] * (n+1)
        g[0],g[1] = 1,1
        for i in range(2, n+1):
            for index in range(1, i+1):
                g[i] += g[index-1] * g[i - index]
        return g[n]


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            n = int(line);

            ret = Solution().numTrees(n)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()