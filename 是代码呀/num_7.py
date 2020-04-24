class Solution:
    def reverse(self, x: int) -> int:
        # 用栈应该是可以的
        nums = str(x)
        stack = []
        res=''
        flag = 1
        if nums[0] == '-':
            flag = 0
            nums = nums[1:]
        for i in range(0,len(nums)):
            stack.append(nums[i])
        for i in range(len(nums)-1,-1,-1):
            if nums[0] == '0':
                stack = stack[:i]
            else:
                break
        for i in range(len(nums)-1,-1,-1):
            res+=nums[i]
        if flag == 0:
            return -int(res)
        else:
            return int(res)

if __name__ == '__main__':
    x = 123
    print(Solution().reverse(x))