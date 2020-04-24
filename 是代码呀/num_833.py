# num_833
# 字符串中的查找与替换
# 自己写的


class Solution:
    def findReplaceString(self, S, indexes, sources, targets):
        flag = [0]*len(indexes)
        result = S
        for index in range(len(indexes)):
            # 判断能否对应上
            for i in range(len(sources[index])):
                if S[indexes[index]+i] != sources[index][i]:
                    flag[index] = 1
            # 如果对应的上，执行替换操作
            if flag[index] == 0:
                left = S[0:indexes[index]]
                right = S[indexes[index]+len(sources[index]):]
                result = left+targets[index]+right
                # 替换之后，比indexes[index]的数大的话，要更新一下
                if index < len(indexes) - 1:
                    for t in range(index+1, len(indexes)):
                        if indexes[t] > indexes[index]:
                            indexes[t] = indexes[t]+len(result)-len(S)
                    S = result
        return result


if __name__ == '__main__':
    S = "jjievdtjfb"
    indexes = [4,6,1]
    sources = ["md","tjgb","jf"]
    targets = ["foe","oov","e"]
    print(Solution().findReplaceString(S,indexes,sources,targets))


