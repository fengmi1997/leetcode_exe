# num_160
# 相交链表
# question:playground与类的输入不一致？？回答：playground中的有些函数需要自己构造
# 用两个指针来循环，会超出时间限制，此时时间复杂度为O(n^2)

import json

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self,headA,headB):
        ha, hb = headA, headB
        while ha:
            while hb:
                if ha.next == hb.next:
                    if ha == hb:
                        return ha
                    return ha.next
                hb = hb.next
            ha = ha.next
            hb = headB
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

def ListToNewlist(listA,listB,skipA,skipB):
    countA,countB = 1,1
    curA = listA
    while countA < skipA:
        curA = curA.next
        countA += 1
    curB = listB
    while countB < skipB:
        curB = curB.next
        countB += 1
    # 此时curA,curB分别指向相交节点的前一个
    curB.next = curA.next
    return listA,listB


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
            intersectVal = int(line);
            line = next(lines)
            listA = stringToListNode(line);
            line = next(lines)
            listB = stringToListNode(line);
            line = next(lines)
            skipA = int(line);
            line = next(lines)
            skipB = int(line);

            listA,listB = ListToNewlist(listA,listB,skipA,skipB)


            ret = Solution().getIntersectionNode(listA, listB)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()