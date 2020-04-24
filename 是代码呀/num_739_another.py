# num_739
# 每日温度
# tag是栈
# 根据思路写出来了
"""
确保栈里面的元素递减
栈里面既要保存T的元素，也要保存下标
"""


class Solution:
    def dailyTemperatures(self, T):
        result = [0]*len(T)
        stack = []
        # i是栈顶的下标,j是即将入栈的下标
        i, j = 0, 1
        stack.append([i, T[i]])
        for j in range(1, len(T)):
            i, ele = stack[-1][0], stack[-1][1]
            while T[j] > ele:
                stack.pop()
                result[i] = j - i
                if stack:
                    i, ele = stack[-1][0], stack[-1][1]
                else:
                    break
            stack.append([j, T[j]])
        return result


if __name__ == '__main__':
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    print(Solution().dailyTemperatures(T))