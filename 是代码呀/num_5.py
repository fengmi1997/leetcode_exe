# num_5
# 最长回文子串
# 自己写出来了,官方题解有好几种，但是我没看

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for index in range(len(s)):
            # 对于每一个index,开始左右进行遍历,单个是回文
            flag = 1
            dp = s[index]
            i = index - 1
            j = index + 1
            # 找到这个中间字符相同的部分
            while j<len(s):
                if s[index] == s[j]:
                    dp = dp+s[j]
                    j+=1
                else:
                    break
            # 从相同的开始向前向后遍历，直到找到最大的回文
            while i>-1 and j<len(s) and flag==1:
                if s[i] == s[j]:
                    dp = s[i] + dp + s[j]
                    i-=1
                    j+=1
                else:
                    flag = 0
            if len(dp)>len(res):
                res = dp
        return res


if __name__ == '__main__':
    s = "bananas"
    print(Solution().longestPalindrome(s))