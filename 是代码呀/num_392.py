# num_392
# 就用很简单的查找做出来的

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in range(len(s)):
            index = t.find(s[i])
            if index>=0:
                t = t[index+1:]
            else:
                return False
        return True


if __name__ == '__main__':
    s = 'abc'
    t = 'ahbgadc'
    print(Solution().isSubsequence(s,t))