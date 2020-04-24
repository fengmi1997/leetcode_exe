# num_105
# 从前序与中序遍历序列构造二叉树
# 自己写出来了


import json
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):

        def repeat(preorder, inorder,root,tree):
            if len(inorder) == 1:
                return
            index = inorder.index(root)
            left_inorder = inorder[0:index]
            right_inorder = inorder[index+1:len(inorder)]
            left_preorder = preorder[1:len(left_inorder)+1]
            right_preorder = preorder[len(left_inorder)+1:len(preorder)]
            if left_preorder:
                tree.left = TreeNode(left_preorder[0])
                repeat(left_preorder, left_inorder,root=left_preorder[0],tree=tree.left)

            if right_preorder:
                tree.right = TreeNode(right_preorder[0])
                repeat(right_preorder, right_inorder,root=right_preorder[0],tree=tree.right)

        if preorder == []:
            return None
        else:

            root = preorder[0]
            tree = TreeNode(root)
            repeat(preorder, inorder,root,tree)
            return tree



def stringToIntegerList(input):
    return json.loads(input)


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

            preorder = [3,9,20,15,7]

            inorder = [9,3,15,20,7];

            ret = Solution().buildTree(preorder, inorder)

            out = treeNodeToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()