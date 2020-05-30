# ac版本
# 整数转罗马数字
# IVXLCDM
# 1,5,10,50,100,500,1000
# 建立哈希表后，直接从高到低遍历取整


class Solution(object):
    def intToRoman(self, num):
        # 先定义一个字典来存罗马数字
        dic = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
               90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        s = ''
        for key in list(dic.keys())[::-1]:
            # 从最高位开始算整数
            reminder = num // key
            s += reminder * dic[key]
            num -= key * reminder
        return s


if __name__ == '__main__':
    num = 1
    print(Solution().intToRoman(num))