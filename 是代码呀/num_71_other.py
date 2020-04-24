# num_71
# 泡菜的代码


class Solution:
    def simplifyPath(self, path):
        stack = []
        path = path.split("/")

        for item in path:
            if item == "..":
                if stack: stack.pop()
            elif item and item != ".":
                stack.append(item)
        return "/" + "/".join(stack)


if __name__ == '__main__':
    path = '/home//foo/'
    print(Solution().simplifyPath(path))