# num_17
# 电话号码的字母组合


class Solution:
    def letterCombinations(self, digits):
        #  先定义一个字典来存电话号码对应的数字
        #  定义一个[]来存储
        output = []
        dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
               '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        #  定义一个回溯的算法

        def backtrack(combination, digits):
            if len(digits) == 0:
                output.append(combination)
            else:
                index = digits[0]
                for letter in dic[index]:
                    backtrack(combination + letter, digits[1:])
        if digits:
            backtrack('', digits)
        return output


if __name__ == '__main__':
    digits = ''
    print(Solution().letterCombinations(digits))