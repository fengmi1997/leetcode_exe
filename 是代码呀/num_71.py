# num_71
# 简化路径
# 给出一个文件的绝对路径
# 分情况讨论
# 自己可以想出来
# 错了
# '.'里面不对


class Solution:
    def simplifyPath(self, digits):
        standrad_path = []
        if len(digits) == 0:
            return ''
        else:
            standrad_path.append(digits[0])
            i = 1
            while i < len(digits):
                if digits[i] == '/':
                    if standrad_path[-1] != '/':
                        standrad_path.append(digits[i])
                elif digits[i] == '.':
                    if i < len(digits) - 1:
                        if digits[i+1] == '.':
                            if len(standrad_path) == 1:
                                standrad_path.append(digits[i])
                            if len(standrad_path) >= 1:
                                if standrad_path[-1] == '.':

                                    standrad_path.append(digits[i])
                                elif len(standrad_path) >= 2:
                                    standrad_path.pop()
                                    standrad_path.pop()
                else:
                    standrad_path.append(digits[i])
                i += 1
            if len(standrad_path) > 1 and standrad_path[-1] == '/':
                standrad_path.pop()
            str = ''.join(standrad_path)
            return str


if __name__ == '__main__':
    digits = '/../'
    print(Solution().simplifyPath(digits))