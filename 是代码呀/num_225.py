# num_225
# 用队列实现栈

import queue as q


class MyStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q1 = q.Queue()
        self._q2 = q.Queue()

    def push(self, x: int) -> None:
        self.q1.put(x)

    def pop(self) -> int:
        for i in range(self.q1.qsize() - 1):
            x = self.q1.get()
            self._q2.put(x)
        top_num = self.q1.get()
        self.q1.queue.clear()
        for i in range(self._q2.qsize()):
            x = self._q2.get()
            self.q1.put(x)
        return top_num

    def top(self) -> int:
        for i in range(self.q1.qsize() - 1):
            x = self.q1.get()
            self._q2.put(x)
        top_num = self.q1.get()
        self._q2.put(top_num)
        for i in range(self._q2.qsize()):
            x = self._q2.get()
            self.q1.put(x)
        self._q2.queue.clear()
        return top_num

    def empty(self) -> bool:
        return self.q1.empty()


if __name__ == '__main__':
    myStack = MyStack()
    myStack.push(1)
    myStack.push(2)
    print(myStack.top())
    print(myStack.pop())
    myStack.empty()