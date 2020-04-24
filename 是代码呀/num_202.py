class Solution:
    def isHappy(self, n: int) -> bool:
        s = str(n)
        def compute(s):
            res = 0
            for i in range(len(s)):
                res += pow(int(s[i]),2)
            return res
        num = [n]
        new_num = compute(s)
        if new_num == 1:
            return True
        while new_num != 1:
            if new_num in num:
                return False
            num.append(new_num)
            new_num = compute(str(new_num))
            if new_num == 1:
                return True


if __name__=='__main__':
    print(Solution().isHappy(2))