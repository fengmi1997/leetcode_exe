# num_82
# 删除排序链表中的重复元素2
# question:
# 为什么实例一这样的可以删，示例二那样重复元素在最开始就失败啊
# 回答：对于头指针重复的时候，注意头指针要把head进行移动


import json
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pre = ListNode(-1)
        flag_num = 0
        pre.next = head
        cur = head
        count = 0
        # 设置一个标识符，如果出现了删减，说明要把cur指向的元素删除
        while cur is not None:
            count += 1
            num = 0
            tail = cur.next
            while tail is not None:
                if tail.val == cur.val:
                    cur.next = tail.next
                    tail = cur.next
                    num = 1
                else:
                    tail = tail.next
            if num == 1:
                if count == 1 or count == flag_num + 1:
                    head = cur.next
                    flag_num = count
                pre.next = cur.next
                cur = pre.next
            else:
                pre = cur
                cur = cur.next
        return head

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

            ret = Solution().deleteDuplicates(head)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()