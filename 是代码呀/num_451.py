# num_451
# 根据字符出现频率排序
# 根据别人的思路写的


class Solution:
    def frequencySort(self, s: str) -> str:
        # 创建字典，{‘c’：num}
        dic = {}
        for c in s:
            if c not in dic:
                dic[c] = 1
            else:
                dic[c] += 1
        # 根据num排序
        new_dic = sorted(dic.items(), key=lambda item:item[1],reverse=True)
        res = []
        for index in new_dic:
            res.append(index[0]*index[1])
        return ''.join(res)


if __name__ == '__main__':
    s = "Aabb"
    print(Solution().frequencySort(s))