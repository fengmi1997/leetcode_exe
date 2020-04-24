# num_739
# 每日温度
# tag是栈，但很明显首先想到的就是遍历
# 暴力法果然超时

class Solution:
    def dailyTemperatures(self, T):
        result = []
        for i in range(len(T)):
            for j in range(i, len(T)):
                if T[j] > T[i]:
                    result.append(j-i)
                    break
                if j == len(T) - 1:
                    result.append(0)
        return result


if __name__ == '__main__':
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    print(Solution().dailyTemperatures(T))