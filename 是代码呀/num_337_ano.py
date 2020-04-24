# num_337
# 打家劫舍
# 这可太绕了，写不出来


import json
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:

        def aftorder(root):
            if root is None:
                stole.append(0)
                no_stole.append(0)
                return

            aftorder(root.left)

            aftorder(root.right)
            val_num.append(root.val)
            stole_ano = stole[:]
            stole.append(root.val+no_stole[len(val_num)]+no_stole[len(val_num)-1])
            no_stole.append(stole_ano[len(val_num)]+stole_ano[len(val_num)-1])

        stole = []
        no_stole = []
        # 后序遍历的节点存储
        val_num = []
        aftorder(root)
        return max(stole[-1],no_stole[-1])




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

            ret = Solution().rob(root)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()