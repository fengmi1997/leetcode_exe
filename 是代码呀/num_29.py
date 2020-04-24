# num_29
# 提交的别人的代码


class Solution:
    def divide(self, divd: int, dior: int) -> int:
        '''
        超时
        res = 0
        flag=1
        if dividend>0 and divisor<0:
            flag=0
        if dividend<0 and divisor>0:
            flag=0
        dividend,divisor = abs(dividend),abs(divisor)
        while dividend>=0:
            res += 1
            dividend-=divisor
        res-=1
        return res if flag==1 else -res
        '''
        res = 0
        sign = 1 if divd ^ dior >= 0 else -1
        # print(sign)
        divd = abs(divd)
        dior = abs(dior)
        while divd >= dior:
            tmp, i = dior, 1
            while divd >= tmp:
                divd -= tmp
                res += i
                i <<= 1
                tmp <<= 1
        res = res * sign
        return min(max(-2 ** 31, res), 2 ** 31 - 1)

print(Solution().divide(10,3))