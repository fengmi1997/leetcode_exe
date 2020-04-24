# num_617
# 合并二叉树
# 写乱了，难受


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:

        def repeat(t1, t2,tree):
            if (t1 is None) and (t2 is None):
                return
            if t1 and t2:
                tree.val = t1.val + t2.val
            if t2 and (t1 is None):
                tree.val = t2.val
            if t1 and (t2 is None):
                tree.val = t1.val
            if t1:
                tree.left = TreeNode(0)
                if t2 is None:
                    repeat(t1.left, None,tree.left)
                else:
                    repeat(t1.left, t2.left,tree.left)
            else:
                if t2 is None:
                    pass
                else:
                    tree.left = TreeNode(0)
                    repeat(None, t2.left, tree.left)
            if t1:
                tree.right = TreeNode(0)
                if t2 is None:
                    repeat(t1.right, None, tree.right)
                else:
                    repeat(t1.right, t2.right,tree.right)
            else:
                if t2 is None:
                    pass
                else:
                    tree.right = TreeNode(0)
                    repeat(None, t2.right, tree.right)
        tree = TreeNode(0)
        repeat(t1, t2, tree)
        return tree


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


def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"


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
            t1 = stringToTreeNode(line);
            line = next(lines)
            t2 = stringToTreeNode(line);

            ret = Solution().mergeTrees(t1, t2)

            out = treeNodeToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()