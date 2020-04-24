# num_55
# 跳跃游戏
# 有缺陷，没有办法ac


class Solution:
    def canJump(self, nums) -> bool:
        if len(nums) == 1 and nums[0] == 0:
            return True
        index = len(nums)-1
        while nums[index] > 0 and index > 0:
            index -= 1
        if index == 0 and nums[index] > 0:
            return True
        if index == 0 and nums[index] == 0:
            return False
        if index == len(nums)-1:
            for i in range(0, index):
                if nums[i] >= index-i:
                    return True
        if index < len(nums)-1:
            for i in range(0, index):
                if nums[i] > index-i:
                    return True
        return False


if __name__ == '__main__':
    nums = [1,0,1,0]
    print(Solution().canJump(nums))