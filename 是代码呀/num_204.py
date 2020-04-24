# 需要复习

class Solution:
    def countPrimes(self, n: int) -> int:
        # 超时
        # res = 2
        # if n <= 2:
        #     return 0
        # if n <= 3:
        #     return 1
        # for i in range(4, n):
        #     flag = 0
        #     for j in range(2, int(pow(i, 1 / 2))+1):
        #         if i % j == 0:
        #             flag = 1
        #             break
        #     if flag == 0:
        #         res += 1
        # return res

        if n < 2: return 0
        isPrimes = [1] * n  # 立flag
        isPrimes[0] = isPrimes[1] = 0  # 设置0和1位为0
        # 下面的思路是在 2 到 根号n 的范围内，当一个数是质数，将它所有的比n小的倍数设置成0
        for i in range(2, int(n ** 0.5) + 1):
            if isPrimes[i] == 1:
                # 哇这个切片真的是pythonic
                isPrimes[i * i: n: i] = [0] * len(isPrimes[i * i: n: i])
        # 现在每个质数位的flag为1，其余的位数为0.由于我们不需要知道质数是什么只要总数，因此直接返回list里面所有1的和就行。
        return sum(isPrimes)

print(Solution().countPrimes(10))