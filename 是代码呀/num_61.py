# num_61
# 旋转链表
# 自己写出来了

import json
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # 首先把链表尾部链接到头部
        # count，记下链表的长度
        count = 0
        cur = head
        if cur is None:
            return cur
        else:
            while cur.next is not None:
                cur = cur.next
                count += 1
            count += 1
            cur.next = head
            # 找到新链表的头部,链表头部的位置是count-k
            new_head = head
            new_tail = head
            num_head = 0
            while num_head != (count-(k % count)-1):
                new_head = new_head.next
                new_tail = new_tail.next
                num_head += 1
            new_head = new_head.next
            new_tail.next = None
            return new_head


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


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


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
            line = next(lines)
            k = int(line);

            ret = Solution().rotateRight(head, k)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()