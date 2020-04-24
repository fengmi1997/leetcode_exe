class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        while n > 0:
            n //= 5
            res += n
        return res

if __name__=='__main__':
    n = 125
    print(Solution().trailingZeroes(n))