# num_234
# 回文链表
# 在链表里寻找元素是O(n),把链表变成一个顺序表，设置两个指针去判断是否回文
# 但是这个时间还是不是O(n)

import json
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        cur = head
        new_list = []
        while cur:
            new_list.append(cur.val)
            cur = cur.next
        i = 0
        j = len(new_list) - 1
        while i < ((len(new_list))/2):
            if new_list[i] != new_list[j]:
                return False
            else:
                i += 1
                j -= 1
        return True





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

            ret = Solution().isPalindrome(head)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()