# num_98
# 验证二叉搜索树
# 不能全部ac，原因在于不能判断整棵数是不是子树
# 这个还改崩了

import json
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def repeat(root,lower,uper):
            while stack:
                if root.left is not None and lower < root.left.val < uper and root.left.val < root.val:
                    stack.pop(0)
                    stack.append(root.left.val)
                    repeat(root.left, lower=root.left.val, uper=root.val)
                if root.right is not None and lower < root.right.val < uper and root.right.val > root.val:
                    stack.pop(0)
                    stack.append(root.right.val)
                    repeat(root.right, lower=root.val, uper=root.right.val)
                if (root.left is not None and (lower > root.left.val or root.left.val > uper or root.left.val > root.val)) or \
                        (root.right is not None and(lower > root.right.val or root.right.val > uper or root.right.val < root.val)):
                    return False
            return True

        if root is None or (root.left is None and root.right is None):
            return True
        else:
            stack = [root.val]
            return repeat(root,  float('-inf'), float('inf'))


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