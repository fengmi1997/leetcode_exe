# num-101
# 有问题，不能得到中间是空的情况

import json
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 广度遍历
        stack = [root]
        val_stack = []
        while stack:
            node = stack.pop(0)
            val_stack.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        val_stack.pop(0)
        i = 1
        while val_stack:
            start = 0
            end = (2 ** i)
            one_part = val_stack[start:end]
            del val_stack[start:end]
            j = 0
            while j < (len(one_part)/2):
                if one_part[j] != one_part[len(one_part)-j-1]:
                    return False
                else:
                    j += 1
            i += 1
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

            ret = Solution().isSymmetric(root)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()