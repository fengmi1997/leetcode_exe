# num_22
# 括号生成

class Solution:
    def generateParenthesis(self, n):

        def allPossible(one_res):
            if one_res.count('(') == n and one_res.count(')') == n:
                stack = []
                stack.append(one_res[0])
                for i in range(1,len(one_res)):
                    if stack == []:
                        stack.append(one_res[i])
                    elif stack[-1] == "(" and one_res[i] == ")":
                        stack.pop()
                    else:
                        stack.append(one_res[i])
                if stack == []:
                    res.append(one_res)
            if one_res.count('(') < n:
                allPossible(one_res+"(")
            if one_res.count(")") < n:
                allPossible(one_res + ")")

        res = []
        one_res = ''
        allPossible(one_res)

        return res


if __name__ == '__main__':
    n = 3
    print(Solution().generateParenthesis(n))