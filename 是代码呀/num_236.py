# num_236
# 二叉树的最近公共祖先


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
#自己写的
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 判断root的左节点和右节点是否是p
        def repeat_p(root, pos_p, ele):
            if root is None:
                return
            if root.val == ele:
                res.append(pos_p)
            repeat_p(root.left, pos_p+[root.left],ele)
            repeat_p(root.right, pos_p+[root.right],ele)
        res = []
        pos_p = [root]
        repeat_p(root, pos_p,p)
        pos_p = [root]
        repeat_p(root,pos_p,q)
        for i in range(len(res[0])-1,-1,-1):
            for j in range(len(res[1])-1,-1,-1):
                if res[0][i].val == res[1][j].val:
                    return res[0][i]
'''

'''
#官方
class Solution:

    def __init__(self):
        # Variable to store LCA node.
        self.ans = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def recurse_tree(current_node):

            # If reached the end of a branch, return False.
            if not current_node:
                return False

            # Left Recursion
            left = recurse_tree(current_node.left)

            # Right Recursion
            right = recurse_tree(current_node.right)

            # If the current node is one of p or q
            mid = current_node == p or current_node == q

            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                self.ans = current_node

            # Return True if either of the three bool values is True.
            return mid or left or right

        # Traverse the tree
        recurse_tree(root)
        return self.ans
'''

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        dic = {root:None}
        def dfs(node):
            if node:
                if node.left:
                    dic[node.left] = node
                if node.right:
                    dic[node.right] = node
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        l1, l2 = p, q
        while(l1!=l2):
            l1 = dic.get(l1, q)
            l2 = dic.get(l2, p)
        return l1


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
            root = stringToTreeNode(line);
            line = next(lines)
            p = int(line);
            line = next(lines)
            q = int(line);

            ret = Solution().lowestCommonAncestor(root, p, q)

            out = treeNodeToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()