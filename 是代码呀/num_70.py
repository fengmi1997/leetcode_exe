# num_70
# 爬楼梯

# 回溯超时了
class Solution:
    def climbStairs(self, n: int) -> int:

        def repeat(sum):
            if sum == n:
                res[0] += 1
                return
            if sum > n:
                return
            for i in range(1, 3):
                repeat(sum+i)
        res = [0]
        repeat(0)
        return res[0]


if __name__ == '__main__':
    n = 35
    print(Solution().climbStairs(n))