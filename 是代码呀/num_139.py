# num_139
# 单词拆分
# 递归居然又超时了，晕
# 递归的时候，如何退出整个递归???
#
# class Solution:
#     def wordBreak(self, s: str, wordDict) -> bool:
#         def repeat(s):
#             if s.isspace():
#                 res[0] = True
#                 return
#             for word in wordDict:
#                 if word in s:
#                     repeat(s.replace(word, ' '))
#         res = [False]
#         repeat(s)
#         return res[0]

# 还是超时
# class Solution:
#     def wordBreak(self, s: str, wordDict) -> bool:
#         def repeat(s, i):
#             if s.isspace():
#                 return True
#             for j in range(i, len(wordDict)):
#                 word = wordDict[j]
#                 if (word in s) and (repeat(s.replace(word, ' ', 1), j)):
#                     return True
#             return False
#         wordDict = sorted(wordDict)
#         return repeat(s, 0)

class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        import functools
        @functools.lru_cache(None)
        def repeat(s):
            if s == '':
                return True
            for j in range(len(s)+1):
                if (s[:j] in wordDict) and (repeat(s[j:])):
                    return True
            return False
        return repeat(s)


if __name__ == '__main__':
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
    print(Solution().wordBreak(s,wordDict))
