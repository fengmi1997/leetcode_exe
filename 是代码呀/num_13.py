# ac版本
# 罗马数字转整数
# IVXLCDM
# 1,5,10,50,100,500,1000
# 完全是学习别人的


class Solution(object):
    def romanToInt(self, s):
        # 先定义一个字典来存罗马数字
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        results = 0
        for i in range(len(s)-1):
            if dic[s[i]] >= dic[s[i+1]]:
                results = results + dic[s[i]]
            else:
                results = results - dic[s[i]]
        results = results + dic[s[len(s)-1]]
        return results


if __name__ == '__main__':
    s = 'MCMXCIV'
    print(Solution().romanToInt(s))