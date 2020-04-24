# num_55
# 跳跃游戏
# ac


class Solution:
    def canJump(self, nums) -> bool:
        # nums[i]是能跳的最远距离
        if len(nums) == 1 and nums[0] == 0:
            return True
        max_right = 0
        for i in range(len(nums)):
            # 如果当前位置能到达，当前位置+跳数>最远位置
            if i <= max_right and max_right < i+nums[i]:
                max_right = nums[i]+i
        if max_right >= len(nums)-1:
            return True
        else:
            return False


if __name__ == '__main__':
    nums = [2,0,0]
    print(Solution().canJump(nums))