# ac版本
# 最长公共前缀

# i指针在单词里循环，j指针在字符串里循环


class Solution(object):
    def longestCommonPrefix(self, strs):
        results = ''
        if strs == []:
            return results
        for i in range(0, len(strs[0])):
            results = results + strs[0][i]
            for j in range(1, len(strs)):
                if len(strs[j]) > i and strs[j][i] == strs[0][i]:
                    j += 1
                else:
                    results_list = list(results)
                    results_list.pop(-1)
                    results = ''.join(results_list)
                    return results
        return results


if __name__ == '__main__':
    strs = ['aa', 'a']
    print(Solution().longestCommonPrefix(strs))