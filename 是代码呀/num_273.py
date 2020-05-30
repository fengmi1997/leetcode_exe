# ac
# 整数转英文
#
#
# 自己写的，就是有点复杂


class Solution(object):
    def numberToWords(self, num):
        # 定义一个字典
        dic = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
               6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
               11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
               16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty',
               30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy',
               80: 'Eighty', 90: 'Ninety', 100: 'Hundred', 1000: 'Thousand', 1000000: 'Million',
               1000000000: 'Billion'}
        if num == 0:
            s = 'Zero'
            return s
        s = ''
        while num > 0:
            if num >= 100:
                for big_key in list(dic.keys())[-4:][::-1]:
                    reminder = num // big_key
                    if reminder == 0:
                        continue
                    t = ''
                    bakup_reminder = reminder
                    while reminder > 0:
                        if reminder >= 100:
                            reminder_for_cal = reminder // 100
                            t += dic[reminder_for_cal] + ' ' + dic[100] + ' '
                            reminder -= reminder_for_cal * 100
                        elif (reminder < 100) and (reminder >= 21):
                            for key in list(dic.keys())[-12:-4][::-1]:
                                reminder_for_cal = reminder // key
                                if reminder_for_cal == 0:
                                    continue
                                t += dic[key] + ' '
                                reminder -= reminder_for_cal * key
                                break
                        else:
                            t += dic[reminder] + ' '
                            reminder -= reminder
                    s = s + t + dic[big_key] + ' '
                    num -= bakup_reminder * big_key
            elif (num < 100) and (num >= 21):
                for key in list(dic.keys())[-12:-4][::-1]:
                    reminder = num // key
                    if reminder == 0:
                        continue
                    s = s + dic[key] + ' '
                    num -= reminder * key
            else:
                for key in list(dic.keys())[:20]:
                    if num == key:
                        s = s + dic[key] + ' '
                        num -= key
                        break
            if num == 0:
                results = s.strip()
        return results


if __name__ == '__main__':
    num = 36
    print(Solution().numberToWords(num))