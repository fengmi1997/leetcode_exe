class Solution:
    def lengthOfLIS(self, nums) -> int:
        if nums == []:
            return 0
        max_res = 1
        for i in range(0,len(nums)):
            res = 1
            tmp = nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] > tmp:
                    tmp = nums[j]
                    res += 1
            max_res = max(res, max_res)
        return max_res

print(Solution().lengthOfLIS(nums=[10,9,2,5,3,4]))