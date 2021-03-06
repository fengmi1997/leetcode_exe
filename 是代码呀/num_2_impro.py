# num_2
# 两数相加
# 改进版

import json
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1.val + l2.val < 10:
            l = ListNode(l1.val + l2.val)
            flag = 0
        else:
            l = ListNode(l1.val + l2.val - 10)
            flag = 1
        l1 = l1.next
        l2 = l2.next
        res = l
        while l1 is not None or l2 is not None:
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            if x + y + flag < 10:
                node = ListNode(x + y + flag)
                flag = 0
            else:
                node = ListNode(x + y - 10 + flag)
                flag = 1
            if l1 is not None: l1 = l1.next
            if l2 is not None: l2 = l2.next
            l.next = node
            l = l.next
        if l1 is None and l2 is None and flag==1:
            l.next = ListNode(1)
        return res


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
            l1 = stringToListNode(line);
            line = next(lines)
            l2 = stringToListNode(line);

            ret = Solution().addTwoNumbers(l1, l2)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()