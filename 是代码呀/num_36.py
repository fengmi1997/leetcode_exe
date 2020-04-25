# num_36
class Solution:
    def isValidSudoku(self, board) -> bool:
        # 判断这九个数是不是只出现了一次
        def repeat(nums):
            dic = {}
            for i in range(len(nums)):
                if nums[i] not in dic:
                    dic[nums[i]] = 1
                else:
                    dic[nums[i]] += 1
                    if nums[i] != '.':
                        # 重复了
                        return 1
            return 0

        for i in range(len(board)):
            res = repeat(board[i][:])
            if res == 1:
                return False

        for i in range(len(board)):
            nums=[]
            for j in range(len(board)):
                nums +=board[j][i]
            if repeat(nums) == 1:
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                res = repeat(board[i][j:j+3]+board[i+1][j:j+3]+board[i+2][j:j+3])
                if res == 1:
                    return False
        return True
