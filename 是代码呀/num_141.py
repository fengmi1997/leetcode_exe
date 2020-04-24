# num_141
# 环形链表
# 在参考思路的基础上，写出来了
# 在playground的基础上，增加了一个函数def ListToCircle
# 解题思路
"""
设置两个指针，slow每次移动一个位置，fast每次移动两个位置
如果有环的话，fast == slow
如果没有环的话，fast会等于NONE
"""

import json

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        if head is None:
            return False
        else:
            slow = head
            fast = head.next
            while fast is not None:
                if fast == slow:
                    return True
                slow = slow.next
                if fast.next:
                    fast = fast.next.next
                else:
                    break
            return False



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

def ListToCircle(head,pos):
    # 根据pos的位置给单链表中增加一个环
    if pos == -1:
        return head
    else:
        cur = head
        count = 0
        while cur.next:
            if count == pos:
                circle = cur
            count += 1
            cur = cur.next
        cur.next = circle
        return head



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
            pos = int(line);
            head = ListToCircle(head,pos)

            ret = Solution().hasCycle(head)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()