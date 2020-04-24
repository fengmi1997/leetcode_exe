# num_155
# 最小栈
# 简单

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._data = []

    def push(self, x: int) -> None:
        self._data.append(x)

    def pop(self) -> None:
        self._data.pop()

    def top(self) -> int:
        return self._data[-1]

    def getMin(self) -> int:
        return min(self._data)


if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    print(minStack.getMin())