# num_160
# 相交链表
"""
 //题解：设链表A的长度为a+c，链表B的长度为b+c，a为链表A不公共部分，b为链表B不公共部分，c为链表A、B的公共部分
 //将两个链表连起来，A->B和B->A，长度：a+c+b+c=b+c+a+c，
 若链表AB相交，则a+c+b与b+c+a就会抵消，它们就会在c处相遇
 若不相交，则c为nullptr，则a+b=b+a，它们各自移动到尾部循环结束，即返回nullptr
"""

import json

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self,headA,headB):
        ha, hb = headA, headB
        while ha != hb:
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA
        return ha

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