# num_833
# 字符串中的查找与替换
# 改进版


class Solution:
    def findReplaceString(self, S, indexes, sources, targets):
        flag = [0]*len(indexes)
        result = S
        # sort by indexes
        sorted_indexes = sorted(range(len(indexes)), key=lambda k: indexes[k])
        indexes = [indexes[i] for i in sorted_indexes]
        sources = [sources[i] for i in sorted_indexes]
        targets = [targets[i] for i in sorted_indexes]

        for index in range(len(indexes)):
            num = indexes[index]
            # 判断能否对应上
            if S[num:num+len(sources[index])] != sources[index][:]:
                flag[index] = 1
            # 如果对应的上，执行替换操作
            if flag[index] == 0:
                left = S[0:num]
                right = S[num+len(sources[index]):]
                result = left+targets[index]+right
                # 替换之后，比indexes[index]的数大的话，要更新一下
                if index < len(indexes) - 1:
                    for t in range(index + 1, len(indexes)):
                        indexes[t] = indexes[t] + len(result) - len(S)
                    S = result
        return result


if __name__ == '__main__':
    S = "abcd"
    indexes = [0,2]
    sources = ["a", "cd"]
    targets = ["eee", "ffff"]
    print(Solution().findReplaceString(S,indexes,sources,targets))


