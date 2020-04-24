class Solution:
    def canPartition(self, nums):
        dp1 = [[0]*len(nums) for _ in range(len(nums))]
        dp2 = [[0]*len(nums) for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i == j:
                    dp1[i][j] = nums[i]
                else:
                    dp1[i][j] = dp1[i][j-1]+nums[j]
                if i == 0 and j == len(nums)-1:
                    sum = dp1[i][j]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                dp2[i][j] = sum-dp1[i][j]
                if dp1[i][j] == dp2[i][j]:
                    return True
        return False



if __name__ == '__main__':
    nums = [23,13,11,7,6,5,5]
    print(Solution().canPartition(nums))