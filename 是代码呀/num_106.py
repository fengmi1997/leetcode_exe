# num_106
# 从后序与中序遍历序列构造二叉树
# 自己写出来了


import json
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder):

        def repeat(inorder, postorder,root,tree):
            if len(inorder) == 1:
                return
            index = inorder.index(root)
            left_inorder = inorder[0:index]
            right_inorder = inorder[index+1:len(inorder)]
            left_postorder = postorder[0:index]
            right_postorder = postorder[index:len(postorder)-1]
            if left_postorder:
                tree.left = TreeNode(left_postorder[-1])
                repeat(left_inorder,left_postorder,root=left_postorder[-1],tree=tree.left)

            if right_postorder:
                tree.right = TreeNode(right_postorder[-1])
                repeat(right_inorder,right_postorder,root=right_postorder[-1],tree=tree.right)

        if postorder == []:
            return None
        else:

            root = postorder[-1]
            tree = TreeNode(root)
            repeat( inorder,postorder,root,tree)
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
            inorder = [9, 3, 15, 20, 7];
            postorder = [9,15,7,20,3]



            ret = Solution().buildTree(inorder, postorder)

            out = treeNodeToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()