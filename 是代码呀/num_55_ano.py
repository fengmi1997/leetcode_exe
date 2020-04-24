# num_55
# 跳跃游戏
# 超时


class Solution:
    def canJump(self, nums) -> bool:
        # nums[i]是能跳的最远距离
        if len(nums) == 1 and nums[0] == 0:
            return True
        i = 0
        right = nums[i]
        while i < len(nums)-1:
            if right >= len(nums) - 1:
                return True
            for j in range(i, right+1):
                right = max(nums[j]+j, right)
            if i == right:
                if i < len(nums):
                    return False
                else:
                    return True
            i += 1
        return True


if __name__ == '__main__':
    nums = [5,9,3,2,1,0,2,3,3,1,0,0]
    print(Solution().canJump(nums))