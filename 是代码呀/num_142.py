# num_142
# 在num_141的基础上稍加改动
# 环形链表,我第一次想的是new_head比slow慢一步，但是这是不对的，有可能第一次快慢指针相遇时，new_head并不是头节点
# 参考了评论区的思路
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
    """
    要在第一次相遇后，让两个指针再次相遇，此次相遇在入环处
    """
    def detectCycle(self, head) -> None:
        if head is None:
            return None
        else:
            slow = head
            fast = head
            while fast is not None:
                slow = slow.next
                if fast.next:
                    fast = fast.next.next
                else:
                    break
                if fast == slow:
                    fast = head
                    while fast != slow:
                        fast = fast.next
                        slow = slow.next
                    return slow
            return None



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
        if count == pos:
            circle = cur
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

            ret = Solution().detectCycle(head)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()