# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # 每次找到单链表的中间位置,如果是偶数，就是正中间；如果是奇数，就是靠右边的位置
        def heaper(head):
            if head is None:
                return None
            cur, mid = head, head
            # 用cur去记录长度
            len = 0
            while cur is not None:
                len += 1
                cur = cur.next
            num = 0
            while num != ((len//2)-1):
                num += 1
                if mid.next is not None:
                    mid = mid.next
                else:
                    break
            if mid.next is not None:
                root = TreeNode(mid.next.val)
                # 生成两个单链表
                tail = mid
                if mid.next is not None:
                    mid = mid.next.next
                if tail is not None:
                    tail.next = None
                root.left = heaper(head)
                root.right = heaper(mid)
                return root
            else:
                root = TreeNode(mid.val)
                head = None
                mid = None
                root.left = heaper(head)
                root.right = heaper(mid)
                return root
        return heaper(head)





import json
def stringToIntegerList(input):
    return json.loads(input)


def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


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
            head = stringToListNode(line);

            ret = Solution().sortedListToBST(head)

            out = treeNodeToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()