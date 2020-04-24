# num_3
# 无重复字符的最长子串
# 双指针控制窗口的移动


class Solution:
    def lengthOfLongestSubstring(self, digits):
        if digits == '':
            output = 0
        else:
            substring = []
            i, j = 0, 1
            substring.append(digits[i])
            length = len(substring)
            output = length
            while j < len(digits):
                if digits[j] in substring:
                    index = substring.index(digits[j])
                    substring.append(digits[j])
                    substring = substring[index+1:]
                    output = max(output, length)
                    i, j = index + 1, j + 1
                else:
                    substring.append(digits[j])
                    length = len(substring)
                    output = max(output, length)
                    j += 1
        return output


if __name__ == '__main__':
    digits = "pwwkew"
    print(Solution().lengthOfLongestSubstring(digits))