# num_437
# 路径总和3


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
能输出每一个路径的和，但是和结果有差距
"""


# class Solution:
#     def pathSum(self, root: TreeNode, sum: int) -> int:
#         def deep_circle(root, sum_list):
#             if root is None:
#                 print(sum_list)
#                 flag = 0
#                 for one_sum_list in res:
#                     if set(sum_list) >= set(one_sum_list):
#                         flag = 1
#                 if flag == 0:
#
#                     res.append(sum_list)
#                 return
#             deep_circle(root.left, sum_list+[sum_list[-1] + root.val])
#             deep_circle(root.right, sum_list+[sum_list[-1] + root.val])
#         sum_list = [0]
#         res = []
#         deep_circle(root, sum_list)
#         return res

class Solution:

    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        return self.dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def dfs(self, root, path):
        if not root:
            return 0
        path -= root.val
        return (1 if path == 0 else 0) + self.dfs(root.left, path) + self.dfs(root.right, path)


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


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
            root = stringToTreeNode(line);
            line = next(lines)
            sum = int(line);

            ret = Solution().pathSum(root, sum)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()