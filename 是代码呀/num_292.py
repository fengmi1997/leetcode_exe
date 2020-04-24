class Solution:
    def canWinNim(self, n: int) -> bool:
        if n % 4 == 0:
            return False
        else:
            return True


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

            ret = Solution().canWinNim(n)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()