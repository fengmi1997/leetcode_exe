# num_20
# 有效的括号
# 用栈来存储数据


class Solution:
    def isValid(self, digits):
        lefty = '([{'
        right = ')]}'
        stack = []
        if len(digits) == 0:
            return True
        else:
            stack.append(digits[0])
            i = 1
            while i < len(digits):
                # stack[-1]就相当与top
                if (digits[i] in right) and len(stack) > 0 and (stack[-1] in lefty) and right.index(digits[i]) == lefty.index(stack[-1]):
                    stack.pop()
                else:
                    stack.append(digits[i])
                i += 1
            if len(stack) == 0:
                return True
            else:
                return False


if __name__ == '__main__':
    digits = '[])'
    print(Solution().isValid(digits))