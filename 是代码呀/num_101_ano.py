# num-101
# 102的基础上写出来了

import json
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        stack = [root]
        res = []
        j = 0
        while stack:
            res.append([])
            for i in range(len(stack)):
                node = stack.pop(0)
                if node is None:
                    res[j].append(99999)
                    continue
                else:
                    res[j].append(node.val)
                if node.left:
                    stack.append(node.left)
                else:
                    stack.append(None)
                if node.right:
                    stack.append(node.right)
                else:
                    stack.append(None)
            index = 0
            while index < ((len(res[j]))/2):
                if res[j][index] != res[j][len(res[j])-index-1]:
                    return False
                index+=1
            j += 1
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