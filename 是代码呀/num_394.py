# num_394
# 字符串解码
# 参考思路写的
# 是一个很不错的题


class Solution:
    def decodeString(self, s: str) -> str:
        # 设置一个辅助栈
        stack_str = []
        multi = 0
        res = ''
        # 遍历s
        for c in s:
            # 如果是数字
            if '0' <= c <= '9':
                multi = multi * 10 + int(c)
            # 如果是字母
            elif 'A' <= c <= 'Z' or 'a' <= c <= 'z':
                res += c
            elif c == '[':
                stack_str.append(multi)
                stack_str.append(res)
                multi, res = 0, ''
            else:
                last_res = stack_str[-1]
                cur_multi = stack_str[-2]
                stack_str.pop()
                stack_str.pop()
                """
                last_res:放到栈里面不断地去加
                res:当前需要乘的
                """
                res = last_res + cur_multi * res
        return res


def stringToString(input):
    return input[1:-1].decode('string_escape')


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            # line = next(lines)
            s = "3[a]2[b4[F]c]"

            ret = Solution().decodeString(s)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()