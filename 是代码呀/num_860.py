# num_860
# 思路很简单：尽量留下5


class Solution:
    def lemonadeChange(self, bills) -> bool:
        # 用哈希表记录剩余的钱数
        dic = {5:0,10:0,20:0}
        for i in range(len(bills)):
            if bills[i] == 5:
                dic[5] += 1
            elif bills[i] == 10:
                dic[10] += 1
                dic[5] -= 1
                if dic[5] < 0:
                    return False
            else:
                dic[20] += 1
                if dic[10] > 0:
                    dic[10] -= 1
                    dic[5] -= 1
                else:
                    dic[5] -= 3
                if dic[5] < 0 or dic[10] < 0:
                    return False
        return True

if __name__ == '__main__':
    bills = [5,5,5,10,20]
    print(Solution().lemonadeChange(bills))