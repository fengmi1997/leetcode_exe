# num_98
# 验证二叉搜索树
# 按照思路改的

import json
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None or (root.left is None and root.right is None):
            return True
        else:
            stack = [[root, float('-inf'), float('inf')]]

            while stack:
                root,lower,uper = stack.pop(0)
                if root.val >= uper or root.val <= lower:
                    return False
                if root.left:
                    stack.append([root.left,lower,root.val])
                if root.right:
                    stack.append([root.right,root.val,uper])
            return True





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

            ret = Solution().isValidBST(root)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()